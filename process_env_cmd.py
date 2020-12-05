def process_env_cmd(cmd,cwd,env):
    res=''
    rc=0
    if len(cmd)==2 and cmd[1].lower()=='help': # ['env','help']
        res='Usage:\nenv list #get key list\n'
        res='Usage:\nenv dump #get all keys and values\n'
        res+='env set key value #set key value\n'
        res+='env get key #get value from key\n'
    elif len(cmd)==2 and cmd[1].lower()=='list': # ['env','list']
        for k in env.keys():
            res+='{}\n'.format(k)
    elif len(cmd)==2 and cmd[1].lower()=='dump': # ['env','list']
        for k,v in env.items():
            res+='{}={}\n'.format(k,v)
    elif len(cmd)>=4 and cmd[1].lower()=='set': # ['env','set','key','value']
        res='OK.'
        k=cmd[2]
        v=' '.join(e[3:])
        env[k]=v
    elif len(cmd)==3 and cmd[1].lower()=='get': # ['env','get','key']
        k=cmd[2]
        res=env[k]
    else:
        rc=1
        res='env: Missing argument or unrecognized commnad.\nuse env help, for usage.'
    return rc,res,cwd,env
