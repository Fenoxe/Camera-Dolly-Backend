# pylint: disable=E0202

import pybleno
import Error
import Success
import os
from DriverInterface import DriverInterface

class ShutdownCharacteristic(pybleno.Characteristic):
    
    def __init__(self, blenoObj):
        pybleno.Characteristic.__init__(self, {
            'uuid': 'a6a1',
            'properties': ['write'],
            'descriptors': [
                pybleno.Descriptor({
                    'uuid': 'a6a2',
                    'value': 'Shuts down the RPi'
                })],
            'value': None
        })

        self.blenoObj = blenoObj

    def onWriteRequest(self, data, offset, withoutResponse, callback):
        print("Shutdown Write Called")
        print(data)
        if offset:
            Error.throw("Failed write in Shutdown (#1)")
            callback(pybleno.Characteristic.RESULT_ATTR_NOT_LONG)

        elif len(data) != 1:
            Error.throw("Failed write in Shutdown (#2)")
            callback(pybleno.Characteristic.RESULT_INVALID_ATTRIBUTE_LENGTH)

        else:
            parsed = int.from_bytes(data, byteorder='big', signed=False)
            if parsed == 1:
                Success.throw("Started Shutdown")
                DriverInterface.sleep(DriverInterface, 1)
                callback(pybleno.Characteristic.RESULT_SUCCESS)
                self.blenoObj.stopAdvertising()
                self.blenoObj.disconnect()
                if os.system('sudo shutdown -h now'):
                    Error.throw("--FAILED REBOOT--")
            elif parsed == 0:
                Success.throw("Wrote 0 to Shutdown")
                callback(pybleno.Characteristic.RESULT_SUCCESS)

            else:
                Error.throw("Failed write in Shutdown (#3)")
                callback(pybleno.Characteristic.RESULT_UNLIKELY_ERROR)
