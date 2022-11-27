#!/usr/bin/python3

import os, sys
import serial
import time
import datetime
import geopy.distance
from gps import *


time.sleep(1)

gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE)

time_now  = datetime.datetime.now().strftime('%m_%d_%Y_%H_%M_%S') 
print(time_now)

#adler_lat = 31.88287429
#adler_long = -81.63445874

#ser = serial.Serial('/dev/ttyUSB0',19200, timeout = 5)
ser = serial.Serial('/dev/ttyUSB0', 9600, 8, 'N', 1, timeout=20)

with open('IncomingData_' + time_now + '.csv', 'a') as IncomingData,\
open('OutgoingData_' + time_now + '.csv', 'a') as OutgoingData:

   # listen for the input, exit if nothing received in timeout period


   while True:
      line = ser.readline()
   
      if len(line) == 0:
         print("No Incoming Serial Data Exit.\n")
         sys.exit()
   
      # the decode is explained here:
      # https://stackoverflow.com/questions/41918836/how-do-i-get-rid-of-the-b-prefix-in-a-string-in-python
   
      # UnicodeDecodeError: 'utf-8' codec can't decode byte 0x96 in position 57: invalid start byte
      # seen error from line below:
      # print(f"line = {line}")
      try:
         dline = line.decode('utf-8')
       
      except:
         print("******************************** An exception occurred ************************************")
         print(line)
         print("********************************************************************************************\n")
      IncomingData.write(dline)

      spline = dline.split(',')
      #print(spline[0], spline[1], spline[2])

      OutgoingData.write(f"Target cooridinates: {spline[0]}, {spline[1]}, {spline[2]}\n")
      print(f"Target cooridinates: {spline[0]}, {spline[1]}, {spline[2]}")

      #report = gpsd.next()
      #print(report['class'])
    
      while True:
         report = gpsd.next()
         #print(report['class'])
         if report['class'] == 'TPV':
           GPSTime = getattr(report,'time','')
           GPSLat = getattr(report,'lat',0.0)
           GPSLong = getattr(report,'lon',0.0)
           GPSAlt = getattr(report,'alt','nan')
           GPSMode = getattr(report,'mode','nan')
   
           break


      OutgoingData.write(f"Local cooridinates: {GPSTime}, {GPSLat}, {GPSLong}, {GPSAlt}\n")
      print(f"Local cooridinates: {GPSTime}, {GPSLat}, {GPSLong}, {GPSAlt}")

      coords_1 = (spline[1], spline[2])
      coords_2 = (GPSLat, GPSLong)

      try:
         miles  = geopy.distance.geodesic(coords_1, coords_2).miles
      except:
         print("******************************** An exception occurred ************************************")
         print("ValueError('Latitude must be in the [-90; 90] range.'")
         print("********************************************************************************************\n")

      OutgoingData.write(f"miles = {miles}\n")
      print(f"miles = {miles}")
      OutgoingData.write("\n")
      print()
      
      ser.flushInput()

ser.close()             # close port
