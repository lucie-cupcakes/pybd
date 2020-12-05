"""Copyright (C) 2020 Lucie Cupcakes <lucie_linux [at] protonmail.com>

This file is part of pybd <https://gitlab.com/lucie_cupcakes/pybd>.
GCC is free software; you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free
Software Foundation; either version 3, or (at your option) any later
version.
GCC is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
for more details.
You should have received a copy of the GNU General Public License
along with GCC; see the file LICENSE.  If not see
<http://www.gnu.org/licenses/>."""

from bash_run import bash_run
from spawn_daemon import spawn_daemon

def internal_cmd_spawn(args):
    bash_run(cmd=args['cmd'],cwd=args['cwd'],env=args['env'])

def process_spawn_cmd(cmd,cwd,env):
    rc=0
    res=''
    if len(cmd)>=2:
        args={}
        args['cmd']=' '.join(cmd[1:])
        args['cwd']=cwd
        args['env']=env
        spawn_daemon(internal_cmd_spawn,args)
        res='Daemon started.'
    else:
        rc=1
        res='spawn: Invalid number of arguments.'
    return rc,res,cwd,env
