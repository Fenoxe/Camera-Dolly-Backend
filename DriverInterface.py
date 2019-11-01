from Pins import Pins as PINS
import RPi.GPIO as GPIO

class DriverInterface:
    
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(PINS.all_list, GPIO.OUT)

    def set_step(self, step_size):
        vals = [GPIO.HIGH for _ in range(3)]

        if step_size != 4:
            vals[2] = GPIO.LOW
        if step_size <= 1:
            vals[1] = GPIO.LOW
        if step_size == 0 or step_size == 2:
            vals[0] = GPIO.LOW

        for channel, output in PINS.MS_list, vals:
            GPIO.output(channel, output)

    def terminate(self):
        GPIO.cleanup()