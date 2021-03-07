import json


def get_conf():
    try:
        with open('easyaws_conf.json', 'r') as credfile:
            confdata = json.load(credfile)
            return confdata
    except OSError :
        return {'access_key_id': None, 'secret_access_key': None, 'region': None}
