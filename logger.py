import csv
import datetime

datetime = str(datetime.datetime.now())
updatedfilename = 'shaketest_'+datetime+'.csv'
line = []

def addToLine(data):
    line.append.(data)


def addLine:
    ''' simply logs data '''

    if isinstance(line, list):
        ofile = open(updatedfilename, "a")
        writer = csv.writer(ofile)
        writer.writerow(line)
    elif isinstance(line, float):
        with open(updatedfilename, "a") as myFile:
            myFile.write(str(line)+'\n')
    else:
        print("No input for logger")

    line = []
