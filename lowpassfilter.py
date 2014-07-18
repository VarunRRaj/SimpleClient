"""
    Input[data,time] is passed through a lowpassfilter to remove noise
"""
class LowPassFilter:
    def __init__(self, samplerate, cutofffrequency):
        self.dt = 1.0 /samplerate
        self.RC = 1.0 /cutofffrequency
        print(samplerate, cutofffrequency, self.dt, self.RC)
        self.alpha = self.dt / (self.dt+self.RC)
        self.oneminusalpha = 1 - self.alpha
        self.olddata = 0

    def add(self, data):
        self.olddata = self.alpha*data[0] + self.olddata*self.oneminusalpha
        return [self.olddata, data[1]]
