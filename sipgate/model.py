class Device(object):

    def __init__(self, device_id, alias, online):
        self._id = device_id
        self._alias = alias
        self._online = online

    @property
    def id(self):
        return self._id

    @property
    def alias(self):
        return self._alias

    @property
    def online(self):
        return self._online

    @staticmethod
    def from_json(json_object):
        return Device(
            json_object.get('id'), 
            json_object.get('alias'),
            json_object.get('online'))
