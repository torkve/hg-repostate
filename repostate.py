# Written at 2018 Vsevolod Velichko
# This extension is in public domain.
# Feel free to use it as you wish and keep in mind that in my country code is not covered by patents.

from __future__ import absolute_import

from mercurial import registrar


cmdtable = {}
command = registrar.command(cmdtable)

testedwith = '4.6.1'


@command('repostate', [], 'hg repostate', inferrepo=True)
def repostate(ui, repo, *args, **kwags):
    '''display current bookmarks and branch for the repo as long as
    '''
    reslist = []
    bmks = []
    ctx = repo[None]
    for p in ctx.parents():
        b = p.bookmarks()
        if b:
            bmks.extend(b)
    branch = ctx.branch()
    active = repo._activebookmark

    if bmks:
        for bmk in bmks:
            if bmk == active and active is not None:
                reslist.append('*' + bmk)
            else:
                reslist.append(bmk)

    if branch:
        reslist.append(branch)

    print(' '.join(reslist))

    status = repo.status(unknown=True)
    dirty = bool(
        status.modified
        or status.unknown
        or status.added
        or status.removed
        or any(ctx.sub(s).dirty() for s in ctx.substate)
    )
    raise SystemExit(int(dirty))
