import os
import sys
import time
import smbus
import subprocess

from datetime import datetime

from gps import *

# Delay start by 15 seconds
time.sleep(1)



gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE)


while True:

    GPSLat = 0.0
    GPSLong = 0.0
    GPSTime = "00:00:00"
    GPSAlt = 000
    GPSMode = 0

# Get timestamp
    CurrTimestamp = datetime.now()
#    print(f"CurrTimestamp = {CurrTimestamp}")
    report = gpsd.next()
#    print(report['class'])




    if report['class'] == 'TPV':
           GPSTime = getattr(report,'time','')
           GPSLat = getattr(report,'lat',0.0)
           GPSLong = getattr(report,'lon',0.0)
           GPSAlt = getattr(report,'alt','nan')
           GPSMode = getattr(report,'mode','nan')
   
           print("System Time: ", CurrTimestamp)
           print ("GPS Time: ", GPSTime)
           print ("Lat: ", GPSLat)
           print ("Long: ", GPSLong)
           print ("Altitude: ", GPSAlt)
           print ("GPSMode: ",GPSMode)
           print ()


    time.sleep(1)
