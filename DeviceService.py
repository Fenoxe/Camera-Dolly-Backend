from pybleno import BlenoPrimaryService
from RebootCharacteristic import RebootCharacteristic
from ShutdownCharacteristic import ShutdownCharacteristic

class DeviceService(BlenoPrimaryService):
    def __init__(self, blenoObj):
        BlenoPrimaryService.__init__(self, {
            'uuid': "aaaa1111bbbb2222cccc3333eeee5555",
            'characteristics': [
                RebootCharacteristic(blenoObj),
                ShutdownCharacteristic(blenoObj)
            ]
        })
