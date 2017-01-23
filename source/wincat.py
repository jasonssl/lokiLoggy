import threading
import os
import time
import ImageGrab
import win32api

lastInTime = 0

def currentActiveTime():
    return win32api.GetLastInputInfo()

def updateLastTime():
    global lastInTime
    lastInTime = currentActiveTime()
    activeGrabber()

def activeGrabber():
    threading.Timer(900, activeGrabber).start()
    screenGrab()

def screenGrab():
    global lastInTime
    t = currentActiveTime()
    if t != lastInTime:
        lastInTime = t
        print 'Taking screenshot...'
        img = ImageGrab.grab()

        if not os.path.exists('C:\\Windows\\Temp\\win32log\\snapshots'):
            os.makedirs('C:\\Windows\\Temp\\\win32log\\snapshots')

        img.save('C:\\Windows\\Temp\\win32log\\snapshots\\full_snap_' + str(int(time.time())) + '.png', 'PNG')
