import pybleno
from UUIDDatabase import UUIDDatabase as ID
from StartPosCharacteristic import *
from EndPosCharacteristic import *
from DurationCharacteristic import *

class SliderService(pybleno.BlenoPrimaryService):
    def __init__(self, move):
        pybleno.BlenoPrimaryService.__init__(self, {
            'uuid': ID.get("Slider Service"),
            'characteristics': [
                StartPosCharacteristic(move),
                EndPosCharacteristic(move),
                DurationCharacteristic(move)
            ]
        })