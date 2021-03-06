import csv
import time

datetime = time.strftime("%Y%m%d_%H%M%S")
updatedfilename = 'shaketest_'+datetime+'.csv'
line = []

def addToLine(data):
    line.append(data)


def addLine():
    ''' simply logs data '''
    global line

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

def addSeparator(text):
    with open(updatedfilename, "a") as myFile:
        myFile.write(text+'\n')
