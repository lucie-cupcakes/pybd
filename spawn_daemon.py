"""Copyright (C) 2020 Lucie Cupcakes <lucie_linux [at] protonmail.com>
This file is part of pybd <https://gitlab.com/lucie_cupcakes/pybd>.
pybd is free software; you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free
Software Foundation; either version 3, or (at your option) any later
version.
pybd is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
for more details.
You should have received a copy of the GNU General Public License
along with pybd; see the file LICENSE.  If not see <http://www.gnu.org/licenses/>."""

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
