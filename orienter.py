import time
import math

class Orienter:
    """An Orienter object decomposes 3D data into vertical and lateral components."""
    def __init__(self):
        self.unitDown = None
        self.tempDown = None

        self.discrepancies = 0
        self.stable = 0

        self.currAccel = None
        self.currAccelSquared = None
        self.currMagnitude = None
        self.currMagnitudeSquared = None

    def checkDown(self):
        """ Timestamp """
        self.timestamp = time.time()

        """Verifies that the current down vector is good enough."""
        self.currAccelSquared = [acc**2 for acc in self.currAccel]
        self.currMagnitudeSquared = sum(self.currAccelSquared)
        self.currMagnitude = math.sqrt(self.currMagnitudeSquared)

        newDown = [acc/self.currMagnitude for acc in self.currAccel]

        if self.unitDown == None:
            self.unitDown = newDown
            self.actualDownMagnitude = self.currMagnitude
        if self.tempDown == None:
            self.tempDown = self.unitDown

        differences = [a-b for a,b in zip(self.unitDown, newDown)]

        # Update the down vector if it has been consistently wrong.
        if reduce((lambda x, y: x or y), [diff > 0.0001 for diff in differences]):
            if self.discrepancies > 25000: # Down may be wrong.
                diffTemp = [a-b for a, b in zip(self.tempDown, newDown)]
                if self.stable > 1000: # Down is definitely wrong
                    self.discrepancies = 0
                    self.stable = 0
                    self.unitDown = self.tempDown
                    self.actualDownMagnitude = self.currMagnitude
                elif reduce((lambda x, y: x or y), [diff < .05 for diff in diffTemp]):
                    self.stable += 1
                else:
                    self.stable = 0
                    self.tempDown = newDown
            else:
                self.discrepancies += 1
        else: # Down is right
            self.discrepancies = 0
            self.stable = 0

    def orient(self, accel):
        """Decomposes the acceleration data.

        accel -- the acceleration data from the accelerometer.
        """
        self.currAccel = accel
        self.checkDown()
        #The down component is the scalar product of currAccel and unitDown
        currentDownMagnitude = sum([a*b for a,b in zip(self.unitDown, self.currAccel)])
        #Subtract the current Magnitude in the down direction, by the recorded magnitude in the down direction
        downMagnitude = currentDownMagnitude - self.actualDownMagnitude
        #The side component is determined by the Pythagorean theorem.
        sideMagnitude = math.sqrt(abs(self.currMagnitudeSquared - currentDownMagnitude**2))

        return [downMagnitude, sideMagnitude, self.timestamp]
