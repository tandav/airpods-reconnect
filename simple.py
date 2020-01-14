# tmp script
import json
import subprocess

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

airpods = find(AIRPODS_NAME)
disconnect(airpods['address'])
connect(airpods['address'])
