# !/usr/bin/python3
import threading
import time
from xbee import XBee
import serial
import serial.tools.list_ports
#import threads

exitFalg = 0

def sendData(data):
    pass


class xb_rcv_thread(threading.Thread):
    def __init__(self, threadID, name, counter, timeStamp, chamberTemp, chamberPres, altitude, accelX, accelY, accelZ, GPSLon, GPSLat, port):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.port = port
        self.serial = self.init()
        self.xbee = XBee(self.serial, callback=self.processMessage)
        self.chamberTemp = chamberTemp
        self.chamberPres = chamberPres
        self.timeStamp = timeStamp
        self.altitude = altitude
        self.accelX = accelX
        self.accelY = accelY
        self.accelZ = accelZ
        self.GPSLon = GPSLon
        self.GPSLat = GPSLat
         
    def run(self):
        print("Starting " + self.name)
        #self.xbee.tx(dest_addr=b'\x00\x01', data=b'Hello World')
        self.listen()
        print("Exiting " + self.name)

    def init(self):
        try:
            # Open serial port
            print("opening comm")
            #ser = serial.Serial('COM4', 9600)
            return serial.Serial(self.port, 9600)

            # Send the string 'Hello World' to the module with MY set to 1
            #xbee.tx(dest_addr=b'\x00\x01', data=b'Hello World')
       
        except KeyboardInterrupt:
            pass

    def end(self):
        self.xbee.halt()
        self.ser.close()

    def listen(self):
        while 1:
            time.sleep(0.001)

    def processMessage(self, data):
        print("San Check")
        dataStr = data["rf_data"].decode("utf-8").split(';')

        #what if we dont get values? Need to test and adjust for that
        self.timeStamp.put(dataStr[0], block=False)
        self.chamberTemp.put(dataStr[1], block=False)
        self.chamberPres.put(dataStr[2], block=False)
        self.altitude.put(dataStr[3], block=False)
        self.accelX.put(dataStr[4], block=False)
        self.accelY.put(dataStr[5], block=False)
        self.accelZ.put(dataStr[6], block=False)
        self.GPSLon.put(dataStr[7], block=False)
        self.GPSLat.put(dataStr[8], block=False)

