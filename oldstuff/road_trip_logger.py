#!/usr/bin/python3

import os, sys
import serial
import time
import datetime
import geopy.distance
import FetchGPS


time_now  = datetime.datetime.now().strftime('%m_%d_%Y_%H_%M_%S') 

print(time_now)


with open('logged_gps_' + time_now + '.csv', 'w') as logged_gps:

   logged_gps.write("GPS_Time,Lat,Long,Altitude,GPSMode\n")


   while True:

      logged_gps.write(f"{FetchGPS.GPSTime},{FetchGPS.GPSLat},{FetchGPS.GPSLong},{FetchGPS.GPSAlt},{FetchGPS.GPSMode}\n")

      print (f"GPS Time = {FetchGPS.GPSTime}")
      print (f"FetchGPS.GPSLat = {FetchGPS.GPSLat}")
      print (f"FetchGPS.GPSLong = {FetchGPS.GPSLong}")
      print (f"FetchGPS.GPSAlt = {FetchGPS.GPSAlt}")
      print (f"GPSMode =  {FetchGPS.GPSMode}")
      print()

      time.sleep(1)



      
 
#        print("System Time: ", CurrTimestamp)
#        print ("Lat: ", GPSLat)
#        print ("Long: ", GPSLong)
#        print ("GPS Time: ", GPSTime)
#        print ("Altitude: ", GPSAlt)
#        print ("GPSMode: ",GPSMode)
#        print ()
#
#        logged_gps.write (CurrTimestamp, GPSTime, GPSLat, GPSLong, GPSAlt, GPSMode, "\n")

