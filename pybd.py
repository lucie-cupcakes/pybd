import os
from server_main import server_main

if __name__ == '__main__':
    server_main(host=os.environ['host'],port=int(os.environ['port']))
