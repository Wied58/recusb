#! /bin/sh
cd /home/pi/
sleep 30
python3 ReceiveAndWrite.py /dev/ttyUSB0 &

