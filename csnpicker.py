from collections import deque
#import publisher
import math
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

        self.sumLTA = 0
        self.sumSTA = 0
        self.sum2LTA = 0
        self.sum2STA = 0

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

         """
        length = len(self.accels)
        if length <= self.window*20: #Populate the deque of acceleration data
            self.sum2LTA += self.accels[-1][0]**2
            self.sumLTA += self.accels[-1][0]
            return
        #Chunk chunk chunk
        self.sum2LTA += self.accels[-1][0]**2 - self.accels[0][0]**2
        self.sumLTA += self.accels[-1][0] - self.accels.popleft()[0]

        self.LTA = self.sumLTA/(self.window*20)
        self.stdev = math.sqrt(self.sum2LTA/(self.window*3) - self.LTA**2)

        self.sumSTA = 0
        for i in range(self.window):
            self.sumSTA += abs(self.accels[-1-i][0] - self.LTA)
        self.STA = self.sumSTA/self.window

        metric = self.STA/self.stdev
        logger.addToLine(metric)

        time = self.accels[-1][1]

        currAcc = self.accels[-1][0]

        if metric > self.threshold and (self.currentPick == None or metric > self.currentPick.metric):
            self.currentPick = Pick(self.name, metric, currAcc, time)
            self.counter = 1 #self.window

    def pickDetected(self):
        """Publishes a confirmed pick."""
        #print(self.currentPick)
        #publisher.publish(str(self.currentPick))



class Pick:
    """
        A Pick object provides a neat internal representation for a Pick
    """
    def __init__(self, name, metric, accel, time):
        self.name = name
        self.metric = metric
        self.accel = accel
        self.time = time

    def __str__(self):
        """The String representation of the Pick."""
        return self.name+' Pick with Metric of: '+str(self.metric)+' at '+str(self.time)
