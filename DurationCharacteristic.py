import pybleno
import Error
import Success

class DurationCharacteristic(pybleno.Characteristic):
    
    def __init__(self, move):
        pybleno.Characteristic.__init__(self, {
            'uuid': 'a3a1',
            'properties': ['read', 'write'],
            'descriptors': [
                pybleno.Descriptor({
                    'uuid': 'a3a2',
                    'value': 'Gets or sets the Duration'
                })],
            'value': None
        })

        self.move = move
    
    def onReadRequest(self, offset, callback):
        print('duration read req')
        if offset:
            Error.throw("Failed read in Duration")
            callback(pybleno.Characteristic.RESULT_ATTR_NOT_LONG, None)

        else:
            duration = int(self.move.duration)
            data = duration.to_bytes(2, "big")
            Success.throw("Read Duration")
            callback(pybleno.Characteristic.RESULT_SUCCESS, data)

    def onWriteRequest(self, data, offset, withoutResponse, callback):
        print("Duration Data:")
        print(data)
        if offset:
            Error.throw("Failed write in Duration (#1)")
            callback(pybleno.Characteristic.RESULT_ATTR_NOT_LONG)

        elif len(data) != 2:
            Error.throw("Failed write in Duration (#2)")
            callback(pybleno.Characteristic.RESULT_INVALID_ATTRIBUTE_LENGTH)

        else:
            parsed = int.from_bytes(data, byteorder='big', signed=False)
            print("parsed: " + str(parsed))
            if self.move.set_duration(parsed):
                Error.throw("Failed write in Duration (#3)")
                callback(pybleno.Characteristic.RESULT_UNLIKELY_ERROR)

            else:
                Success.throw("Set Duration: " + str(parsed))
                callback(pybleno.Characteristic.RESULT_SUCCESS)
