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
from _thread import *
import threading
from handle_client import handle_client
def server_main(host='0.0.0.0',port=6969,max_cli=128,buffsize=4096,encoding='utf-8'):
    main_loop_going=True
    srv=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tlock=threading.Lock()
    srv.bind( (host, port) )
    srv.listen(max_cli)
    print(f'Listening as {host}:{port} ...')
    while main_loop_going:
        try:
            cli,addr=srv.accept()
            start_new_thread(handle_client, (cli,addr,tlock,buffsize,encoding))
        except KeyboardInterrupt:
            print('Leaving..')
            main_loop_going=False
            srv.close()
        except Exception as e:
            main_loop_going=False
            print('pybd err: {}'.format(repr(e)))
            srv.close()
    srv.close()
