import time
import sys
import pybleno
from SliderService import SliderService
from DeviceService import DeviceService
import StartPosCharacteristic
import EndPosCharacteristic
import DurationCharacteristic
import Pins
from Move import Move
import Config as config
import os

bleno = pybleno.Bleno()

os.environ['BLENO_DEVICE_NAME'] = 'TT Camera Slider'

# naming and creating the bluetooth service
move = Move()
sliderService = SliderService(move)
deviceService = DeviceService(bleno)

def onStateChange(state):
    if (state == 'poweredOn'):

        def on_startAdvertising(err):
            if err:
                print(err)

        bleno.startAdvertising(config.DEVICE_NAME, [sliderService.uuid], on_startAdvertising)

    else:
        bleno.stopAdvertising()
        
bleno.on('stateChange', onStateChange)
    
def onAdvertisingStart(error):

    def on_setServiceError(error):
        print('setServices: %s'  % ('error ' + error if error else 'success'))

    if not error:
        print('advertising...')
        bleno.setServices([
            sliderService,
            deviceService,
        ], on_setServiceError)

bleno.on('advertisingStart', onAdvertisingStart)

bleno.start()

print ('Hit <ENTER> to disconnect')

input()

move.driver_interface.sleep(1)

bleno.stopAdvertising()
bleno.disconnect()

print('terminated.')
sys.exit(1)
