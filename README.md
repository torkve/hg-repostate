hg-repostate
============

This is an extension inspired by the [hg-prompt][hg-prompt extension].
It adds 'hg repostate' command which outputs current bookmarks or branch and returns dirty flag as exitcode.

Installing
----------

Add to the '[extensions]' section in your hgrc:

    [extensions]
    repostate = /path/to/hg-repostate/repostate.py

Documentation
-------------

Command should return space-separated list of bookmarks and/or branch name.
If the repository appears to be clean, the exitcode should be 0. Otherwise it will be set to 1.
If the hg repository is not found, mercurial returns exitcode 255, keep it in mind.

Links
-----

[hg-prompt]: https://bitbucket.org/sjl/hg-prompt/
