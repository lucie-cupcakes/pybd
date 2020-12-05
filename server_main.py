import sys, os, socket
from _thread import *
import threading
from handle_client import handle_client

def server_main():
    tlock=threading.Lock()
    srv=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv_host=os.environ['host']
    srv_port=int(os.environ['port'])
    srv_max_cli=128
    main_loop_going=True
    srv.bind( (srv_host, srv_port) )
    srv.listen(srv_max_cli)
    print(f"Listening as {srv_host}:{srv_port} ...")
    while main_loop_going:
        try:
            cli,addr=srv.accept()
            start_new_thread(handle_client, (cli, addr, tlock))
        except KeyboardInterrupt:
            print("Leaving..")
            main_loop_going=False
        except Exception as e:
            main_loop_going=False
            print("pybd err: {}".format(repr(e)))
    srv.close()
    exit()
