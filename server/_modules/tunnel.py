import os
from threading import Thread

def tunnel():
    try:
        os.chdir(os.path.dirname(__file__))
        os.chdir('../frps')
        os.system('frps.exe -c config.txt > NUL')
    except:
        print('Could not start FRPS, Are you using pyinstaller?')
    
def start():
    Thread(target=tunnel,daemon=True).start()