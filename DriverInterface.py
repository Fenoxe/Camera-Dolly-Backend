from Pins import Pins as PINS
import time
import RPi.GPIO as GPIO

class DriverInterface:
    
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(PINS.all_list, GPIO.OUT)
        GPIO.setup(PINS.INITSTOP, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.output(PINS.ENABLE, GPIO.HIGH) # by default disabled
        GPIO.output(PINS.RST, GPIO.HIGH)
        GPIO.output(PINS.SLEEP, GPIO.LOW) # by default in sleep mode
        GPIO.output(PINS.STEP, GPIO.LOW)

    # dir=0 for low, dir=1 for high
    def set_dir(self, dir):
        output = GPIO.HIGH if dir else GPIO.LOW
        GPIO.output(PINS.DIR, output)

    # step_size=0-4, full, half, etc [2^(-step_size) steps per tick]
    def set_step(self, step_size):
        vals = [GPIO.HIGH for _ in range(3)]

        if step_size != 4:
            vals[2] = GPIO.LOW
        if step_size <= 1:
            vals[1] = GPIO.LOW
        if step_size == 0 or step_size == 2:
            vals[0] = GPIO.LOW

        for channel, output in zip(PINS.MS_list, vals):
            GPIO.output(channel, output)

    def execute(self, step_delay, step_count):
        self.sleep(0)
        time.sleep(0.2)
        self.enable(1)
        delay = step_delay / 2
        for _ in range(step_count):
            GPIO.output(PINS.STEP, GPIO.HIGH)
            time.sleep(delay)
            GPIO.output(PINS.STEP, GPIO.LOW)
            time.sleep(delay)
        time.sleep(0.5)
        self.enable(0)

    def execute_INITIAL(self, step_delay, step_count):
        self.sleep(0)
        time.sleep(0.2)
        self.enable(1)
        delay = step_delay / 2
        for _ in range(step_count):
            GPIO.output(PINS.STEP, GPIO.HIGH)
            time.sleep(delay)
            GPIO.output(PINS.STEP, GPIO.LOW)
            time.sleep(delay)
            if GPIO.INPUT(PINS.INITSTOP):
                break
        time.sleep(0.5)
        self.enable(0)

    def terminate(self):
        GPIO.cleanup()

    # state=1 off state=0 on
    def sleep(self, state):
        if state:
            GPIO.output(PINS.SLEEP, GPIO.LOW)
        else:
            GPIO.output(PINS.SLEEP, GPIO.HIGH)

    # state=1 on state=0 off
    def enable(self, state):
        if state:
            GPIO.output(PINS.ENABLE, GPIO.LOW)
        else:
            GPIO.output(PINS.ENABLE, GPIO.HIGH)