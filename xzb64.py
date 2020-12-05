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
