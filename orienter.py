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
        if self.tempDown == None:
            self.tempDown = self.unitDown

        differences = [a-b for a,b in zip(self.unitDown, newDown)]
        diffTemp = [a-b for a, b in zip(self.tempDown, newDown)]    

        # Update the down vector if it has been consistently wrong.
        if reduce((lambda x, y: x or y), [diff > 0.01 for diff in differences]):
            if self.discrepancies > 100000: # Down may be wrong.
                if self.stable > 1000: # Down is definitely wrong
                    self.discrepancies = 0
                    self.stable = 0
                    self.unitDown = self.tempDown
                elif reduce((lambda x, y: x or y), [diff < .05 for diff in diffTemp]):
                    self.stable += 1
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
        downMagnitude = sum([a*b for a,b in zip(self.unitDown, self.currAccel)])
        #The side component is determined by the Pythagorean theorem.
        sideMagnitude = math.sqrt(abs(self.currMagnitudeSquared - downMagnitude**2))
        
        return [downMagnitude, sideMagnitude, self.timestamp]
