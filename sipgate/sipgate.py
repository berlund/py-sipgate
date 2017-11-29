""" Simple client for the Sipgate REST API.
For details about the API see https://developer.sipgate.io
This client comes with some restrictions:
- Basic Authentication is the only implemented authentication mechanism
- Currently only the endpoints devices/ and devices/{deviceid} are supported
"""
import requests
from model import Device

BASE_URL = "https://api.sipgate.com/v1/"

class SipgateApi(object):
    """The client"""

    def __init__(self, username, password):
        """ Initiate with username and password used for basic authentication"""
        self._username = username
        self._password = password      

    def devices(self):
        """Calls /devices"""
        response = requests.get(BASE_URL + "devices/", auth=(self._username, self._password))
        if(response.ok):
            json = response.json()
            devices = json.get('items')
            result = []
            for device in devices:
                result.append(Device.from_json(device))
            return result
        else:
            response.raise_for_status()
        

    def device_by_id(self, device_id):
        """Calls /devices/{device_id}"""
        response = requests.get(BASE_URL + "devices/" + device_id, auth=(self._username, self._password))
        if(response.ok):
            json = response.json()
            return Device.from_json(json)
        else:
            response.raise_for_status()

