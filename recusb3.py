import os, sys
import serial
import time

#ser = serial.Serial('/dev/ttyUSB0',19200, timeout = 5)
ser = serial.Serial('/dev/ttyUSB0', 9600, 8, 'N', 1, timeout=10)

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
   spline = dline.split(',')
   print(spline[0])


