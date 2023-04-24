import os
from threading import Thread

def tunnel():
    os.chdir(os.path.dirname(__file__))
    os.chdir('../frps')
    os.system('frps.exe -c config.txt > NUL')
    
def start():
    Thread(target=tunnel,daemon=True).start()