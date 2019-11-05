from pybleno import BlenoPrimaryService
from UUIDDatabase import UUIDDatabase as ID
from StartPosCharacteristic import *
from EndPosCharacteristic import *
from DurationCharacteristic import *
from ExecuteCharacteristic import *

class SliderService(BlenoPrimaryService):
    def __init__(self, move):
        BlenoPrimaryService.__init__(self, {
            'uuid': "15b019f3c88cdc319daf2dc528b7ff3c",
            'characteristics': [
                StartPosCharacteristic(move),
                EndPosCharacteristic(move),
                DurationCharacteristic(move),
                ExecuteCharacteristic(move)
            ]
        })
