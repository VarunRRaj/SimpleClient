import csv
import datetime

tdatetime = str(datetime.datetime.now())
updatedfilename = 'shaketest_'+datetime+'.csv'

def addLine(data):
    ''' simply logs data '''

    if isinstance(data, list):
        ofile = open(updatedfilename, "a")
        writer = csv.writer(ofile)
        writer.writerow(data)
    elif isinstance(data, float):
        with open(updatedfilename, "a") as myFile:
            myFile.write(str(data)+'\n')
    else:
        print("No input for logger")
