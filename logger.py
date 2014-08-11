import csv
import datetime

def _init_(self)
    datetime = str(datetime.datetime.now())
    self.updatedfilename = 'shaketest_'+datetime+'.csv'

def add(self, data):
    ''' simply logs data '''

    if isinstance(data, list):
        ofile = open(self.updatedfilename, "a")
        writer = csv.writer(ofile)
        writer.writerow(data)
    elif isinstance(data, float):
        with open(self.updatedfilename, "a") as myFile:
            myFile.write(str(data)+'\n')
    else:
        print("No input for logger")
        
        
        


def clear():
    open('log.csv', 'w').close()
