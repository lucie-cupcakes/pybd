import sys, os, socket
from _thread import *
import threading
from handle_client import handle_client
def server_main(host='0.0.0.0',port=6969,max_cli=128):
    main_loop_going=True
    srv=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tlock=threading.Lock()
    srv.bind( (host, port) )
    srv.listen(max_cli)
    print(f'Listening as {host}:{port} ...')
    while main_loop_going:
        try:
            cli,addr=srv.accept()
            start_new_thread(handle_client, (cli, addr, tlock))
        except KeyboardInterrupt:
            print('Leaving..')
            main_loop_going=False
            srv.close()
        except Exception as e:
            main_loop_going=False
            print('pybd err: {}'.format(repr(e)))
            srv.close()
    srv.close()
