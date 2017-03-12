# !/usr/bin/python3
import threading
import time
from xbee import XBee
import serial
import serial.tools.list_ports
import threads

exitFalg = 0

def sendData(data):
    pass


class xb_rcv_thread(threading.Thread):
    def __init__(self, threadID, name, counter, q, port):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.port = port
        self.serial = init(self)
        self.xbee = XBee(ser, callback=processMessage)

    def run(self):
        print("Starting " + self.name)
        listen(self)
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

    def processMessage(data):
        print(data)

