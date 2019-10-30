import time
import sys
import pybleno
from SliderService import SliderService
import StartPosCharacteristic
import EndPosCharacteristic
import DurationCharacteristic
import Pins
from Move import Move
import config
import os
#import RPi.GPIO as GPIO

bleno = pybleno.Bleno()

os.environ['BLENO_DEVICE_NAME'] = 'TT Camera Slider'

# naming and creating the bluetooth service
sliderService = SliderService(Move())

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

    if not error:
        print('advertising...')
        bleno.setServices([
            sliderService
        ])

bleno.on('advertisingStart', onAdvertisingStart)

bleno.start()

print ('Hit <ENTER> to disconnect')

input()

bleno.stopAdvertising()
bleno.disconnect()

print ('terminated.')
sys.exit(1)