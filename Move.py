import config
import Error
from DriverInterface import DriverInterface
import time

class Move:
    
    def __init__(self):
        self.start_pos = 0
        self.end_pos = 0
        self.duration = 0
        self.distance = 0
        self.velocity = 0
        self.curr_pos = (config.MAX_POS + config.MIN_POS) / 2
        self.driver_interface = DriverInterface()

    def set_start_pos(self, start_pos):
        if start_pos < config.MIN_POS or start_pos > config.MAX_POS:
            Error.throw("start pos out of range")
            return 1

        self.start_pos = start_pos

    def set_end_pos(self, end_pos):
        if end_pos < config.MIN_POS or end_pos > config.MAX_POS:
            Error.throw("end pos out of range")
            return 1

        self.end_pos = end_pos

    def set_duration(self, duration):
        if duration < config.MIN_DURATION or duration > config.MAX_DURATION:
            Error.throw("duration out of range")
            return 1

        self.duration = duration

    def calculate_distance(self):
        if not self.start_pos or not self.end_pos:
            Error.throw("start and/or end positions not set")
            return 1

        self.distance = self.end_pos - self.start_pos
        
    def calculate_velocity(self):
        if not self.distance or not self.duration:
            Error.throw("distance and/or duration not set")
            return 1

        velocity = self.distance / self.duration
        speed = abs(velocity)
        
        if speed > config.MAX_SPEED or speed < config.MIN_SPEED:
            Error.throw("velocity is out of range")
            return 1
        
        self.velocity = velocity

    def calculate(self):
        if self.calculate_distance():
            return 1

        if self.calculate_velocity():
            return 1
        

    def execute_move(self):
        
        # PHASE 1.1: move slider from curr_pos to start_pos | calculations
        dist = 0
        direc = 0
        velocity = 0
        rps = 0
        step_delay = 0
        step_count = 0

        dist = self.start_pos - self.curr_pos

        if dist < 0:
            dist = -dist
            direc = 1

        velocity = config.DEFAULT_VELOCITY

        rps = abs(velocity) * config.VEL_TO_RPS

        step_delay = (1 / (rps * 360)) * config.STEP_ANGLE

        step_count = int(round(dist * config.DIST_TO_STEPS))

        print("MOVE TO START")
        print("curr_pos = " + str(self.curr_pos))
        print("start_pos = " + str(self.start_pos))
        print("dist = " + str(dist))
        print("direc = " + str(direc))
        print("velocity = " + str(velocity))
        print("rps = " + str(rps))
        print("step_delay = " + str(step_delay))
        print("step_count = " + str(step_count))
        print("")

        # PHASE 1.2: execute move to start_pos
        self.driver_interface.set_dir(direc)
        self.driver_interface.set_step(0) # MICROSTEPPING?
        
        self.driver_interface.execute(step_delay, step_count)

        self.curr_pos += dist * (1 - 2 * direc)

        print("new_pos = " + str(self.curr_pos))
        print("")

        # PHASE 2.1: move slider from start_pos to end_pos | calculations
        dist = 0
        direc = 0
        velocity = 0
        rps = 0
        step_delay = 0
        step_count = 0

        if self.calculate():
            Error.throw("Calculate Failed")
            return 1

        dist = self.end_pos - self.start_pos

        if dist < 0:
            dist = -dist
            direc = 1

        velocity = self.velocity

        rps = abs(velocity) * config.VEL_TO_RPS

        step_delay = (1 / (rps * 360)) * config.STEP_ANGLE

        step_count = int(round(dist * config.DIST_TO_STEPS))

        print("START TO END")
        print("curr_pos = " + str(self.curr_pos))
        print("start_pos = " + str(self.start_pos))
        print("dist = " + str(dist))
        print("direc = " + str(direc))
        print("velocity = " + str(velocity))
        print("rps = " + str(rps))
        print("step_delay = " + str(step_delay))
        print("step_count = " + str(step_count))
        print("")

        # PHASE 2.2: execute move to end_pos
        self.driver_interface.set_dir(direc)
        self.driver_interface.set_step(0) # MICROSTEPPING?
        
        self.driver_interface.execute(step_delay, step_count)

        self.curr_pos += dist * (1 - 2 * direc)

        print("new_pos = " + str(self.curr_pos))

        return 0
