from pybleno import BlenoPrimaryService
from StartPosCharacteristic import StartPosCharacteristic
from EndPosCharacteristic import EndPosCharacteristic
from DurationCharacteristic import DurationCharacteristic
from ExecuteCharacteristic import ExecuteCharacteristic

class SliderService(BlenoPrimaryService):
    def __init__(self, move):
        BlenoPrimaryService.__init__(self, {
            'uuid': "aaaa1111bbbb2222cccc3333dddd4444",
            'characteristics': [
                StartPosCharacteristic(move),
                EndPosCharacteristic(move),
                DurationCharacteristic(move),
                ExecuteCharacteristic(move)
            ]
        })
