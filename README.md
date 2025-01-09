Copr repository for git builds of piper and ratbagd, commits are fetched every hour.

The packages in this repo should work on Fedora 40+.



## Installation 

Activate the repo with `sudo dnf copr enable jackgreiner/piper-git` and then run `sudo dnf update --refresh`.

To revert this, remove the copr repository with `sudo dnf copr remove jackgreiner/piper-git` and then run `sudo dnf distro-sync` to download your distro's version of the piper and libratbagd packages.


## Issues

Feel free to open issues when there are build issues I haven't fixed for a few days: https://github.com/ProjectSynchro/copr-piper-git/issues

If you'd like me to attempt to package this for other RPM based distros like SUSE, open an issue and I'll see what I can do :)
