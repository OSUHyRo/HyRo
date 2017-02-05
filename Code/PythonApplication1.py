# !/usr/bin/python3
from tkinter import *
from tkinter import messagebox
from math import *
import tkinter as tk
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import time
from xbee import XBee
import serial
import serial.tools.list_ports

class drawCanvas:
        def __init__(self, mainwindow, x, y, w, h):
            self.x = x
            self.y = y
            self.window = mainwindow
            self.width = w
            self.height = h
            self.canvas = Canvas(hyroGUI, width=w, height=h)
            self.canvas.config(background='white')

        def putScreen(self):
            self.canvas.place(x = self.x, y = self.y)

        def redraw(self):
            self.canvas.create_line(0, 0, 200, 100)
            self.canvas.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))

            self.canvas.create_rectangle(50, 25, 150, 75, fill="blue")

class drawPlot:
        def __init__(self, mainwindow, x, y, w, h):
            self.x = x
            self.y = y
            self.window = mainwindow
            self.width = w
            self.height = h

            f = Figure(figsize=(self.width,self.height), dpi=100)
            a = f.add_subplot(111)
            a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,5,5,5,5])

        

            self.canvas = FigureCanvasTkAgg(f, master=mainwindow)
            self.canvas.show()

        def putScreen(self):
            self.canvas.get_tk_widget().place(x = self.x, y = self.y)
           

       # def redraw(self):
            #self.canvas.create_line(0, 0, 200, 100)
            #self.canvas.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))

            #self.canvas.create_rectangle(50, 25, 150, 75, fill="blue")

class drawGuage(drawCanvas):
    def __init__(self, min, max, *args, **kwargs):
        self.min = min
        self.max = max
        super(drawGuage, self).__init__(*args, **kwargs)

    def reDraw(self, value):
        #self.canvas.create_line(0, 0, 200, 100)
        self.canvas.delete("all")
        scale = self.max - self.min
        r = pi
        p = pi + (pi * (value / scale))
        count = 0
        while r <= 2 * pi:
            xpos = 100*cos(r) + self.width / 2
            #print("x")
            #print(xpos)
            ypos = 100*sin(r) + self.height
            #print("y")
            #print(ypos)
            if(count % 2 == 0):
                self.canvas.create_line(75*cos(r) + self.width / 2, 75*sin(r) + self.height, xpos, ypos, width = 4)
            else:
                self.canvas.create_line(75*cos(r) + self.width / 2, 75*sin(r) + self.height, xpos, ypos, width = 1)
            count += 1
            r += (pi / 2) / 10
        self.canvas.create_line(self.width / 2, self.height, 95*cos(p) + self.width / 2, 95*sin(p) + self.height, width = 4, fill="red");

class drawGrpah(drawCanvas):
    def reDraw(self):
        self.canvas.create_line(0, 0, 200, 100)

class drawMultiGraph(drawCanvas):
    def reDraw(self):
        self.canvas.create_line(0, 0, 200, 100)
    

hyroGUI = Tk()
hyroGUI.geometry("1000x1000")
def proccessCommand(command):
   msg=messagebox.showinfo( "Command You Clicked", command)

armButton = Button(hyroGUI, text ="Arm", command = lambda: proccessCommand("Arm"))
disarmButton = Button(hyroGUI, text ="Disarm", command = lambda: proccessCommand("Disarm"))
fillButton = Button(hyroGUI, text ="Fill", command = lambda: proccessCommand("Fill"))
ignButton = Button(hyroGUI, text ="Ignition", command = lambda: proccessCommand("Ignition"))
abortButton = Button(hyroGUI, text ="Abort", command = lambda: proccessCommand("Abort"))
launchButton = Button(hyroGUI, text ="Luanch", command = lambda: proccessCommand("Launch"))

tankPressure = drawGuage(mainwindow=hyroGUI, x=200, y=25, h=150, w=200, min=10 , max=100)
temperature = drawGuage(mainwindow=hyroGUI, x=450, y=25, h=150, w=200, min=10 , max=100)
chamberPressure = drawGuage(mainwindow=hyroGUI, x=700, y=25, h=150, w=200, min=10, max=100)

acceleration = drawPlot(mainwindow=hyroGUI, x=200, y=400, h=2, w=3)
velocity = drawPlot(mainwindow=hyroGUI, x=400, y=400, h=2, w=3)


temperature.putScreen()
temperature.reDraw(value=30)

tankPressure.putScreen()
chamberPressure.putScreen()
chamberPressure.reDraw(value=50)

acceleration.putScreen()
velocity.putScreen()

armButton.place(x=50, y=50)
disarmButton.place(x=50, y=100)
fillButton.place(x=50, y=150)
ignButton.place(x=50, y=200)
abortButton.place(x=50, y=250)
launchButton.place(x=50,y=300)

#hyroGUI.mainloop()
c = 0
#while True:
#    if(c > 100):
#        c = 0
#   c += 1
#    tankPressure.reDraw(value=c)
#    hyroGUI.update_idletasks()
#    hyroGUI.update()
#    time.sleep(0.5)

#portfound = False
#ports = list(serial.tools.list_ports.comports())
#for p in ports:
    # The SparkFun XBee Explorer USB board uses an FTDI chip as USB interface
#    if "FTDIBUS" in p[2]:
#        print("Found possible XBee on " + p[0])
#        if not portfound:
#            portfound = True
#            portname = p[0]
#            print("Using " + p[0] + " as XBee COM port.")
#        else:
#            print("Ignoring this port, using the first one that was found.")
 
#if portfound:
#    ser = serial.Serial(portname, 9600)
#else:
#    sys.exit("No serial port seems to have an XBee connected.")

try:
    
    # Open serial port
    print("opening comm")
    ser = serial.Serial('COM4', 9600)
    print("Successful")
    # Create XBee Series 1 object
    xbee = XBee(ser)
        
    # Send the string 'Hello World' to the module with MY set to 1
    xbee.tx(dest_addr=b'\x00\x00', data=b'Hello World')

except KeyboardInterrupt:
    pass
finally:
    ser.close()