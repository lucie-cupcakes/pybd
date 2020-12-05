import sys, os, subprocess, uuid

def bash_run(cmd, cwd, env):
    fpath = "/tmp/bashrun_{}.sh".format(str(uuid.uuid4()))
    fh = open(fpath, "w+")
    fh.write("#!/bin/bash\n{}\n".format(cmd))
    fh.close()
    p=subprocess.Popen(['/bin/bash', fpath], shell=False, cwd=cwd, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    rc=p.wait()
    os.remove(fpath)
    res=p.stdout.read().decode()
    return rc,res
