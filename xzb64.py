import subprocess

def xzb64_encode(str_in):
    if str_in is None or str_in == '':
        return ''
    xz_header='/Td6WFoAAATm1rRGAgAhARwAAAAQz1jM'
    cmd='xz -z -e -9 -c | base64'
    p=subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    o_arr=p.communicate(input=str_in.encode())
    res=''
    for i in o_arr:
        if i is not None:
            res+=i.decode().strip()
    return res.replace('\n','')[len(xz_header):]

def xzb64_decode(str_in):
    if str_in is None or str_in == '':
        return ''
    xz_header='/Td6WFoAAATm1rRGAgAhARwAAAAQz1jM'
    str_in=xz_header+str_in
    cmd='base64 -d | xz -k -d -c'
    p=subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    o_arr=p.communicate(input=str_in.encode())
    res=''
    for i in o_arr:
        if i is not None:
            res+=i.decode()
    return res
