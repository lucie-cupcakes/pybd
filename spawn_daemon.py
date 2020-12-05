import sys, os

def spawn_daemon(func, args=None):
    # do the UNIX double-fork magic, see Stevens' 'Advanced
    # Programming in the UNIX Environment' for details (ISBN 0201563177)
    try:
        pid = os.fork()
        if pid > 0:
            return
    except OSError as e:
        print('fork #1 failed: %d (%s)' % (e.errno, e.strerror), file=sys.stderr)
        sys.exit(1)
    os.setsid()
    try:
        pid = os.fork()
        if pid > 0:
            sys.exit(0)
    except OSError as e:
        print('fork #2 failed: %d (%s)' % (e.errno, e.strerror), file=sys.stderr)
        sys.exit(1)
    if args != None:
        func(args)
    else:
        func()
    os._exit(os.EX_OK)
