from bash_run import bash_run
from spawn_daemon import spawn_daemon

def internal_cmd_spawn(args):
    bash_run(cmd=args['cmd'],cwd=args['cwd'],env=args['env'])

def process_spawn_cmd(cmd,cwd,env):
    rc=0
    res=''
    if len(cmd)>=2:
        args={}
        args['cmd']=' '.join(cmd[1:])
        args['cwd']=cwd
        args['env']=env
        spawn_daemon(internal_cmd_spawn,args)
        res='Daemon started.'
    else:
        rc=1
        res='spawn: Invalid number of arguments.'
    return rc,res,cwd,env
