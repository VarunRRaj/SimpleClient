#!/usr/bin/env python

"""Copyright 2010 Phidgets Inc.
This work is licensed under the Creative Commons Attribution 2.5 Canada License.
To view a copy of this license, visit http://creativecommons.org/licenses/by/2.5/ca/

Modified by Varun Raj and Sanket More for SCALE
"""

__author__ = 'Adam Stelmack'
__version__ = '2.1.8'
__date__ = 'May 17 2010'

#Basic imports
from ctypes import *
import sys
#Phidget specific imports
from Phidgets.Phidget import Phidget
from Phidgets.PhidgetException import PhidgetErrorCodes, PhidgetException
from Phidgets.Events.Events import SpatialDataEventArgs, AttachEventArgs, DetachEventArgs, ErrorEventArgs
from Phidgets.Devices.Spatial import Spatial, SpatialEventData, TimeSpan

#SimpleClient imports
import time
import csnpicker
import picker
import orienter
import logger

ori = orienter.Orienter()

zCSNPicker = csnpicker.Picker('z', 1, 0)
xyCSNPicker = csnpicker.Picker('xy', 1, 0)
zPicker = picker.Picker('z',1,0)
xyPicker = picker.Picker('xy',1,0)

#Create an accelerometer object
try:
    spatial = Spatial()
except RuntimeError as e:
    print("Runtime Exception: %s" % e.details)
    print("Exiting....")
    exit(1)

#Event Handler Callback Functions
def SpatialAttached(e):
    attached = e.device
    spatial.setDataRate(4)

def SpatialDetached(e):
    detached = e.device

def SpatialError(e):
    try:
        source = e.device
    except PhidgetException as e:
        print("Phidget Exception %i: %s" % (e.code, e.details))

def SpatialData(e):
    source = e.device
    for index, spatialData in enumerate(e.spatialData):
        if len(spatialData.Acceleration) > 0:
            addToLine(spatialData.Acceleration)
            #oriented = ori.orient(spatialData.Acceleration)

            #zPicker.add([oriented[0], oriented[2]])
            #zCSNPicker.add([oriented[0],oriented[2]])
            #xyPicker.add([oriented[1], oriented[2]])
            #xyCSNPicker.add([oriented[1],oriented[2]])

            logger.addLine()

def collect(zWindow, zThreshold, xyWindow, xyThreshold):
    """Collects data"""

    print('TEST BEGIN')

    global zPicker, xyPicker, zCSNPicker, xyCSNPicker

    zPicker = picker.Picker('z', zWindow, zThreshold)
    zCSNPicker = csnpicker.Picker('z',zWindow,zThreshold)
    xyPicker = picker.Picker('xy', xyWindow, xyThreshold)
    xyCSNPicker = csnpicker.Picker('xy', xyWindow, xyThreshold)

    #Main Program Code
    try:
        spatial.setOnAttachHandler(SpatialAttached)
        spatial.setOnDetachHandler(SpatialDetached)
        spatial.setOnErrorhandler(SpatialError)
        spatial.setOnSpatialDataHandler(SpatialData)
    except PhidgetException as e:
        print("Phidget Exception %i: %s" % (e.code, e.details))
        print("Exiting....")
        exit(1)

    try:
        spatial.openPhidget()
    except PhidgetException as e:
        print("Phidget Exception %i: %s" % (e.code, e.details))
        print("Exiting....")
        exit(1)

    try:
        spatial.waitForAttach(10000)
    except PhidgetException as e:
        print("Phidget Exception %i: %s" % (e.code, e.details))
        try:
            spatial.closePhidget()
        except PhidgetException as e:
            print("Phidget Exception %i: %s" % (e.code, e.details))
            print("Exiting....")
            exit(1)
        print("Exiting....")
        exit(1)

    time.sleep(300)
    #time.sleep(120)

    try:
        spatial.closePhidget()
    except PhidgetException as e:
        print("Phidget Exception %i: %s" % (e.code, e.details))
        print("Exiting....")
        exit(1)
    #exit(0)
