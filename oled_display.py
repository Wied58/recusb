#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import time
from pathlib import Path
from datetime import datetime

import subprocess
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

#from gps import *

from demo_opts import get_device
from luma.core.render import canvas
from PIL import ImageFont


TimeFormat = "%H:%M:%S %d.%m"

# Setup GPSd client
#gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE)

# Setup Display
device = get_device()

# use custom font
font_path = str(Path(__file__).resolve().parent.joinpath('fonts', 'monospace.medium.ttf'))
font2 = ImageFont.truetype(font_path, 11)

#while True:
#    GPSLat = "0.00000"
#    GPSLong = "0.00000"
#    GPSTime = "0001-01-01T00:00:00Z"
#    GPSAlt = "000.0"
#
## Get timestamp
#    CurrTimestamp = datetime.now()
#    CurrTimestamp = CurrTimestamp.strftime(TimeFormat)
#    CurrTimestamp = str(CurrTimestamp)
#
#
## Get GPS Info
##    report = gpsd.next()
##    if report['class'] == 'TPV':
##        GPSLat = getattr(report,'lat',0.00000)
##        GPSLong = getattr(report,'lon',0.00000)
##        GPSTime = getattr(report,'time',"0001-01-01T00:00:00Z")
##        GPSAlt = getattr(report,'alt','000.0')
#
#
# Fix GPS Time Formatting
# python ISO standard time parser does not support "Z" (zulu) notation in ISO8601, which is what GPSd provides,
# but only time zone notation "+00:00". Using string replace to fix that
# next two lines extract ISO time into python datetime variable type and then format it into same timestamp as system time above
    GPSTime = GPSTime.replace("Z", "+00:00")
    StdGPSTime = datetime.fromisoformat(GPSTime)
    GPSTime = StdGPSTime.strftime(TimeFormat)
    GPSTime = str(GPSTime)

## Get IP
#    cmd = "hostname -I"
#    IP = subprocess.check_output(cmd, shell = True)
#    IP = IP.decode('ASCII')
#
## Get SSID
#    cmd = "iwgetid wlan0 -r"
#    try:
#        SSID = subprocess.check_output(cmd, shell = True)
#        SSID = SSID.decode('ASCII')
#    except Exception:
#        pass

## Dispaly first Screen
#    with canvas(device) as draw:
#        draw.text((0, 0),"IP: " + IP, font=font2, fill="white")
#        draw.text((0, 11),"SSID: " + SSID, font=font2, fill="white")
#        draw.text((0, 22),"LOC: " + GPSLat + ", " + GPSLong, font=font2, fill="white")
#    time.sleep(4)
#
## After 4 seconds dispaly second screen
#    with canvas(device) as draw:
#        draw.text((0, 0),"SYS: " + CurrTimestamp, font=font2, fill="white")
#        draw.text((0, 11),"GPS: " + GPSTime, font=font2, fill="white")
#        draw.text((0, 22),"ALT: " + GPSAlt + "m", font=font2, fill="white")
#    time.sleep(4)

