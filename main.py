import json
import time
import subprocess
from pykeyboard import PyKeyboard # TODO: dive into source to get rid of PyKeyboard dependency

AIRPODS_NAME = 'AirPods Pro'

def find(name):
    _ = subprocess.check_output(['blueutil',  '--paired', '--format', 'json'])
    _ = json.loads(_)
    for x in _:
        if x['name'] == name:
            return x
        
def disconnect(id_): subprocess.run(['blueutil', '--disconnect', id_])
def connect   (id_): subprocess.run(['blueutil', '--connect'   , id_])


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

def current_output():
    return subprocess.check_output(['SwitchAudioSource', '-c'], text=True).strip()

# if current_output() != AIRPODS_NAME:
#     print('triggered')
#     disconnect(airpods['address'])
#     connect(airpods['address'])


while True:
    if current_output() != AIRPODS_NAME:
        print('triggered')
        disconnect(airpods['address'])
        connect(airpods['address'])

        while True:
            curr_device = current_output()
            print('waiting reconnect', curr_device)
            if curr_device == AIRPODS_NAME:
                continue
            time.sleep(1)

        PyKeyboard().press_key('KEYTYPE_PLAY')
    else:
        print('all good')
    time.sleep(1)  
