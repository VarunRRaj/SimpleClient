from collections import deque
import os
import sys

import csv

import matplotlib.pyplot as plt
import matplotlib.animation as animation



def findDataSet(filename, rowbegin, rowend, columnvalue):
    csvfile = open(filename, "rb")
    reader = csv.reader(csvfile)
    read = 0
    arrayTime= []
    arrayValue = []
    test = 0
    for row in reader:
        if row == rowend:
            read = 0
        if read == 1:
            if len(row) == 7:
                arrayTime.append(float(row[0]))
                if columnvalue == 1:
                    arrayValue.append(float(row[1]))
                elif columnvalue == 2:
                    arrayValue.append(float(row[2]))
                elif columnvalue == 3:
                    arrayValue.append(float(row[3]))
                elif columnvalue == 4:
                    arrayValue.append(float(row[4]))
                elif columnvalue == 5:
		    arrayValue.append(float(row[5]))
                elif columnvalue == 6:
                    arrayValue.append(float(row[6]))
                else:
                    print('Error')
                    sys.exit()
        if row == rowbegin:
            read = 1

    return arrayTime, arrayValue


def specifyMeasurement(value):
    print('For the '+value+' data set, which measurement would you like to display')
    print('A - Z - Raw')
    print('B - XY -Raw')
    print('C - Z - MER values from Wong')
    print('D - XY - MER values from Wong')
    print('E - Z - Metric Values from CSN')
    print('F - XY - Metric Values from CSN')

    
def specifyWindow(value):
    print('For the '+value+' data set, which window would you like to display')
    print('A - 1')
    print('B - 2')
    print('C - 5')
    print('D - 10')
    print('E - 20')
    print('F - 50')
    print('G - 100')
    print('H - 200')
    print('I - 500')
    print('J - 1000')
    
def specifyIntensity(value):
    print('For the '+ value +' data set, which intensity would you like to display')
    print('A - Noise')
    print('B - 50 mV')
    print('C - 75 mV')
    print('D - 100 mV')
    print('E - 125 mV')
    print('F - 150 mV')

def findFile(value):
    #1) NOISE,2) 100 mV,3) 75 mV,4) 50 mV,5) 125 mV,6) 150 mV
    if value == 'A':
        return 'shaketest_20140813_123405.csv'
    elif value == 'B':
        return 'shaketest_20140813_140743.csv'
    elif value == 'C':
        return 'shaketest_20140813_134025.csv'
    elif value == 'D':
        return 'shaketest_20140813_132402.csv'
    elif value == 'E':
        return 'shaketest_20140813_142110.csv'
    elif value == 'F':
        return 'shaketest_20140813_143344.csv'
    else:
        print('Error')
        sys.exit()

def findWindow(value):
    if value == 'A':
        return ['WINDOW=1'], ['WINDOW=2']
    elif value == 'B':
        return ['WINDOW=2'], ['WINDOW=5']
    elif value == 'C':
        return ['WINDOW=5'], ['WINDOW=10']
    elif value == 'D':
        return ['WINDOW=10'], ['WINDOW=20']
    elif value == 'E':
        return ['WINDOW=20'], ['WINDOW=50']
    elif value == 'F':
        return ['WINDOW=50'], ['WINDOW=100']
    elif value == 'G':
        return ['WINDOW=100'], ['WINDOW=200']
    elif value == 'H':
        return ['WINDOW=200'], ['WINDOW=500']
    elif value == 'I':
        return ['WINDOW=500'], ['WINDOW=1000']
    elif value == 'J':
        return ['WINDOW=1000'], ['End']
    else:
        print('Error')
        sys.exit()
          
def findMeasurement(value):
    #time,zori,xyori,zwong,zcsn,xywong,xycsn
    if value == 'A':
        return 1
    elif value == 'B':
        return 2
    elif value == 'C':
        return 3
    elif value == 'D':
        return 5
    elif value == 'E':
        return 4
    elif value == 'F':
        return 6
    else:
        print('Error')
        sys.exit()


def getCharacterType():
    character = raw_input()[0]
    if character in [ 'A','B', 'C', 'D', 'E', 'F']:
        print('Data Type Set')
        return character
    else:
        print('Invalid Input')
        return getCharacterType()

def getCharacterMeasurement():
    character = raw_input()[0]
    if character in [ 'A','B', 'C', 'D', 'E', 'F']:
        print('Measurement Type Set')
        return character
    else:
        print('Invalid Input')
        return getCharacterMeasurement()
          
def getCharacterWindow():
    character = raw_input()[0]
    if character in [ 'A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']:
        print('WindowLength Set')
        return character
    else:
        print('Invalid Input')
        return getCharacterWindow()
    

def animate(time1,value1,time2,value2):
    a = reduce(lambda x, y: x + y, value1) / len(value1)
    b = reduce(lambda x, y: x + y, value2) / len(value2)
    valueA = [x/a for x in value1]
    valueB = [x/b for x in value2]
    a = time1[0]
    b = time2[0]
    time1 = [x - a for x in time1]
    time2 = [x - a for x in time2]

    ax1.plot(time1,valueA,'b',time2, valueB,'g')
    





#BEGIN


fig1 = plt.figure()
ax1 = fig1.add_subplot(1,1,1)
ax1.clear()




print('This program will display two data sets')

specifyIntensity('First')
typeA = getCharacterType()
firstfilename = findFile(typeA)

specifyIntensity('Second')
typeB = getCharacterType()
secondfilename = findFile(typeB)

specifyWindow('First')
windowA = getCharacterWindow()
firstrowbegin, firstrowend = findWindow(windowA)
specifyWindow('Second')
windowB = getCharacterWindow()
secondrowbegin, secondrowend = findWindow(windowB)

specifyMeasurement('First')
measurementA = getCharacterMeasurement()
firstmeasurement = findMeasurement(measurementA)
specifyMeasurement('Second')
measurementB = getCharacterMeasurement()
secondmeasurement = findMeasurement(measurementB)

time1,value1 = findDataSet(firstfilename, firstrowbegin, firstrowend, firstmeasurement)
time2,value2 = findDataSet(secondfilename, secondrowbegin, secondrowend, secondmeasurement)

animate(time1,value1,time2,value2)

plt.show()
