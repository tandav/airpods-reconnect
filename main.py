import json
import time
import subprocess
from pykeyboard import PyKeyboard # TODO: dive into source to get rid of PyUserInput dependency, also try osascript

AIRPODS_NAME = 'AirPods Pro'

cc = subprocess.check_call
co = lambda x: subprocess.check_output(x, text=True).strip()

def current_output():
    return co(['SwitchAudioSource', '-c'])

def get_id(name):
    for x in json.loads(co(['blueutil',  '--paired', '--format', 'json'])):
        if x['name'] == name:
            return x['address']

def disconnect(device_id):
    print('disconnect')
    cc(['blueutil', '--disconnect', device_id])

def connect(device_id):
    print('connect')
    while True:
        curr_device = current_output()
        if curr_device == AIRPODS_NAME:
            break
        print('waiting until connect, current output device is:', curr_device)
        time.sleep(1)

def is_connected(device_id):
    return co(['blueutil',  '--is-connected', device_id]) == '0'

airpods = get_id(AIRPODS_NAME)

while True:
    if current_output() != AIRPODS_NAME:
        print('triggered')
        disconnect(airpods)
        connect(airpods)
        print('pressing PLAY')
        PyKeyboard().press_key('KEYTYPE_PLAY') # resume playback
    print('all good' + ' ' * int(str(int(time.time()))[-1]) + '*')
    time.sleep(1)  
