import csv
import datetime

def add(data):
    ''' simply logs data '''
    datetime = str(datetime.datetime.now())
    updatedfilename = 'shaketest_'+datetime+'.csv'
    if isinstance(data, list):
        ofile = open(updatedfilename, "a")
        writer = csv.writer(ofile)
        writer.writerow(data)
    elif isinstance(data, float):
        with open(updatedfilename, "a") as myFile:
            myFile.write(str(data)+'\n')
    else:
        print("No input for logger")
        
        
        


def clear():
    open('log.csv', 'w').close()
