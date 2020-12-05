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
    client_main(rhost=os.environ['rhost'],rport=int(os.environ['rport']))
