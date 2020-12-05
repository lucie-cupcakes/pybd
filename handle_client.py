import os,socket
from _thread import *
import threading
from xzb64 import xzb64_encode, xzb64_decode
from process_cmd import process_cmd

def handle_client(cli,addr,tlock):
    tlock.acquire()
    print(f'{addr[0]}:{addr[1]} connected.')
    tlock.release()
    buff_size=1024
    process_input=True
    cli.settimeout(1800) # 30 minutes
    rc=-1
    cwd=os.getcwd()
    env=os.environ.copy()
    try:
        while process_input:
            res=''
            msg_enc=cli.recv(buff_size).decode('utf-8').strip()
            cmd=xzb64_decode(msg_enc).split(' ')
            if cmd[0].lower()=='exit':
                res='Goodbye :)'
                process_input=False
            else:
                tlock.acquire()
                rc,res,cwd,env=process_cmd(cmd,cwd,env)
                tlock.release()
            res=xzb64_encode(res)
            cli.send(f"{rc}%{res}%{cwd}".encode('utf-8'))
    except socket.timeout as e:
        tlock.acquire()
        print(f"{addr[0]}:{addr[1]} timed out.")
        tlock.release()
    finally:
        cli.close()
        tlock.acquire()
        print(f"{addr[0]}:{addr[1]} disconnected.")
        tlock.release()
