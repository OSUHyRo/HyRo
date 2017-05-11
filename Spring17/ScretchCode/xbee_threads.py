# !/usr/bin/python3
import threading
import time
from xbee import XBee
import serial
import serial.tools.list_ports

coneSep = 0
secDeployed = 0

class xb_rcv_thread(threading.Thread):
    #Initializes all self variables, including the queues this thread needs to access
    def __init__(self, threadID, name, counter, timeStamp, chamberTemp, chamberPres, altitude, accelX, accelY, accelZ, GPSLon, GPSLat, port, sQue):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.port = port
        self.serial = self.init()
        self.xbee = XBee(self.serial, callback=self.processMessage) #sets serial port and call back functino for recieved messages
        self.chamberTemp = chamberTemp
        self.chamberPres = chamberPres
        self.timeStamp = timeStamp
        self.altitude = altitude
        self.accelX = accelX
        self.accelY = accelY
        self.accelZ = accelZ
        self.GPSLon = GPSLon
        self.GPSLat = GPSLat
        self.sendQue = sQue
        self.exit = 0
    
    #The main thread of execution for this thread, calls listen 
    def run(self):
        print("Starting " + self.name)
        #self.xbee.tx(dest_addr=b'\x00\x01', data=b'Hello World')
        self.listen()
        print("Exiting " + self.name)

    #initialization function for thread, opens up serial port for communication to the XBee
    def init(self):
        try:
            # Open serial port
            print("opening comm")
            return serial.Serial(self.port, 9600)
       
        except KeyboardInterrupt:
            pass
    
    #Called when thread is closed, stops the xbee, cloes the serial port and sets the exit flag.
    def end(self):
        self.xbee.halt()
        self.serial.close()
        #set exit flag
        self.exit = 1

    #Our imposed main thread process, checks if exit is set and then returns to exit thread if it is set. 
    #Also calls send() to send any commands in the send queue then sleeps briefly and repeats
    #This while loop keeps the thread alive
    def listen(self):
        while 1:
            #exit thread if flag is set
            if(self.exit == 1):
                    return
            self.send()
            time.sleep(0.001)

    #This is the call back function for the XBee API. When a messesage is revieced on the XBee this message 
    #parses the data and puts it into the respected shared queues
    def processMessage(self, data):
        global secDeployed
        global coneSep
        print("New Message")
        # print(data)
       
        dataStr = data["rf_data"].decode("utf-8").split(';')
        #print(dataStr)
        if(len(dataStr) == 9):
            #After expo we are going to add a recieve block for the parachute deployment, this was just requested 
            self.timeStamp.put(dataStr[0], block=False)
            self.chamberTemp.put(dataStr[1], block=False)
            self.chamberPres.put(dataStr[2], block=False)
            self.altitude.put(dataStr[3], block=False)
            self.accelX.put(dataStr[4], block=False)
            self.accelY.put(dataStr[5], block=False)
            self.accelZ.put(dataStr[6], block=False)
            self.GPSLon.put(dataStr[7], block=False)
            self.GPSLat.put(dataStr[8], block=False)
        elif(dataStr[2] == "SECONDARY PARACHUTE DEPLOYED\r"):
            print("Secondary Parachute Deployed")
            secDeployed = 1
            print(secDeployed)
        elif(dataStr[3] == "NOSECONE SEPARATED\r"):
            print("Nose Cone Seperated")
            coneSep = 1
            print(coneSep)
        elif(dataStr[2] == "CONFIRMATION"):
            print("got confirmation")
            #do stuff


    #Checks the message que for the fill command. If detected sends fill to the other radio transciever.
    def send(self):
        #self.xbee.tx(dest_addr=b'\x00\x01', data=message)
        if(self.sendQue.empty()):
            pass
        else:
            self.sendQue.get(False)
     
            self.sendQue.task_done()
            print("Send Fill Message")
            #self.xbee.tx(dest_addr=b'\x00\x01', data=b'FILL') #Send message to the other Xbee
            self.xbee.tx_long_addr(dest_addr='\x00\x13\xA2\x00\x41\x5E\x0E\x52', data=b'$COMMAND13')

