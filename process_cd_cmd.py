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

import os

def process_cd_cmd(cmd,cwd,env):
    res=''
    rc=0
    if len(cmd)>=2:
        path=cmd[1]
        if path.find('@') == -1:
            if path=='..':
                path='@/..'
            elif not path.startswith('/'):
                path='@/{}'.format(path)
        path=path.replace('@', cwd)
        if os.path.exists(path) and os.path.isdir(path):
            cwd=os.path.realpath(path)
            res='OK'
        else:
            rc=1
            res='cd: {}: does not exists or is not a directory.'.format(path)
    else:
        rc,res,cwd,env=process_cd_cmd(['cd', env['HOME']], cwd, env)
    return rc,res,cwd,env
