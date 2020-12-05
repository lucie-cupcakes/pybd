from bash_run import bash_run
from process_cd_cmd import process_cd_cmd
from process_env_cmd import process_env_cmd
from process_spawn_cmd import process_spawn_cmd

def process_cmd(cmd,cwd,env):
    rc=-1
    res=''    
    if cmd[0]=='sv_ping':
        rc=0
        res='Pong!'
    elif cmd[0] == 'cd':
        rc,res,cwd,env=process_cd_cmd(cmd,cwd,env)
    elif cmd[0] == 'env':
        rc,res,cwd,env=process_env_cmd(cmd,cwd,env)
    elif cmd[0]=='spawn':
        rc,res,cwd,env=process_spawn_cmd(cmd,cwd,env)
    else:
        rc,res=bash_run(cmd=' '.join(cmd),cwd=cwd,env=env)
    return rc,res,cwd,env
