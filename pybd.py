"""Copyright (C) 2021 Lucie Cupcakes <lucie_linux [at] protonmail.com>
This file is part of pybd <https://github.com/lucie-cupcakes/pybd>.
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

import os
from server_main import server_main

if __name__ == '__main__':
    print('pydb - Python Backdoor Daemon.')
    print('Forever beta software. Use on production on your own risk!\n')
    print('This software is Free software - released under the GPLv3 License.')
    print('Read the LICENSE file. Or go visit https://www.gnu.org/licenses/gpl-3.0.html\n')
    server_main(host=os.environ['host'],port=int(os.environ['port']))
