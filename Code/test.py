#! /usr/bin/python

"""
receive_samples.py
By Paul Malmsten, 2010
pmalmsten@gmail.com
This example continuously reads the serial port and processes IO data
received from a remote XBee.
"""

#from xbee import XBee
import XBeeAPI as XBee
import serial
import time
import random as rand

PORT = '/dev/ttyO2'
BAUD_RATE = 9600

# Open serial port
#ser = serial.Serial(PORT, BAUD_RATE)

# Create API object
#xbee = XBee(ser)

xbee = XBee.XBee('/dev/ttyO2')

# Continuously read and print packets
while True:
    try:
	print "Ready..."
	#xbee.remote_at(dest_addr_long=, command='D1', frame_id='A')
	#response = xbee.wait_read_frame()
	#print(response)
	td = rand.randrange(0, 1000, 1)
    	temp = rand.randrange(0, 65, 1)
    	press = rand.randrange(0, 1000, 1)
    	alt = rand.randrange(0,6000, 1)

    	acclx = round(rand.random() * 16, 2)
    	accly = round(rand.random() * 16, 2)
    	acclz = round(rand.random() * 16, 2)

    	gpsLN = "44 33' 38.214\" N"
    	gpsLA = "123 16' 24.582\" W"

    	msg = str(td)+";"+str(temp)+";"+str(press)+";"+str(alt)+";"+str(acclx)+";"+str(accly)+";"+str(acclx)+";"+gpsLN+";"+gpsLA+";"

    	#print(data)
    	time.sleep(0.25)
	#xbee.tx(dest_addr='\x00\x00', data=msg)
	#xbee.tx_long_addr(dest_addr='\x00\x13\xA2\x00\x41\x03\x50\xA9', data=msg)
	addr = 0x0013A200410350A9
    	#msg = sensorData
    	sent = xbee.SendStr(msg, addr)
	#xbee.tx(dest_addr='\x50\xA9', data=msg)
	#xbee.send("at", frame='A', command='MY')
	time.sleep(1)
	#print response
    except KeyboardInterrupt:
        break
        
#sser.close()
