import pybleno
import Error
import Success

class StartPosCharacteristic(pybleno.Characteristic):
    
    def __init__(self, move):
        pybleno.Characteristic.__init__(self, {
            'uuid': 'a1a1',
            'properties': ['read', 'write'],
            'descriptors': [
                pybleno.Descriptor({
                    'uuid': 'a1a2',
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
            start_pos = (int) (self.move.start_pos * 100)
            data = start_pos.to_bytes(1, "big")
            Success.throw("Read Start Pos")
            callback(pybleno.Characteristic.RESULT_SUCCESS, data)

    def onWriteRequest(self, data, offset, withoutResponse, callback):
        print("StartPos Data:")
        print(data)
        if offset:
            Error.throw("Failed write in Start Pos (#1)")
            callback(pybleno.Characteristic.RESULT_ATTR_NOT_LONG)

        elif len(data) != 1:
            Error.throw("Failed write in Start Pos (#2)")
            callback(pybleno.Characteristic.RESULT_INVALID_ATTRIBUTE_LENGTH)

        else:
            parsed = int.from_bytes(data, byteorder='big', signed=False)
            val = parsed / 100
            if self.move.set_start_pos(val):
                Error.throw("Failed write in Start Pos (#3)")
                callback(pybleno.Characteristic.RESULT_UNLIKELY_ERROR)

            else:
                Success.throw("Set Start Pos: " + str(val))
                callback(pybleno.Characteristic.RESULT_SUCCESS)