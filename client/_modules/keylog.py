from pynput.keyboard import Listener

msg = ''

def on_press(key):
    global msg,callback
    key = str(key)
    #print(key)
    if key == 'Key.enter':
        callback(msg)
        msg = ''
    else:
        key = key.replace("'",'').replace('Key.space', ' ').replace('Key.backspace', '[<]')
        msg = msg + key




def start(func):
    global callback
    callback = func
    listener = Listener(on_press=on_press).start()