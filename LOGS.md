# Example log output

Below is a timed run of the epel offline sync tool:

```bash
time podman run -v /home/badger/code/epel-offline-sync/epelout:/app/epel localhost/test/epeldownloader:0.2
[2024-04-03 18:11:29] INFO - Initialized EPELDownloader for https://ftp.uni-stuttgart.de/epel/8/Everything/x86_64/ with local dir ./epel/8/
[2024-04-03 18:11:29] INFO - Fetching XML from https://ftp.uni-stuttgart.de/epel/8/Everything/x86_64/repodata/repomd.xml
[2024-04-03 18:11:29] INFO - No updates are available for repomd.xml localdate: 1712110674, remotedate: 1712110674
[2024-04-03 18:11:29] INFO - Fetching XML from https://ftp.uni-stuttgart.de/epel/8/Everything/x86_64/repodata/repomd.xml
[2024-04-03 18:11:29] INFO - Thread-3 started processing 1 packages
[2024-04-03 18:11:29] INFO - Thread-6 started processing 1 packages
[2024-04-03 18:11:29] INFO - Thread-A started processing 261 packages
[2024-04-03 18:11:29] INFO - Thread-B started processing 319 packages
[2024-04-03 18:11:29] INFO - Thread-C started processing 390 packages
[2024-04-03 18:11:29] INFO - Thread-D started processing 221 packages
[2024-04-03 18:11:29] INFO - Thread-F started processing 265 packages
[2024-04-03 18:11:29] INFO - Thread-3 finished processing: 0 packages downloaded in 0 hours, 0 minutes, 0.00 seconds.
[2024-04-03 18:11:29] INFO - Thread-6 finished processing: 0 packages downloaded in 0 hours, 0 minutes, 0.00 seconds.
[2024-04-03 18:11:29] INFO - Thread-G started processing 834 packages
[2024-04-03 18:11:29] INFO - Thread-H started processing 104 packages
[2024-04-03 18:11:29] INFO - Thread-I started processing 119 packages
[2024-04-03 18:11:30] INFO - Thread-I finished processing: 0 packages downloaded in 0 hours, 0 minutes, 0.19 seconds.
[2024-04-03 18:11:30] INFO - Thread-L started processing 896 packages
[2024-04-03 18:11:30] INFO - Thread-H finished processing: 0 packages downloaded in 0 hours, 0 minutes, 0.20 seconds.
[2024-04-03 18:11:30] INFO - Thread-M started processing 323 packages
[2024-04-03 18:11:59] INFO - Active threads (8): Thread-M, Thread-L, Thread-A, Thread-B, Thread-C, Thread-D, Thread-F, Thread-G
[2024-04-03 18:12:29] INFO - Active threads (8): Thread-M, Thread-L, Thread-A, Thread-B, Thread-C, Thread-D, Thread-F, Thread-G
[2024-04-03 18:12:30] INFO - Thread-D finished processing: 105 packages downloaded in 0 hours, 1 minutes, 0.28 seconds.
[2024-04-03 18:12:30] INFO - Thread-N started processing 291 packages
[2024-04-03 18:12:56] INFO - Thread-B finished processing: 215 packages downloaded in 0 hours, 1 minutes, 26.51 seconds.
[2024-04-03 18:12:56] INFO - Thread-O started processing 185 packages
[2024-04-03 18:12:59] INFO - Active threads (8): Thread-M, Thread-L, Thread-A, Thread-O, Thread-C, Thread-N, Thread-F, Thread-G
[2024-04-03 18:13:29] INFO - Active threads (8): Thread-M, Thread-L, Thread-A, Thread-O, Thread-C, Thread-N, Thread-F, Thread-G
[2024-04-03 18:13:51] INFO - Thread-N finished processing: 291 packages downloaded in 0 hours, 1 minutes, 21.11 seconds.
[2024-04-03 18:13:51] INFO - Thread-P started processing 2963 packages
[2024-04-03 18:13:56] INFO - Thread-C finished processing: 264 packages downloaded in 0 hours, 2 minutes, 26.41 seconds.
[2024-04-03 18:13:56] INFO - Thread-R started processing 469 packages
[2024-04-03 18:13:59] INFO - Active threads (8): Thread-M, Thread-L, Thread-A, Thread-O, Thread-R, Thread-P, Thread-F, Thread-G
[2024-04-03 18:14:19] INFO - Thread-O finished processing: 185 packages downloaded in 0 hours, 1 minutes, 23.38 seconds.
[2024-04-03 18:14:19] INFO - Thread-S started processing 445 packages
[2024-04-03 18:14:29] INFO - Active threads (8): Thread-M, Thread-L, Thread-A, Thread-S, Thread-R, Thread-P, Thread-F, Thread-G
[2024-04-03 18:14:29] INFO - Thread-M finished processing: 288 packages downloaded in 0 hours, 2 minutes, 59.67 seconds.
[2024-04-03 18:14:29] INFO - Thread-T started processing 356 packages
[2024-04-03 18:14:59] INFO - Active threads (8): Thread-T, Thread-L, Thread-A, Thread-S, Thread-R, Thread-P, Thread-F, Thread-G
[2024-04-03 18:15:00] INFO - Thread-A finished processing: 191 packages downloaded in 0 hours, 3 minutes, 30.33 seconds.
[2024-04-03 18:15:00] INFO - Thread-Z started processing 90 packages
[2024-04-03 18:15:29] INFO - Active threads (8): Thread-T, Thread-L, Thread-Z, Thread-S, Thread-R, Thread-P, Thread-F, Thread-G
[2024-04-03 18:15:33] INFO - Thread-Z finished processing: 90 packages downloaded in 0 hours, 0 minutes, 32.99 seconds.
[2024-04-03 18:15:33] INFO - Thread-E started processing 137 packages
[2024-04-03 18:15:33] INFO - Thread-F finished processing: 256 packages downloaded in 0 hours, 4 minutes, 3.61 seconds.
[2024-04-03 18:15:33] INFO - Thread-J started processing 101 packages
[2024-04-03 18:15:53] INFO - Thread-L finished processing: 875 packages downloaded in 0 hours, 4 minutes, 23.88 seconds.
[2024-04-03 18:15:53] INFO - Thread-K started processing 570 packages
[2024-04-03 18:15:59] INFO - Active threads (8): Thread-T, Thread-K, Thread-E, Thread-S, Thread-R, Thread-P, Thread-J, Thread-G
[2024-04-03 18:16:11] INFO - Thread-E finished processing: 137 packages downloaded in 0 hours, 0 minutes, 37.82 seconds.
[2024-04-03 18:16:11] INFO - Thread-Q started processing 159 packages
[2024-04-03 18:16:29] INFO - Active threads (8): Thread-T, Thread-K, Thread-Q, Thread-S, Thread-R, Thread-P, Thread-J, Thread-G
[2024-04-03 18:16:48] INFO - Thread-T finished processing: 356 packages downloaded in 0 hours, 2 minutes, 18.75 seconds.
[2024-04-03 18:16:48] INFO - Thread-U started processing 167 packages
[2024-04-03 18:16:48] INFO - Thread-R finished processing: 469 packages downloaded in 0 hours, 2 minutes, 52.45 seconds.
[2024-04-03 18:16:48] INFO - Thread-V started processing 92 packages
[2024-04-03 18:16:59] INFO - Active threads (8): Thread-U, Thread-K, Thread-Q, Thread-S, Thread-V, Thread-P, Thread-J, Thread-G
[2024-04-03 18:17:29] INFO - Active threads (8): Thread-U, Thread-K, Thread-Q, Thread-S, Thread-V, Thread-P, Thread-J, Thread-G
[2024-04-03 18:17:49] INFO - Thread-U finished processing: 167 packages downloaded in 0 hours, 1 minutes, 0.79 seconds.
[2024-04-03 18:17:49] INFO - Thread-W started processing 104 packages
[2024-04-03 18:17:59] INFO - Thread-S finished processing: 445 packages downloaded in 0 hours, 3 minutes, 39.57 seconds.
[2024-04-03 18:17:59] INFO - Thread-X started processing 181 packages
[2024-04-03 18:17:59] INFO - Active threads (8): Thread-W, Thread-K, Thread-Q, Thread-X, Thread-V, Thread-P, Thread-J, Thread-G
[2024-04-03 18:17:59] INFO - Thread-V finished processing: 92 packages downloaded in 0 hours, 1 minutes, 11.10 seconds.
[2024-04-03 18:17:59] INFO - Thread-Y started processing 31 packages
[2024-04-03 18:18:10] INFO - Thread-Y finished processing: 31 packages downloaded in 0 hours, 0 minutes, 10.82 seconds.
[2024-04-03 18:18:16] INFO - Thread-Q finished processing: 159 packages downloaded in 0 hours, 2 minutes, 5.67 seconds.
[2024-04-03 18:18:17] INFO - Thread-G finished processing: 791 packages downloaded in 0 hours, 6 minutes, 47.14 seconds.
[2024-04-03 18:18:29] INFO - Active threads (8): Thread-W, Thread-K, Thread-Q, Thread-X, Thread-Y, Thread-P, Thread-J, Thread-G
[2024-04-03 18:18:33] INFO - Thread-W finished processing: 104 packages downloaded in 0 hours, 0 minutes, 44.31 seconds.
[2024-04-03 18:18:54] INFO - Thread-K finished processing: 570 packages downloaded in 0 hours, 3 minutes, 0.20 seconds.
[2024-04-03 18:18:59] INFO - Active threads (8): Thread-W, Thread-K, Thread-Q, Thread-X, Thread-Y, Thread-P, Thread-J, Thread-G
[2024-04-03 18:19:00] INFO - Thread-X finished processing: 181 packages downloaded in 0 hours, 1 minutes, 1.29 seconds.
[2024-04-03 18:19:29] INFO - Active threads (8): Thread-W, Thread-K, Thread-Q, Thread-X, Thread-Y, Thread-P, Thread-J, Thread-G
[2024-04-03 18:19:59] INFO - Active threads (8): Thread-W, Thread-K, Thread-Q, Thread-X, Thread-Y, Thread-P, Thread-J, Thread-G
[2024-04-03 18:20:29] INFO - Active threads (8): Thread-W, Thread-K, Thread-Q, Thread-X, Thread-Y, Thread-P, Thread-J, Thread-G
[2024-04-03 18:20:59] INFO - Active threads (8): Thread-W, Thread-K, Thread-Q, Thread-X, Thread-Y, Thread-P, Thread-J, Thread-G
[2024-04-03 18:21:24] INFO - Thread-J finished processing: 101 packages downloaded in 0 hours, 5 minutes, 50.68 seconds.
[2024-04-03 18:21:29] INFO - Active threads (8): Thread-W, Thread-K, Thread-Q, Thread-X, Thread-Y, Thread-P, Thread-J, Thread-G
[2024-04-03 18:21:59] INFO - Active threads (8): Thread-W, Thread-K, Thread-Q, Thread-X, Thread-Y, Thread-P, Thread-J, Thread-G
[2024-04-03 18:22:29] INFO - Active threads (8): Thread-W, Thread-K, Thread-Q, Thread-X, Thread-Y, Thread-P, Thread-J, Thread-G
[2024-04-03 18:22:59] INFO - Active threads (8): Thread-W, Thread-K, Thread-Q, Thread-X, Thread-Y, Thread-P, Thread-J, Thread-G
[2024-04-03 18:23:29] INFO - Active threads (8): Thread-W, Thread-K, Thread-Q, Thread-X, Thread-Y, Thread-P, Thread-J, Thread-G
[2024-04-03 18:23:59] INFO - Active threads (8): Thread-W, Thread-K, Thread-Q, Thread-X, Thread-Y, Thread-P, Thread-J, Thread-G
[2024-04-03 18:24:10] INFO - Thread-P finished processing: 2963 packages downloaded in 0 hours, 10 minutes, 19.65 seconds.
[2024-04-03 18:24:10] INFO - Downloaded repo from https://ftp.uni-stuttgart.de/epel/8/Everything/x86_64/ in 0 hours, 12 minutes, and 41.91 seconds.
[2024-04-03 18:24:10] INFO - Downloaded a total of 9326 files
[2024-04-03 18:24:10] INFO - Total files in the downloaded repo: 10087
[2024-04-03 18:24:10] INFO - Total space used by the repo: 18.72 GB, 19169.66 MB
[2024-04-03 18:24:11] INFO - Processing centos9...
[2024-04-03 18:24:11] INFO - Initialized EPELDownloader for https://ftp.uni-stuttgart.de/epel/9/Everything/x86_64/ with local dir ./epel/9/
[2024-04-03 18:24:11] INFO - Fetching XML from https://ftp.uni-stuttgart.de/epel/9/Everything/x86_64/repodata/repomd.xml
[2024-04-03 18:24:11] INFO - No updates are available for repomd.xml localdate: 1712109437, remotedate: 1712109437
[2024-04-03 18:24:11] INFO - Fetching XML from https://ftp.uni-stuttgart.de/epel/9/Everything/x86_64/repodata/repomd.xml
[2024-04-03 18:24:12] INFO - Thread-3 started processing 1 packages
[2024-04-03 18:24:12] INFO - Thread-6 started processing 1 packages
[2024-04-03 18:24:12] INFO - Thread-A started processing 274 packages
[2024-04-03 18:24:12] INFO - Thread-B started processing 265 packages
[2024-04-03 18:24:12] INFO - Thread-C started processing 500 packages
[2024-04-03 18:24:12] INFO - Thread-D started processing 190 packages
[2024-04-03 18:24:12] INFO - Thread-6 finished processing: 0 packages downloaded in 0 hours, 0 minutes, 0.00 seconds.
[2024-04-03 18:24:12] INFO - Thread-3 finished processing: 0 packages downloaded in 0 hours, 0 minutes, 0.00 seconds.
[2024-04-03 18:24:12] INFO - Thread-F started processing 219 packages
[2024-04-03 18:24:12] INFO - Thread-G started processing 2836 packages
[2024-04-03 18:24:12] INFO - Thread-H started processing 115 packages
[2024-04-03 18:24:12] INFO - Thread-I started processing 124 packages
[2024-04-03 18:24:12] INFO - Thread-I finished processing: 0 packages downloaded in 0 hours, 0 minutes, 0.24 seconds.
[2024-04-03 18:24:12] INFO - Thread-L started processing 1037 packages
[2024-04-03 18:24:12] INFO - Thread-H finished processing: 0 packages downloaded in 0 hours, 0 minutes, 0.27 seconds.
[2024-04-03 18:24:12] INFO - Thread-M started processing 391 packages
[2024-04-03 18:24:12] INFO - Thread-F finished processing: 0 packages downloaded in 0 hours, 0 minutes, 0.42 seconds.
[2024-04-03 18:24:12] INFO - Thread-N started processing 294 packages
[2024-04-03 18:24:12] INFO - Thread-D finished processing: 0 packages downloaded in 0 hours, 0 minutes, 0.56 seconds.
[2024-04-03 18:24:12] INFO - Thread-O started processing 200 packages
[2024-04-03 18:24:13] INFO - Thread-A finished processing: 0 packages downloaded in 0 hours, 0 minutes, 0.96 seconds.
[2024-04-03 18:24:13] INFO - Thread-P started processing 3128 packages
[2024-04-03 18:24:13] INFO - Thread-B finished processing: 0 packages downloaded in 0 hours, 0 minutes, 1.00 seconds.
[2024-04-03 18:24:13] INFO - Thread-R started processing 8860 packages
[2024-04-03 18:24:13] INFO - Thread-N finished processing: 0 packages downloaded in 0 hours, 0 minutes, 0.69 seconds.
[2024-04-03 18:24:13] INFO - Thread-S started processing 433 packages
[2024-04-03 18:24:13] INFO - Thread-O finished processing: 0 packages downloaded in 0 hours, 0 minutes, 0.68 seconds.
[2024-04-03 18:24:13] INFO - Thread-T started processing 251 packages
[2024-04-03 18:24:13] INFO - Thread-C finished processing: 0 packages downloaded in 0 hours, 0 minutes, 1.28 seconds.
[2024-04-03 18:24:13] INFO - Thread-Z started processing 86 packages
[2024-04-03 18:24:13] INFO - Thread-Z finished processing: 0 packages downloaded in 0 hours, 0 minutes, 0.09 seconds.
[2024-04-03 18:24:13] INFO - Thread-E started processing 91 packages
[2024-04-03 18:24:13] INFO - Thread-M finished processing: 0 packages downloaded in 0 hours, 0 minutes, 1.11 seconds.
[2024-04-03 18:24:13] INFO - Thread-J started processing 106 packages
[2024-04-03 18:24:13] INFO - Thread-T finished processing: 0 packages downloaded in 0 hours, 0 minutes, 0.20 seconds.
[2024-04-03 18:24:13] INFO - Thread-K started processing 575 packages
[2024-04-03 18:24:14] INFO - Thread-L finished processing: 0 packages downloaded in 0 hours, 0 minutes, 1.60 seconds.
[2024-04-03 18:24:14] INFO - Thread-Q started processing 263 packages
[2024-04-03 18:24:14] INFO - Thread-S finished processing: 0 packages downloaded in 0 hours, 0 minutes, 0.88 seconds.
[2024-04-03 18:24:14] INFO - Thread-U started processing 158 packages
[2024-04-03 18:24:14] INFO - Thread-E finished processing: 0 packages downloaded in 0 hours, 0 minutes, 0.66 seconds.
[2024-04-03 18:24:14] INFO - Thread-V started processing 112 packages
[2024-04-03 18:24:14] INFO - Thread-U finished processing: 0 packages downloaded in 0 hours, 0 minutes, 0.13 seconds.
[2024-04-03 18:24:14] INFO - Thread-W started processing 101 packages
[2024-04-03 18:24:14] INFO - Thread-K finished processing: 0 packages downloaded in 0 hours, 0 minutes, 0.77 seconds.
[2024-04-03 18:24:14] INFO - Thread-X started processing 182 packages
[2024-04-03 18:24:14] INFO - Thread-Q finished processing: 0 packages downloaded in 0 hours, 0 minutes, 0.49 seconds.
[2024-04-03 18:24:14] INFO - Thread-Y started processing 36 packages
[2024-04-03 18:24:14] INFO - Thread-W finished processing: 0 packages downloaded in 0 hours, 0 minutes, 0.24 seconds.
[2024-04-03 18:24:14] INFO - Thread-Y finished processing: 0 packages downloaded in 0 hours, 0 minutes, 0.06 seconds.
[2024-04-03 18:24:14] INFO - Thread-X finished processing: 0 packages downloaded in 0 hours, 0 minutes, 0.23 seconds.
[2024-04-03 18:24:14] INFO - Thread-V finished processing: 0 packages downloaded in 0 hours, 0 minutes, 0.48 seconds.
[2024-04-03 18:24:15] INFO - Thread-R finished processing: 0 packages downloaded in 0 hours, 0 minutes, 2.35 seconds.
[2024-04-03 18:24:16] INFO - Thread-P finished processing: 0 packages downloaded in 0 hours, 0 minutes, 2.78 seconds.
[2024-04-03 18:24:16] INFO - Thread-G finished processing: 0 packages downloaded in 0 hours, 0 minutes, 4.15 seconds.
[2024-04-03 18:24:18] INFO - Thread-J finished processing: 0 packages downloaded in 0 hours, 0 minutes, 4.65 seconds.
[2024-04-03 18:24:18] INFO - Downloaded repo from https://ftp.uni-stuttgart.de/epel/9/Everything/x86_64/ in 0 hours, 0 minutes, and 7.42 seconds.
[2024-04-03 18:24:18] INFO - Downloaded a total of 0 files
[2024-04-03 18:24:18] INFO - Total files in the downloaded repo: 20841
[2024-04-03 18:24:18] INFO - Total space used by the repo: 17.77 GB, 18197.07 MB
podman run -v /home/badger/code/epel-offline-sync/epelout:/app/epel   0.72s user 0.46s system 0% cpu 12:49.85 total
```

