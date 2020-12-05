import sys,os

def process_cd_cmd(cmd,cwd,env)
    res=''
    rc=0
    if len(cmd)>=2:
        path=cmd[1]
        if path.find('@') == -1:
            if path=='..':
                path='@/..'
            elif not path.startswith('/'):
                path='@/{}'.format(path)
        path=path.replace('@', cwd)
        if os.path.exists(path) and os.path.isdir(path):
            cwd=os.path.realpath(path)
            res='OK'
        else:
            rc=1
            res='cd: {}: does not exists or is not a directory.'.format(path)
    else:
        rc,res,cwd,env=process_cd_cmd(['cd', env['HOME']], cwd, env)
    return rc,res,cwd,env
