import config
import Error

class Move:
    
    def __init__(self):
        self.start_pos = 0
        self.end_pos = 0
        self.duration = 0
        self.distance = 0
        self.velocity = 0

    def set_start_pos(self, start_pos):
        # if start_pos < config.MIN_POS or start_pos > config.MAX_POS:
        #     throw_error("start pos out of range")
        #     return 1

        self.start_pos = start_pos

    def set_end_pos(self, end_pos):
        # if end_pos < config.MIN_POS or end_pos > config.MAX_POS:
        #     throw_error("end pos out of range")
        #     return 1

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
