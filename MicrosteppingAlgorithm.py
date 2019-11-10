class MicrosteppingAlgorithm:

    @staticmethod
    def calculate(step_delay):
        b = 0.0001

        if step_delay > (16 * b):
            return 4
        if step_delay > (8 * b):
            return 3
        if step_delay > (4 * b):
            return 2
        if step_delay > (2 * b):
            return 1
        return 0
