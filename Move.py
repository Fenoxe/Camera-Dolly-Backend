import config
import Error
from DriverInterface import DriverInterface

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

        def keep_going(direc):
            if direc:
                if self.curr_pos > self.end_pos:
                    return True
                return False
            else:
                if self.curr_pos < self.end_pos:
                    return True
                return False
            

        dist = 0
        direc = 0
        duration = 0
        delta = 0

        # move slider from curr_pos to start_pos
        dist = self.start_pos - self.curr_pos
        if dist < 0:
            dist = -dist
            direc = 1
        duration = self.duration

        self.driver_interface.set_dir(direc)
        self.driver_interface.set_step(0)
        
        while keep_going(direc):
            self.driver_interface.step(delta)
