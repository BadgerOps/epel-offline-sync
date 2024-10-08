#!/usr/bin/env python3.9

# we lock to python 3.9 for now...

import os
import urllib.request
import gzip
import xml.etree.ElementTree as ET
import configparser
import argparse
import logging
import time
import threading
import hashlib
from datetime import datetime
import concurrent.futures


def monitor_thread_activity(interval=30):
    """
    Quick and dirty little method to monitor thread status, because large numbers of files take a while to download
    """
    while True:
        # Get a list of all active Thread objects
        active_threads = threading.enumerate()
        # Prepare a string with the names of active threads
        active_thread_names = ', '.join(thread.name for thread in active_threads if thread.name not in ["MainThread", "Thread-Monitor"])
        # Log the count and names of the active threads (excluding the main thread and the monitor thread)
        logging.info(f"Active threads ({len(active_threads) - 2}): {active_thread_names}")
        time.sleep(interval)

def load_config(config_file='./config.ini'):
    logging.debug("loading configuration data from config.ini")
    config = configparser.ConfigParser()
    config.read(config_file)
    return config


class EPELDownloader:
    """
    Initiate a class for downloading packages from EPEL
    The __init__ method sets up some scaffolding  that we'll use in the rest of the program
    """
    def __init__(self, base_url, local_dir, threads):
        self.base_url = base_url
        self.local_dir = local_dir
        os.makedirs(self.local_dir, exist_ok=True)
        self.parse_arguments()
        self.num_threads = threads
        self.num_packages_downloaded = 0
        self.setup_logging(log_file=self.args.log)
        self.start_time = time.time()
        logging.info(f"Initialized EPELDownloader for {base_url} with local dir {local_dir}")

    def parse_arguments(self):
        parser = argparse.ArgumentParser(description="Download packages from EPEL")
        parser.add_argument('-f', '--force', action='store_true', help="Force re-download of everything")
        parser.add_argument('-d', '--debug', action='store_true', help="Turn on debug options")
        parser.add_argument('-t', '--threads', type=int, default=4, help="Number of threads to use for downloading") # not used yet
        parser.add_argument('-c', '--config', default='./config.ini', help="Path to the config file") # not used yet
        parser.add_argument('-l', '--log', default='epel/logs/epel_manager.log', help="Path to the log file")
        parser.add_argument('-q', '--quiet', action='store_true', help="Suppress output to console")
        self.args = parser.parse_args()

    def setup_logging(self, log_file='./epel_manager.log'):
        """
        Default to logging to ./epel_manager.log, but also log to stdout if in debug mode
        Also accept a log_file argument to log to a different file
        Use standard formatter
        """
        os.makedirs(os.path.dirname(log_file), exist_ok=True)
        logger = logging.getLogger()
            # Remove all existing handlers
        for handler in logger.handlers[:]:
            logger.removeHandler(handler)

        if self.args.debug:
            logger.setLevel(logging.DEBUG)
        else:
            logger.setLevel(logging.INFO)

        formatter = logging.Formatter('[%(asctime)s] %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

        # Create a file handler and set level to info
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        if not self.args.quiet:
            # Create a stdout handler and set level to debug
            stout_handler = logging.StreamHandler()
            stout_handler.setFormatter(formatter)
            logger.addHandler(stout_handler)

    def timeFormatter(self, elapsed_time):
        """
        Take elapsed_time in milliseconds and return hours, minutes, seconds
        :param elapsed_time: time in milliseconds
        :return: hours, minutes, seconds
        """
        hours, remainder = divmod(elapsed_time, 3600)
        minutes, seconds = divmod(remainder, 60)
        return hours,minutes,seconds

    def fetch_xml(self, url):
        logging.info(f"Fetching XML from {url}")
        with urllib.request.urlopen(url) as response:
            return ET.parse(response)

    def get_repomd_path(self):
        primary_xml_path = os.path.join(self.base_url, 'repodata/repomd.xml')
        return primary_xml_path

    def fetch_and_extract_gz(self, url, extraction_path):
        with urllib.request.urlopen(url) as response:
            with gzip.GzipFile(fileobj=response) as uncompressed:
                with open(extraction_path, 'wb') as outfile:
                    try:
                        outfile.write(uncompressed.read())
                        return True
                    except EOFError:
                        logging.critical(f"unable to extract {url} to {extraction_path}")
                        return False

    def download_file(self, file_url):
        """
        Download a file from a given URL, with retries and exponential backoff
        :param file_url: The URL of the file to download
        :return: None
        """
        retries = 3
        timeout = 300  # 5 minutes timeout in seconds

        filename = file_url.split('/')[-1]
        filepath = os.path.join(self.local_dir, file_url.replace(self.base_url, ''))
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        for attempt in range(retries):
            try:
                with urllib.request.urlopen(file_url, timeout=timeout) as response, open(filepath, 'wb') as out_file:
                    out_file.write(response.read())
                logging.debug(f"Successfully downloaded {file_url}")
                break  # If download succeeds, break out of the loop
            except urllib.error.URLError as e:
                logging.warning(f"Attempt {attempt + 1} failed for {file_url}: {e}")
                if attempt < retries - 1:
                    time.sleep(2 ** attempt)  # Exponential backoff
                else:
                    logging.error(f"Failed to download {file_url} after {retries} attempts.")
                    pass  # Re-raise the last exception if all retries fail
            except Exception as e:
                logging.error(f"An error occurred while downloading {file_url}: {e}")
                pass

    def download_package_group(self, package_group, start_letter):
        """
        A method that is spun off as a thread to download all packages in a given group
        :param package_group: list of packages to download
        :param start_letter: the starting letter of the package group, used for thread naming
        :return: None
        """
        start_time = time.time()
        threading.current_thread().name = f"Thread-{start_letter.upper()}"
        logging.info(f"{threading.current_thread().name} started processing {len(package_group)} packages")
        thread_pkgs = 0
        for pkg_location in package_group:
            pkg_url = os.path.join(self.base_url, pkg_location)
            if self.args.force or self.file_needs_update(pkg_url, pkg_location):
                self.download_file(pkg_url)
                # increment thread & total package counters
                thread_pkgs += 1
                self.num_packages_downloaded += 1
            else:
                logging.debug(f"Not downloading package: {pkg_location} since it is up to date")
        elapsed_time = time.time() - start_time
        hours, minutes, seconds = self.timeFormatter(elapsed_time)
        logging.info(f"{threading.current_thread().name} finished processing: {thread_pkgs} packages downloaded in {int(hours)} hours, {int(minutes)} minutes, {seconds:.2f} seconds.")
        return

    def initialize_repo_files(self):
        """
        Download the repomd.xml file, prepare for processing packages
        We use the repomd.xml file to figure out what other xml files we need to download and validate
        :return:
        """
        logging.info(f"Downloading repomd.xml from {self.base_url}")
        repomd_path = self.get_repomd_path()
        self.download_file(repomd_path)
        tree = self.fetch_xml(repomd_path)
        root = tree.getroot()

        namespace = {'repo': 'http://linux.duke.edu/metadata/repo'}
        primary_xml_location = root.find("repo:data[@type='primary']/repo:location", namespaces=namespace).get('href')

        primary_xml_url = os.path.join(self.base_url, primary_xml_location)
        primary_xml_local_path = os.path.join(self.local_dir, "primary.xml")

        if not self.fetch_and_extract_gz(primary_xml_url, primary_xml_local_path):
            time.sleep(5)
            # try one more time
            if not self.fetch_and_extract_gz(primary_xml_url, primary_xml_local_path):
                logging.critical("could not download the primary.xml, exiting")
                os._exit(1)

        primary_tree = ET.parse(primary_xml_local_path)
        primary_root = primary_tree.getroot()

        logging.debug(f"Getting all repomd files...")
        for data in root.findall('{http://linux.duke.edu/metadata/repo}data'):
            if data.find('{http://linux.duke.edu/metadata/repo}location') is not None:
                href = data.find('{http://linux.duke.edu/metadata/repo}location').get('href')
                file_url = os.path.join(self.base_url, href)
                self.download_file(file_url)
            else:
                logging.debug(f"Already downloaded repomd")

    def enumerate_package_groups(self):
        """
        Use the previously downloaded package.xml and repomd.xml to figure out what packages to download
        :return: list of packages grouped by first letter to download
        """
        self.package_checksums = {}
        repomd_path = self.get_repomd_path()
        tree = self.fetch_xml(repomd_path)
        root = tree.getroot()
        namespace = {'repo': 'http://linux.duke.edu/metadata/repo'}
        primary_xml_location = root.find("repo:data[@type='primary']/repo:location", namespaces=namespace).get('href')
        primary_xml_url = os.path.join(self.base_url, primary_xml_location)
        primary_xml_local_path = os.path.join(self.local_dir, "primary.xml")
        logging.debug(f"primary xml local path is {primary_xml_local_path}")
        primary_tree = ET.parse(primary_xml_local_path)
        primary_root = primary_tree.getroot()

        package_namespace = {'common': 'http://linux.duke.edu/metadata/common'}
        packages = primary_root.findall("common:package", namespaces=package_namespace)
        grouped_packages = {}
        for pkg in packages:
            pkg_location = pkg.find("common:location", namespaces=package_namespace).get('href')
            checksum_elem = pkg.find("common:checksum[@type='sha256']", namespaces=package_namespace)
            if checksum_elem is not None:
                self.package_checksums[pkg_location] = checksum_elem.text
            start_letter = pkg_location.split('/')[1]  # Get the starting letter, for ease of threading.
            if start_letter not in grouped_packages:
                grouped_packages[start_letter] = []
            grouped_packages[start_letter].append(pkg_location)
        return grouped_packages

    def check_for_updates(self):
        # Compare local repomd.xml with remote one
        local_repomd_path = os.path.join(self.local_dir, "repodata/repomd.xml")
        if not os.path.exists(local_repomd_path):
            logging.info(f"Local repomd.xml does not exist. Running the initialize_repo_files method.")
            self.initialize_repo_files()

        local_repomd_tree = ET.parse(local_repomd_path)
        local_date = local_repomd_tree.find(".//{http://linux.duke.edu/metadata/repo}revision").text

        remote_repomd_tree = self.fetch_xml(os.path.join(self.base_url, "repodata/repomd.xml"))
        remote_date = remote_repomd_tree.find(".//{http://linux.duke.edu/metadata/repo}revision").text

        if local_date != remote_date:
            logging.info(f"Updates are available. Rerunning the initalize_repo_files method.")
            self.initialize_repo_files()
        else:
            logging.info(f"No updates are available for repomd.xml localdate: {local_date}, remotedate: {remote_date}")

    def get_local_path(self, file_url):
        """
        Given a file URL, return its local path.
        :param file_url: URL of the file to download
        :return: Local path to save the file
        """
        return os.path.join(self.local_dir, file_url.replace(self.base_url, ''))

    def file_needs_update(self, file_url, pkg_location):
        """
        Check if the file needs to be updated.
        :param file_url: URL of the file to download
        :param pkg_location: location of the package in the repo
        :return: True if the file needs to be updated, False otherwise
        """
        local_path = self.get_local_path(file_url)

        if not os.path.exists(local_path):
            return True  # file does not exist locally

        # Compute local file's SHA256 checksum
        with open(local_path, 'rb') as f:
            local_checksum = hashlib.sha256(f.read()).hexdigest()
        # Compare with remote checksum
        remote_checksum = self.package_checksums.get(pkg_location)
        if remote_checksum and local_checksum != remote_checksum:
            logging.debug(f"file size changed, re-downloading {file_url}")
            return True
        logging.debug(f"Local file hash matches, no need to re-download {file_url}")
        return False

    def get_total_files(self):
        """
        Get the total number of files in the downloaded repo
        Get the total size of the files in the downloaded repo
        :return: total number of files, total size of files
        """
        total_count = 0
        total_size = 0
        for root, dirs, files in os.walk(self.local_dir):
            for file in files:
                total_count += 1
                total_size += os.path.getsize(os.path.join(root, file))
        return total_count, total_size

    def main(self):
        """
        Main method to download the packages from EPEL using the repos specified in config.ini
        :return: None
        """
        grouped_packages = self.enumerate_package_groups()
        # Use ThreadPoolExecutor to download packages in parallel
        with concurrent.futures.ThreadPoolExecutor(max_workers=int(self.num_threads)) as executor:
            # Create futures list and populate as we start up threads
            futures = [executor.submit(self.download_package_group, package_group, start_letter) for start_letter, package_group in
                       grouped_packages.items()]

            # Wait for all threads to complete
            for future in concurrent.futures.as_completed(futures):
                future.result()

        # All threads have completed, shutdown the executor
        executor.shutdown()
        # calculate total file count and total repo size
        total_file_count, total_repo_size = self.get_total_files()
        # log total elapsed time and number of packages downloaded
        elapsed_time = time.time() - self.start_time
        hours, minutes, seconds = self.timeFormatter(elapsed_time)
        logging.info(f"Downloaded repo from {self.base_url} in {int(hours)} hours, {int(minutes)} minutes, and {seconds:.2f} seconds.")
        logging.info(f"Downloaded a total of {self.num_packages_downloaded} files")
        logging.info(f"Total files in the downloaded repo: {total_file_count}")
        # log total space used by the repo(s)
        total_size_gb = total_repo_size / (1024 * 1024 * 1024)
        total_size_mb = total_repo_size / (1024 * 1024)
        logging.info(f"Total space used by the repo: {total_size_gb:.2f} GB")

if __name__ == "__main__":
    """
    Main entry point for the program if we're running interactively
    """
    config = load_config()
    monitor = threading.Thread(target=monitor_thread_activity, name='Thread-Monitor', daemon=True)
    monitor.start()
    for version in config.sections():
        logging.info(f"Processing {version}...")
        base_url = config[version]['base_url']
        local_dir = config[version]['local_dir']
        threads = config[version]['threads']
        manager = EPELDownloader(base_url, local_dir, threads)
        manager.check_for_updates()
        manager.main()
