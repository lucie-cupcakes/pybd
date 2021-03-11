"""Copyright (C) 2021 Lucie Cupcakes <lucie_linux [at] protonmail.com>
This file is part of pybd <https://github.com/lucie-cupcakes/pybd>.
pybd is free software; you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free
Software Foundation; either version 3, or (at your option) any later
version.
pybd is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
for more details.
You should have received a copy of the GNU General Public License
along with pybd; see the file LICENSE.  If not see <http://www.gnu.org/licenses/>."""

from random import randint
from bash_run import bash_run
from process_cd_cmd import process_cd_cmd
from process_env_cmd import process_env_cmd
from process_spawn_cmd import process_spawn_cmd

def process_cmd(cmd,cwd,env):
    rc=-1
    res=''
    if cmd[0]=='sv_ping':
        rc=0
        res='Pong!'
    elif cmd[0]=='sv_greet':
        rc=0
        if randint(0,1)==0:
            res='Welcome :)'
        else:
            res='Greetings!'
    elif cmd[0]=='cd':
        rc,res,cwd,env=process_cd_cmd(cmd,cwd,env)
    elif cmd[0]=='env':
        rc,res,cwd,env=process_env_cmd(cmd,cwd,env)
    elif cmd[0]=='spawn':
        rc,res,cwd,env=process_spawn_cmd(cmd,cwd,env)
    else:
        rc,res=bash_run(cmd=' '.join(cmd),cwd=cwd,env=env)
    return rc,res,cwd,env
