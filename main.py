import os

import requests
import json
import uuid
import os.path

machine_id = hex(uuid.getnode())
print('Your current machine-id is: ' + machine_id)

if os.path.exists('config.json'):
    with open('config.json', 'r') as f:
        config = json.load(f)
    x = requests.get('https://mctea.tk/verify2.php?type=check&license_key=' + config['license_key'] + '&machine_id=' + config['machine_id'])
    if x.json()['status'] == 'error':
        os.remove('config.json')
    elif x.json()['status'] == 'ok':
        print('activated')

else:
    license_key = input("Give me key: ")
    config = {"machine_id": machine_id, "license_key": license_key}

    x = requests.get('https://mctea.tk/verify2.php?type=register&license_key=' + config['license_key'] + '&machine_id=' + config['machine_id'])
    if x.json()['status'] == 'ok' and x.json()['registered'] == 'true':
        with open('config.json', 'w') as f:
            json.dump(config, f)
        print('key installed')
    else:
        print('invalid')
