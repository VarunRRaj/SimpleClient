from collections import deque
#import publisher
import logger

class Picker:
    """A Picker Object will take in one dimensional data and calculate the
        Modified Energy Ratio for each time, as described by Wong et al.
    """

    def __init__(self, name, windowSize, threshold):
        self.name = name
        self.window = windowSize
        self.threshold = threshold
        self.currentPick = None
        self.counter = None
        self.accels = deque()

        self.numerator = 0
        self.denominator = 0

    def add(self, data):
        """Incorporates the next data point.

        data -- The acceleration and timestamp.
        """
        if self.counter != None:
            self.counter -= 1
            if self.counter == 0:
                self.pickDetected()
                self.counter = None
                self.currentPick = None
        self.accels.append(data)
        self.checkForPick()

    def checkForPick(self):
        """Checks if the current data point is a Pick and calculates the current Modified Energy Ratio.

        Uses the algorithm described by Wong et al. The MER for the middle
        element of the deque.
        """
        length = len(self.accels)
        if length <= self.window*2+1: #Populate the deque of acceleration data
            if length <= self.window+1:
                self.numerator += self.accels[-1][0]**2
            elif length > self.window:
                self.denominator += self.accels[-1][0]**2
            return

        index = self.window
        currAcc = self.accels[index][0]
        time = self.accels[index][1]
        nextMag = self.accels[index+1][0]**2

        er = self.numerator / self.denominator #energy ratio
        mer = (abs(currAcc)*er)**3 #modified energy ratio
        print(mer)
        logger.addToLine(mer)

        if mer > self.threshold and (self.currentPick == None or
                                     mer > self.currentPick.mer):
            self.currentPick = Pick(self.name, mer, currAcc, time)
            self.counter = 0 #4*self.window

        self.denominator += self.accels[-1][0]**2 - nextMag
        self.numerator += nextMag - self.accels.popleft()[0]**2

    def pickDetected(self):
        """Publishes a confirmed pick."""
        print(self.currentPick)
        #publisher.publish(str(self.currentPick))




class Pick:
    """
        A Pick object provides a neat internal representation for a Pick
    """
    def __init__(self, name, mer, accel, time):
        self.name = name
        self.mer = mer
        self.accel = accel
        self.time = time

    def __str__(self):
        """The String representation of the Pick."""
        return self.name+' Pick with MER of: '+str(self.mer)+' at '+str(self.time)
