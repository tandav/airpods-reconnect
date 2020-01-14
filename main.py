import json
import time
import subprocess
from pykeyboard import PyKeyboard # TODO: dive into source to get rid of PyUserInput dependency

cc = subprocess.check_call
co = lambda x: subprocess.check_output(x, text=True).strip()

AIRPODS_NAME = 'AirPods Pro'

def find(name):
    _ = co(['blueutil',  '--paired', '--format', 'json'])
    _ = json.loads(_)
    for x in _:
        if x['name'] == name:
            return x
        
def disconnect(id_): cc(['blueutil', '--disconnect', id_])
def connect   (id_): cc(['blueutil', '--connect'   , id_])
def is_connected(id_): return co(['blueutil',  '--is-connected', 'e4-76-84-20-f5-8d']) == '0'


airpods = find(AIRPODS_NAME)
'''
airpods object looks like:
{
    'address': 'e4-76-84-20-f5-8d',
    'recentAccessDate': '2020-01-14T08:58:45+03:00',
    'paired': True,
    'RSSI': 0,
    'rawRSSI': -54,
    'favourite': False,
    'connected': True,
    'name': 'AirPods Pro',
    'slave': False,
}
'''

def current_output(): return co(['SwitchAudioSource', '-c'])

# if current_output() != AIRPODS_NAME:
#     print('triggered')
#     disconnect(airpods['address'])
#     connect(airpods['address'])


while True:
    if current_output() != AIRPODS_NAME:
        print('triggered')
        if not is_connected:
            print('disconnect')
            disconnect(airpods['address'])
        print('connect')
        connect(airpods['address'])

        while True:
            curr_device = current_output()
            print('waiting reconnect', curr_device)
            if curr_device == AIRPODS_NAME:
                print(curr_device == AIRPODS_NAME)
                continue
            time.sleep(1)

        print('pressing PLAY')
        PyKeyboard().press_key('KEYTYPE_PLAY') # resume playback
    else:
        print('all good')
    time.sleep(1)  