Thats right, downloaded epel8 and validated an already synced epel9 in 12 minutes, 49 seconds. 


Then, re-running immediately we only take 17 seconds to validate all the packages.

Validation is done by this method:

```python
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
```

Which compares the `package.xml` checksum for the given package, and the actual sha256sum of that file.

```
time podman run -v /home/badger/code/epel-offline-sync/epelout:/app/epel localhost/test/epeldownloader:0.2
[2024-04-03 18:37:23] INFO - Initialized EPELDownloader for https://ftp.uni-stuttgart.de/epel/8/Everything/x86_64/ with local dir ./epel/8/
[2024-04-03 18:37:23] INFO - Fetching XML from https://ftp.uni-stuttgart.de/epel/8/Everything/x86_64/repodata/repomd.xml
[2024-04-03 18:37:23] INFO - No updates are available for repomd.xml localdate: 1712110674, remotedate: 1712110674
[2024-04-03 18:37:23] INFO - Fetching XML from https://ftp.uni-stuttgart.de/epel/8/Everything/x86_64/repodata/repomd.xml
[2024-04-03 18:37:24] INFO - Thread-3 started processing 1 packages
[2024-04-03 18:37:24] INFO - Thread-6 started processing 1 packages
[2024-04-03 18:37:24] INFO - Thread-A started processing 261 packages
[2024-04-03 18:37:24] INFO - Thread-B started processing 319 packages
[2024-04-03 18:37:24] INFO - Thread-C started processing 390 packages
[2024-04-03 18:37:24] INFO - Thread-D started processing 221 packages
[2024-04-03 18:37:24] INFO - Thread-F started processing 265 packages
[2024-04-03 18:37:24] INFO - Thread-6 finished processing: 0 packages downloaded in 0 hours, 0 minutes, 0.00 seconds.
[2024-04-03 18:37:24] INFO - Thread-3 finished processing: 0 packages downloaded in 0 hours, 0 minutes, 0.00 seconds.
[2024-04-03 18:37:24] INFO - Thread-G started processing 834 packages
[2024-04-03 18:37:24] INFO - Thread-H started processing 104 packages
[2024-04-03 18:37:24] INFO - Thread-I started processing 119 packages
[2024-04-03 18:37:24] INFO - Thread-I finished processing: 0 packages downloaded in 0 hours, 0 minutes, 0.21 seconds.
[2024-04-03 18:37:24] INFO - Thread-L started processing 896 packages
[2024-04-03 18:37:24] INFO - Thread-H finished processing: 0 packages downloaded in 0 hours, 0 minutes, 0.23 seconds.
[2024-04-03 18:37:24] INFO - Thread-M started processing 323 packages
[2024-04-03 18:37:24] INFO - Thread-D finished processing: 0 packages downloaded in 0 hours, 0 minutes, 0.86 seconds.
[2024-04-03 18:37:24] INFO - Thread-N started processing 291 packages
[2024-04-03 18:37:25] INFO - Thread-B finished processing: 0 packages downloaded in 0 hours, 0 minutes, 1.28 seconds.
[2024-04-03 18:37:25] INFO - Thread-O started processing 185 packages
[2024-04-03 18:37:25] INFO - Thread-N finished processing: 0 packages downloaded in 0 hours, 0 minutes, 0.78 seconds.
[2024-04-03 18:37:25] INFO - Thread-P started processing 2963 packages
[2024-04-03 18:37:25] INFO - Thread-C finished processing: 0 packages downloaded in 0 hours, 0 minutes, 1.76 seconds.
[2024-04-03 18:37:25] INFO - Thread-R started processing 469 packages
[2024-04-03 18:37:25] INFO - Thread-A finished processing: 0 packages downloaded in 0 hours, 0 minutes, 1.92 seconds.
[2024-04-03 18:37:25] INFO - Thread-S started processing 445 packages
[2024-04-03 18:37:26] INFO - Thread-O finished processing: 0 packages downloaded in 0 hours, 0 minutes, 0.76 seconds.
[2024-04-03 18:37:26] INFO - Thread-T started processing 356 packages
[2024-04-03 18:37:26] INFO - Thread-M finished processing: 0 packages downloaded in 0 hours, 0 minutes, 2.03 seconds.
[2024-04-03 18:37:26] INFO - Thread-Z started processing 90 packages
[2024-04-03 18:37:26] INFO - Thread-F finished processing: 0 packages downloaded in 0 hours, 0 minutes, 2.51 seconds.
[2024-04-03 18:37:26] INFO - Thread-E started processing 137 packages
[2024-04-03 18:37:26] INFO - Thread-Z finished processing: 0 packages downloaded in 0 hours, 0 minutes, 0.26 seconds.
[2024-04-03 18:37:26] INFO - Thread-J started processing 101 packages
[2024-04-03 18:37:26] INFO - Thread-E finished processing: 0 packages downloaded in 0 hours, 0 minutes, 0.33 seconds.
[2024-04-03 18:37:26] INFO - Thread-K started processing 570 packages
[2024-04-03 18:37:26] INFO - Thread-L finished processing: 0 packages downloaded in 0 hours, 0 minutes, 2.71 seconds.
[2024-04-03 18:37:26] INFO - Thread-Q started processing 159 packages
[2024-04-03 18:37:27] INFO - Thread-R finished processing: 0 packages downloaded in 0 hours, 0 minutes, 1.49 seconds.
[2024-04-03 18:37:27] INFO - Thread-U started processing 167 packages
[2024-04-03 18:37:27] INFO - Thread-T finished processing: 0 packages downloaded in 0 hours, 0 minutes, 1.24 seconds.
[2024-04-03 18:37:27] INFO - Thread-V started processing 92 packages
[2024-04-03 18:37:27] INFO - Thread-U finished processing: 0 packages downloaded in 0 hours, 0 minutes, 0.59 seconds.
[2024-04-03 18:37:27] INFO - Thread-W started processing 104 packages
[2024-04-03 18:37:28] INFO - Thread-V finished processing: 0 packages downloaded in 0 hours, 0 minutes, 0.71 seconds.
[2024-04-03 18:37:28] INFO - Thread-X started processing 181 packages
[2024-04-03 18:37:28] INFO - Thread-S finished processing: 0 packages downloaded in 0 hours, 0 minutes, 2.17 seconds.
[2024-04-03 18:37:28] INFO - Thread-Y started processing 31 packages
[2024-04-03 18:37:28] INFO - Thread-Y finished processing: 0 packages downloaded in 0 hours, 0 minutes, 0.11 seconds.
[2024-04-03 18:37:28] INFO - Thread-W finished processing: 0 packages downloaded in 0 hours, 0 minutes, 0.41 seconds.
[2024-04-03 18:37:28] INFO - Thread-Q finished processing: 0 packages downloaded in 0 hours, 0 minutes, 1.39 seconds.
[2024-04-03 18:37:28] INFO - Thread-K finished processing: 0 packages downloaded in 0 hours, 0 minutes, 1.60 seconds.
[2024-04-03 18:37:28] INFO - Thread-G finished processing: 0 packages downloaded in 0 hours, 0 minutes, 4.51 seconds.
[2024-04-03 18:37:28] INFO - Thread-X finished processing: 0 packages downloaded in 0 hours, 0 minutes, 0.54 seconds.
[2024-04-03 18:37:31] INFO - Thread-P finished processing: 0 packages downloaded in 0 hours, 0 minutes, 5.29 seconds.
[2024-04-03 18:37:32] INFO - Thread-J finished processing: 0 packages downloaded in 0 hours, 0 minutes, 5.89 seconds.
[2024-04-03 18:37:32] INFO - Downloaded repo from https://ftp.uni-stuttgart.de/epel/8/Everything/x86_64/ in 0 hours, 0 minutes, and 9.28 seconds.
[2024-04-03 18:37:32] INFO - Downloaded a total of 0 files
[2024-04-03 18:37:32] INFO - Total files in the downloaded repo: 10087
[2024-04-03 18:37:32] INFO - Total space used by the repo: 18.72 GB
[2024-04-03 18:37:32] INFO - Processing centos9...
[2024-04-03 18:37:32] INFO - Initialized EPELDownloader for https://ftp.uni-stuttgart.de/epel/9/Everything/x86_64/ with local dir ./epel/9/
[2024-04-03 18:37:32] INFO - Fetching XML from https://ftp.uni-stuttgart.de/epel/9/Everything/x86_64/repodata/repomd.xml
[2024-04-03 18:37:32] INFO - No updates are available for repomd.xml localdate: 1712109437, remotedate: 1712109437
[2024-04-03 18:37:32] INFO - Fetching XML from https://ftp.uni-stuttgart.de/epel/9/Everything/x86_64/repodata/repomd.xml
[2024-04-03 18:37:33] INFO - Thread-3 started processing 1 packages
[2024-04-03 18:37:33] INFO - Thread-6 started processing 1 packages
[2024-04-03 18:37:33] INFO - Thread-A started processing 274 packages
[2024-04-03 18:37:33] INFO - Thread-B started processing 265 packages
[2024-04-03 18:37:33] INFO - Thread-C started processing 500 packages
[2024-04-03 18:37:33] INFO - Thread-D started processing 190 packages
[2024-04-03 18:37:33] INFO - Thread-F started processing 219 packages
[2024-04-03 18:37:33] INFO - Thread-G started processing 2836 packages
[2024-04-03 18:37:33] INFO - Thread-6 finished processing: 0 packages downloaded in 0 hours, 0 minutes, 0.00 seconds.
[2024-04-03 18:37:33] INFO - Thread-H started processing 115 packages
[2024-04-03 18:37:33] INFO - Thread-3 finished processing: 0 packages downloaded in 0 hours, 0 minutes, 0.00 seconds.
[2024-04-03 18:37:33] INFO - Thread-I started processing 124 packages
[2024-04-03 18:37:34] INFO - Thread-H finished processing: 0 packages downloaded in 0 hours, 0 minutes, 0.25 seconds.
[2024-04-03 18:37:34] INFO - Thread-L started processing 1037 packages
[2024-04-03 18:37:34] INFO - Thread-I finished processing: 0 packages downloaded in 0 hours, 0 minutes, 0.33 seconds.
[2024-04-03 18:37:34] INFO - Thread-M started processing 391 packages
[2024-04-03 18:37:34] INFO - Thread-F finished processing: 0 packages downloaded in 0 hours, 0 minutes, 0.45 seconds.
[2024-04-03 18:37:34] INFO - Thread-N started processing 294 packages
[2024-04-03 18:37:34] INFO - Thread-D finished processing: 0 packages downloaded in 0 hours, 0 minutes, 0.52 seconds.
[2024-04-03 18:37:34] INFO - Thread-O started processing 200 packages
[2024-04-03 18:37:34] INFO - Thread-N finished processing: 0 packages downloaded in 0 hours, 0 minutes, 0.24 seconds.
[2024-04-03 18:37:34] INFO - Thread-P started processing 3128 packages
[2024-04-03 18:37:34] INFO - Thread-A finished processing: 0 packages downloaded in 0 hours, 0 minutes, 0.85 seconds.
[2024-04-03 18:37:34] INFO - Thread-R started processing 8860 packages
[2024-04-03 18:37:34] INFO - Thread-B finished processing: 0 packages downloaded in 0 hours, 0 minutes, 0.90 seconds.
[2024-04-03 18:37:34] INFO - Thread-S started processing 433 packages
[2024-04-03 18:37:34] INFO - Thread-O finished processing: 0 packages downloaded in 0 hours, 0 minutes, 0.41 seconds.
[2024-04-03 18:37:34] INFO - Thread-T started processing 251 packages
[2024-04-03 18:37:35] INFO - Thread-M finished processing: 0 packages downloaded in 0 hours, 0 minutes, 0.79 seconds.
[2024-04-03 18:37:35] INFO - Thread-Z started processing 86 packages
[2024-04-03 18:37:35] INFO - Thread-Z finished processing: 0 packages downloaded in 0 hours, 0 minutes, 0.22 seconds.
[2024-04-03 18:37:35] INFO - Thread-E started processing 91 packages
[2024-04-03 18:37:35] INFO - Thread-T finished processing: 0 packages downloaded in 0 hours, 0 minutes, 0.42 seconds.
[2024-04-03 18:37:35] INFO - Thread-J started processing 106 packages
[2024-04-03 18:37:35] INFO - Thread-C finished processing: 0 packages downloaded in 0 hours, 0 minutes, 1.39 seconds.
[2024-04-03 18:37:35] INFO - Thread-K started processing 575 packages
[2024-04-03 18:37:35] INFO - Thread-L finished processing: 0 packages downloaded in 0 hours, 0 minutes, 1.58 seconds.
[2024-04-03 18:37:35] INFO - Thread-Q started processing 263 packages
[2024-04-03 18:37:35] INFO - Thread-S finished processing: 0 packages downloaded in 0 hours, 0 minutes, 1.14 seconds.
[2024-04-03 18:37:35] INFO - Thread-U started processing 158 packages
[2024-04-03 18:37:35] INFO - Thread-E finished processing: 0 packages downloaded in 0 hours, 0 minutes, 0.70 seconds.
[2024-04-03 18:37:35] INFO - Thread-V started processing 112 packages
[2024-04-03 18:37:36] INFO - Thread-K finished processing: 0 packages downloaded in 0 hours, 0 minutes, 0.78 seconds.
[2024-04-03 18:37:36] INFO - Thread-W started processing 101 packages
[2024-04-03 18:37:36] INFO - Thread-U finished processing: 0 packages downloaded in 0 hours, 0 minutes, 0.15 seconds.
[2024-04-03 18:37:36] INFO - Thread-X started processing 182 packages
[2024-04-03 18:37:36] INFO - Thread-Q finished processing: 0 packages downloaded in 0 hours, 0 minutes, 0.47 seconds.
[2024-04-03 18:37:36] INFO - Thread-Y started processing 36 packages
[2024-04-03 18:37:36] INFO - Thread-Y finished processing: 0 packages downloaded in 0 hours, 0 minutes, 0.05 seconds.
[2024-04-03 18:37:36] INFO - Thread-W finished processing: 0 packages downloaded in 0 hours, 0 minutes, 0.26 seconds.
[2024-04-03 18:37:36] INFO - Thread-X finished processing: 0 packages downloaded in 0 hours, 0 minutes, 0.27 seconds.
[2024-04-03 18:37:36] INFO - Thread-V finished processing: 0 packages downloaded in 0 hours, 0 minutes, 0.51 seconds.
[2024-04-03 18:37:37] INFO - Thread-R finished processing: 0 packages downloaded in 0 hours, 0 minutes, 2.68 seconds.
[2024-04-03 18:37:37] INFO - Thread-P finished processing: 0 packages downloaded in 0 hours, 0 minutes, 3.34 seconds.
[2024-04-03 18:37:38] INFO - Thread-G finished processing: 0 packages downloaded in 0 hours, 0 minutes, 4.19 seconds.
[2024-04-03 18:37:40] INFO - Thread-J finished processing: 0 packages downloaded in 0 hours, 0 minutes, 4.81 seconds.
[2024-04-03 18:37:40] INFO - Downloaded repo from https://ftp.uni-stuttgart.de/epel/9/Everything/x86_64/ in 0 hours, 0 minutes, and 7.55 seconds.
[2024-04-03 18:37:40] INFO - Downloaded a total of 0 files
[2024-04-03 18:37:40] INFO - Total files in the downloaded repo: 20841
[2024-04-03 18:37:40] INFO - Total space used by the repo: 17.77 GB
podman run -v /home/badger/code/epel-offline-sync/epelout:/app/epel   0.12s user 0.08s system 1% cpu 17.325 total
```