"""Copyright (C) 2020 Lucie Cupcakes <lucie_linux [at] protonmail.com>
This file is part of pybd <https://gitlab.com/lucie_cupcakes/pybd>.
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

def process_env_cmd(cmd,cwd,env):
    res=''
    rc=0
    if len(cmd)==2 and cmd[1].lower()=='help': # ['env','help']
        res='Usage:\nenv list #get key list\n'
        res='Usage:\nenv dump #get all keys and values\n'
        res+='env set key value #set key value\n'
        res+='env get key #get value from key\n'
    elif len(cmd)==2 and cmd[1].lower()=='list': # ['env','list']
        for k in env.keys():
            res+='{}\n'.format(k)
    elif len(cmd)==2 and cmd[1].lower()=='dump': # ['env','list']
        for k,v in env.items():
            res+='{}={}\n'.format(k,v)
    elif len(cmd)>=4 and cmd[1].lower()=='set': # ['env','set','key','value']
        res='OK.'
        k=cmd[2]
        v=' '.join(e[3:])
        env[k]=v
    elif len(cmd)==3 and cmd[1].lower()=='get': # ['env','get','key']
        k=cmd[2]
        res=env[k]
    else:
        rc=1
        res='env: Missing argument or unrecognized commnad.\nuse env help, for usage.'
    return rc,res,cwd,env
