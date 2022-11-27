#!/usr/bin/python3

import os, sys
import serial
import time
import datetime

time_now  = datetime.datetime.now().strftime('%m_%d_%Y_%H_%M_%S') 

adler_lat = "41d 51m 59s N"
adler_long = "87d 26m 28s W"
print(time_now)

#ser = serial.Serial('/dev/ttyUSB0',19200, timeout = 5)
ser = serial.Serial('/dev/ttyUSB0', 9600, 8, 'N', 1, timeout=20)

with open('IncomingData_' + time_now + '.csv', 'a') as IncomingData:

   # listen for the input, exit if nothing received in timeout period
   while True:
      line = ser.readline()
   
      if len(line) == 0:
         print("Time out! Exit.\n")
         sys.exit()
   
      # the decode is explained here:
      # https://stackoverflow.com/questions/41918836/how-do-i-get-rid-of-the-b-prefix-in-a-string-in-python
   
      dline = line.decode('utf-8')
   
      print (dline, end ='')
      IncomingData.write(dline)

      spline = dline.split(',')
      print(spline[0])


