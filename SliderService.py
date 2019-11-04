from pybleno import BlenoPrimaryService
from UUIDDatabase import UUIDDatabase as ID
from StartPosCharacteristic import *
from EndPosCharacteristic import *
from DurationCharacteristic import *
from ExecuteCharacteristic import *

class SliderService(BlenoPrimaryService):
    def __init__(self, move):
        BlenoPrimaryService.__init__(self, {
            'uuid': ID.get("Slider Service"),
            'characteristics': [
                StartPosCharacteristic(move),
                EndPosCharacteristic(move),
                DurationCharacteristic(move)
                #ExecuteCharacteristic(move)
            ]
        })
