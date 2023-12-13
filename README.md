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

I run this in a weekly cron job, and for the last couple month's it's done what I expected.
