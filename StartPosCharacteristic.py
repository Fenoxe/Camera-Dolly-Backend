import pybleno
from UUIDDatabase import UUIDDatabase as ID
import Error
import Success

class StartPosCharacteristic(pybleno.Characteristic):
    
    def __init__(self, move):
        pybleno.Characteristic.__init__(self, {
            'uuid': ID.get('Start Position Characteristic'),
            'properties': ['read', 'write'],
            'descriptors': [
                pybleno.Descriptor({
                    'uuid': ID.get('Start Position Characteristic Descriptor'),
                    'value': 'Gets or sets the Start Position'
                })],
            'value': None
        })

        self.move = move
        
    def onReadRequest(self, offset, callback):
        if offset:
            Error.throw("Failed read in Start Pos")
            callback(pybleno.Characteristic.RESULT_ATTR_NOT_LONG, None)

        else:
            start_pos = (int) (self.move.start_pos * 10)
            data = bytes([start_pos])
            Success.throw("Read Start Pos")
            callback(pybleno.Characteristic.RESULT_SUCCESS, data)

    def onWriteRequest(self, data, offset, withoutResponse, callback):
        if offset:
            Error.throw("Failed write in Start Pos (#1)")
            callback(pybleno.Characteristic.RESULT_ATTR_NOT_LONG)

        elif len(data) != 1:
            Error.throw("Failed write in Start Pos (#2)")
            callback(pybleno.Characteristic.RESULT_INVALID_ATTRIBUTE_LENGTH)

        else:
            parsed = int.from_bytes(data, byteorder='big', signed=False)
            if self.move.set_start_pos(parsed / 10):
                Error.throw("Failed write in Start Pos (#3)")
                callback(pybleno.Characteristic.RESULT_UNLIKELY_ERROR)

            else:
                Success.throw("Set Start Pos")
                callback(pybleno.Characteristic.RESULT_SUCCESS)