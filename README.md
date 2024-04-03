# epel-offline-sync

#### Why does this repo exist?

I needed to mirror an EPEL repo to a disconnected environment, and did not have some of the 'usual' tooling available, such as [reposync](https://linux.die.net/man/1/reposync)

I also had to only use stdlib, and only had access to python 3.9

If this is useful for you, awesome. I may extend it in the future to add some other arbitrary download mechanisms.


#### What does it do?

Given an upstream EPEL repo in the `config.ini` file, we download the  `repomd.xml` and `primary.xml` files, and use ElementTree to identify what packages to download.
Using this method, we're able to easily have a deduplication mechanism built in, it won't re-download packages that haven't changed from the last run.

NOTE: this currently won't remove packages that are removed from upstream.

On subsequent runs, this will pull down the latest `repomd.xml` file and use hashlib to compare the file hashes in the download directory with the `common:checksum` specified in the XML.
While this can be resource intensive on a low-power machine, the server I'm running this on (8 core Xeon 6244) barely notices.

I run this in a weekly cron job, and this script has worked quite nicely for several months now.

#### Example log output:

```bash
INFO:root:Initialized EPELDownloader for https://<upstream_epel_server>/epel/8/Everything/x86_64/ with local dir ./epel/8/
INFO:root:Fetching XML from https://<upstream_epel_server>/epel/8/Everything/x86_64/repodata/repomd.xml
INFO:root:No updates are available for repomd.xml localdate: 1712110674, remotedate: 1712110674
INFO:root:Fetching XML from https://<upstream_epel_server>/epel/8/Everything/x86_64/repodata/repomd.xml
INFO:root:Thread-3 started processing 1 packages
INFO:root:Thread-6 started processing 1 packages
INFO:root:Thread-A started processing 261 packages
INFO:root:Thread-B started processing 319 packages
INFO:root:Thread-C started processing 390 packages
INFO:root:Thread-D started processing 221 packages
INFO:root:Thread-F started processing 265 packages
INFO:root:Thread-G started processing 834 packages
INFO:root:Thread-6 finished processing packages in 0.21 seconds, downloaded 1 packages
INFO:root:Thread-H started processing 104 packages
INFO:root:Thread-3 finished processing packages in 0.26 seconds, downloaded 1 packages
INFO:root:Thread-I started processing 119 packages
INFO:root:Thread-I finished processing packages in 26.61 seconds, downloaded 119 packages
INFO:root:Thread-L started processing 896 packages
INFO:root:Active threads (9): Thread-Monitor, Thread-L, Thread-H, Thread-A, Thread-B, Thread-C, Thread-D, Thread-F, Thread-G
INFO:root:Thread-H finished processing packages in 29.88 seconds, downloaded 104 packages
INFO:root:Thread-M started processing 323 packages
INFO:root:Active threads (9): Thread-Monitor, Thread-L, Thread-M, Thread-A, Thread-B, Thread-C, Thread-D, Thread-F, Thread-G
INFO:root:Thread-D finished processing packages in 82.92 seconds, downloaded 221 packages
INFO:root:Thread-N started processing 291 packages
INFO:root:Active threads (9): Thread-Monitor, Thread-L, Thread-M, Thread-A, Thread-B, Thread-C, Thread-N, Thread-F, Thread-G
INFO:root:Active threads (9): Thread-Monitor, Thread-L, Thread-M, Thread-A, Thread-B, Thread-C, Thread-N, Thread-F, Thread-G
INFO:root:Thread-B finished processing packages in 131.59 seconds, downloaded 319 packages
INFO:root:Thread-O started processing 185 packages
INFO:root:Active threads (9): Thread-Monitor, Thread-L, Thread-M, Thread-A, Thread-O, Thread-C, Thread-N, Thread-F, Thread-G
INFO:root:Thread-N finished processing packages in 91.67 seconds, downloaded 291 packages
INFO:root:Thread-P started processing 2963 packages
INFO:root:Active threads (9): Thread-Monitor, Thread-L, Thread-M, Thread-A, Thread-O, Thread-C, Thread-P, Thread-F, Thread-G
INFO:root:Thread-C finished processing packages in 186.85 seconds, downloaded 390 packages
INFO:root:Thread-R started processing 469 packages
INFO:root:Thread-A finished processing packages in 191.08 seconds, downloaded 261 packages
INFO:root:Thread-S started processing 445 packages
INFO:root:Active threads (9): Thread-Monitor, Thread-L, Thread-M, Thread-S, Thread-O, Thread-R, Thread-P, Thread-F, Thread-G
INFO:root:Thread-O finished processing packages in 79.71 seconds, downloaded 185 packages
INFO:root:Thread-T started processing 356 packages
```

#### BUILDING

Using the provided [Dockerfile](./Dockerfile) you can build a container to run this:

```bash
 podman build -t example/epeldownloader:0.1 .
STEP 1/4: FROM registry.access.redhat.com/ubi9/python-39@sha256:195c51368e83a798b6f79c6a5d877685fdf5297a81e5211cfca747a7fca725aa
STEP 2/4: COPY . /app
--> b35199ee2e0e
STEP 3/4: WORKDIR /app
--> c7574b630e24
STEP 4/4: CMD ["python", "main.py"]
COMMIT example/epeldownloader:0.1
--> 6c9704b14fa4
Successfully tagged localhost/example/epeldownloader:0.1
```

Then, run it:

```bash
podman run -v /path/to/desired/epel:/app/epel localhost/example/epeldownloader:0.1
INFO:root:Initialized EPELDownloader for https://<upstream_epel_server>/epel/8/Everything/x86_64/ with local dir ./epel/8/
INFO:root:Fetching XML from https://<upstream_epel_server>/epel/8/Everything/x86_64/repodata/repomd.xml
INFO:root:No updates are available for repomd.xml localdate: 1712110674, remotedate: 1712110674
INFO:root:Fetching XML from https://<upstream_epel_server>/epel/8/Everything/x86_64/repodata/repomd.xml
INFO:root:Thread-3 started processing 1 packages
INFO:root:Thread-6 started processing 1 packages
INFO:root:Thread-A started processing 261 packages
INFO:root:Thread-B started processing 319 packages
INFO:root:Thread-C started processing 390 packages
INFO:root:Thread-D started processing 221 packages
INFO:root:Thread-F started processing 265 packages
INFO:root:Thread-G started processing 834 packages
INFO:root:Thread-6 finished processing packages in 0.21 seconds, downloaded 1 packages
INFO:root:Thread-H started processing 104 packages
INFO:root:Thread-3 finished processing packages in 0.26 seconds, downloaded 1 packages
INFO:root:Thread-I started processing 119 packages
INFO:root:Thread-I finished processing packages in 26.61 seconds, downloaded 119 packages
INFO:root:Thread-L started processing 896 packages
INFO:root:Active threads (9): Thread-Monitor, Thread-L, Thread-H, Thread-A, Thread-B, Thread-C, Thread-D, Thread-F, Thread-G
INFO:root:Thread-H finished processing packages in 29.88 seconds, downloaded 104 packages
INFO:root:Thread-M started processing 323 packages
INFO:root:Active threads (9): Thread-Monitor, Thread-L, Thread-M, Thread-A, Thread-B, Thread-C, Thread-D, Thread-F, Thread-G
INFO:root:Thread-D finished processing packages in 82.92 seconds, downloaded 221 packages
INFO:root:Thread-N started processing 291 packages
INFO:root:Active threads (9): Thread-Monitor, Thread-L, Thread-M, Thread-A, Thread-B, Thread-C, Thread-N, Thread-F, Thread-G
INFO:root:Active threads (9): Thread-Monitor, Thread-L, Thread-M, Thread-A, Thread-B, Thread-C, Thread-N, Thread-F, Thread-G
INFO:root:Thread-B finished processing packages in 131.59 seconds, downloaded 319 packages
INFO:root:Thread-O started processing 185 packages
```