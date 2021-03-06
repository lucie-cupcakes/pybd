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

import os,socket
from _thread import *
import threading
from xzb64 import xzb64_encode, xzb64_decode
from process_cmd import process_cmd

def handle_client(cli,addr,tlock,buffsize,encoding='utf-8'):
    tlock.acquire()
    print(f'{addr[0]}:{addr[1]} connected.')
    tlock.release()
    process_input=True
    cli.settimeout(1800) # 30 minutes
    rc=-1
    cwd=os.getcwd()
    env=os.environ.copy()
    try:
        while process_input:
            res=''
            msg_enc=cli.recv(buffsize).decode(encoding).strip()
            cmd=xzb64_decode(msg_enc).split(' ')
            if cmd[0].lower()=='exit':
                res='Goodbye :)'
                process_input=False
            else:
                tlock.acquire()
                rc,res,cwd,env=process_cmd(cmd,cwd,env)
                tlock.release()
            res=xzb64_encode(res)
            cli.send(f"{rc}%{res}%{cwd}".encode(encoding))
    except socket.timeout as e:
        tlock.acquire()
        print(f"{addr[0]}:{addr[1]} timed out.")
        tlock.release()
    finally:
        cli.close()
        tlock.acquire()
        print(f"{addr[0]}:{addr[1]} disconnected.")
        tlock.release()
