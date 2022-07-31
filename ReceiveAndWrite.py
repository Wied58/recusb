import serial
import sys

InComm = serial.Serial(sys.argv[1], 9600)
InComm.flushInput()
InComm.flushOutput()

while True:
    ReceivedLine=str(InComm.readline())
    with open('IncomingData.csv', 'a') as IncomingData:
        #IncomingData.write(ReceivedLine[2:][:-3] + "\n")
        IncomingData.write(ReceivedLine + "\n")
    #print(ReceivedLine[2:][:-3])
    print(ReceivedLine)
    IncomingData.close()

