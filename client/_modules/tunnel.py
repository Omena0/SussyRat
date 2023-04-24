import os
from threading import Thread

def tunnel():
    os.chdir(os.path.dirname(__file__))
    os.chdir('../frps')
    os.system('frpc.exe -c cconfig.txt > NUL')

def start():
    Thread(target=tunnel,daemon=True).start()