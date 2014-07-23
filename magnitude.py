import time
import math

class Magnitude:
    def add(accel):
        currMagnitude = math.sqrt(sum([acc**2 for acc in accel]))
        return [currMagnitude, time.time()]
