# pylint: disable=E0202

import pybleno
import Error
import Success
import os
from DriverInterface import DriverInterface

class RebootCharacteristic(pybleno.Characteristic):
    
    def __init__(self, blenoObj):
        pybleno.Characteristic.__init__(self, {
            'uuid': 'a5a1',
            'properties': ['write'],
            'descriptors': [
                pybleno.Descriptor({
                    'uuid': 'a5a2',
                    'value': 'Reboots the RPi'
                })],
            'value': None
        })

        self.blenoObj = blenoObj

    def onWriteRequest(self, data, offset, withoutResponse, callback):
        print("Reboot Write Called")
        print(data)
        if offset:
            Error.throw("Failed write in Reboot (#1)")
            callback(pybleno.Characteristic.RESULT_ATTR_NOT_LONG)

        elif len(data) != 1:
            Error.throw("Failed write in Reboot (#2)")
            callback(pybleno.Characteristic.RESULT_INVALID_ATTRIBUTE_LENGTH)

        else:
            parsed = int.from_bytes(data, byteorder='big', signed=False)
            if parsed == 1:
                Success.throw("Started Reboot")
                di = DriverInterface()
                di.sleep(1)
                callback(pybleno.Characteristic.RESULT_SUCCESS)
                self.blenoObj.stopAdvertising()
                self.blenoObj.disconnect()
                if os.system('sudo shutdown -r now'):
                    Error.throw("--FAILED REBOOT--")
            elif parsed == 0:
                Success.throw("Wrote 0 to Reboot")
                callback(pybleno.Characteristic.RESULT_SUCCESS)

            else:
                Error.throw("Failed write in Reboot (#3)")
                callback(pybleno.Characteristic.RESULT_UNLIKELY_ERROR)
