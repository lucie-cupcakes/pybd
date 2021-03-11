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

import sys,os,subprocess,uuid

def bash_run(cmd,cwd,env):
    fpath='/tmp/bashrun_{}.sh'.format(str(uuid.uuid4()))
    fh=open(fpath, 'w+')
    fh.write('#!/bin/bash\n{}\n'.format(cmd))
    fh.close()
    p=subprocess.Popen(['/bin/bash', fpath], shell=False, cwd=cwd, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    rc=p.wait()
    os.remove(fpath)
    res=p.stdout.read().decode()
    return rc,res
