import json
import time
import sys
import subprocess
from pykeyboard import PyKeyboard # TODO: dive into source to get rid of PyUserInput dependency, also try osascript

co = lambda *x: subprocess.check_output(x, text=True).strip()

airpods_name = 'AirPods Pro'

def get_id(name):
    for x in json.loads(co('blueutil', '--paired', '--format', 'json')):
        if x['name'] == name:
            return x['address']

airpods_id = get_id(airpods_name)

def current_output():
    return co('SwitchAudioSource', '-c')

def disconnect():
    print('disconnect')
    co('blueutil', '--disconnect', airpods_id)

def connect():
    print('connect')
    co('blueutil', '--connect', airpods_id)
    t = time.time()
    while True:
        curr_device = current_output()
        if curr_device == airpods_name:
            break
        if time.time() - t > 10:
            print('connect signal lost, sending connect signal again')
            t = time.time()
            co('blueutil', '--connect', airpods_id)
        print('waiting until connect, current output device is:', curr_device)
        time.sleep(1)
    time.sleep(2)
    print('successfully connected to', airpods_name)

def is_connected():
    return co('blueutil',  '--is-connected', airpods_id) == '1'

k = PyKeyboard()

while True:
    if current_output() != airpods_name:
        print('triggered')
        if is_connected():
            disconnect()
        connect()
        if len(sys.argv) == 2:
            print('pressing PLAY')
            k.press_key('KEYTYPE_PLAY') # resume playback
    print('all good' + ' ' * int(str(int(time.time()))[-1]) + '*')
    time.sleep(1)  
