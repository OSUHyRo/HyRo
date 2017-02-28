# !/usr/bin/python3
import threading
import time
from xbee import XBee
import serial
import serial.tools.list_ports

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
        self.serial = self.init()
        self.xbee = XBee(self.serial, callback=self.processMessage)
        self.q = q

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
        #print(data["rf_data"])
        self.q.put(item=data["rf_data"], block=False)

