# !/usr/bin/python3
from tkinter import *
from tkinter import messagebox
from math import *
import tkinter as tk
from tkinter import Tk
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import image
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from xbee_threads import *
import time
from queue import Queue
from PIL import ImageTk,Image

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
hyroGUI.geometry("1500x800")

Back = Canvas(hyroGUI, bg="blue", height=800, width=1500)
backgroundFile = PhotoImage(file = "background.gif")
background_label = Label(hyroGUI, image=backgroundFile)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
Back.pack()

armButtonImage = PhotoImage(file="armButtonImage.gif")
disarmButtonImage = PhotoImage(file="disarmButtonImage.gif")
fillButtonImage = PhotoImage(file="fillButtonImage.gif")
ignitionButtonImage = PhotoImage(file="ignitionButtonImage.gif")
abortButtonImage = PhotoImage(file="abortButtonImage.gif")
launchButtonImage = PhotoImage(file="launchButtonImage.gif")
gaugeImage = PhotoImage(file="gaugeBackgroundImage.gif")

armButton = Button(hyroGUI, command = lambda: proccessCommand("Arm"))
disarmButton = Button(hyroGUI, command = lambda: proccessCommand("Disarm"))
fillButton = Button(hyroGUI, command = lambda: proccessCommand("Fill"))
ignitionButton = Button(hyroGUI, command = lambda: proccessCommand("Ignition"))
abortButton = Button(hyroGUI, command = lambda: proccessCommand("Abort"))
launchButton = Button(hyroGUI, command = lambda: proccessCommand("Launch"))

armButton.config(image=armButtonImage, width="125", height="50", bg="gray", bd=0, relief=SUNKEN, overrelief=RAISED)
disarmButton.config(image=disarmButtonImage, width="125", height="50", bg="gray", bd=0, relief=SUNKEN, overrelief=RAISED)
fillButton.config(image=fillButtonImage, width="125", height="50", bg="gray", bd=0, relief=SUNKEN, overrelief=RAISED)
ignitionButton.config(image=ignitionButtonImage, width="125", height="50", bg="gray", bd=0, relief=SUNKEN, overrelief=RAISED)
abortButton.config(image=abortButtonImage, width="125", height="50", bg="gray", bd=0, relief=SUNKEN, overrelief=RAISED)
launchButton.config(image=launchButtonImage, width="125", height="50", bg="gray", bd=0, relief=SUNKEN, overrelief=RAISED)

chamberPressure = drawGuage(mainwindow=hyroGUI, x=350, y=125, h=150, w=200, min=10 , max=100)
chamberTemp = drawGuage(mainwindow=hyroGUI, x=570, y=125, h=150, w=200, min=10, max=100)
altitude = drawGuage(mainwindow=hyroGUI, x=790, y=125, h=150, w=200, min=10 , max=100)

acceleration = drawPlot(mainwindow=hyroGUI, x=400, y=330, h=1.75, w=2.5)
velocity = drawPlot(mainwindow=hyroGUI, x=700, y=330, h=1.75, w=2.5)
chamberPressureGraph = drawPlot(mainwindow=hyroGUI, x=350, y=575, h=1.75, w=2.5)
chamberTempGraph = drawPlot(mainwindow=hyroGUI, x=650, y=575, h=1.75, w=2.5)
altitudeGraph = drawPlot(mainwindow=hyroGUI, x=950, y=575, h=1.75, w=2.5)

chamberPressureGraph.putScreen()
chamberTempGraph.putScreen()
altitudeGraph.putScreen()


chamberTemp.putScreen()
chamberTemp.reDraw(value=30)
altitude.putScreen()


chamberPressure.putScreen()
chamberTemp.putScreen()
altitude.reDraw(value=50)

acceleration.putScreen()
velocity.putScreen()

armButton.place(x=50, y=50)
disarmButton.place(x=50, y=100)
fillButton.place(x=50, y=150)
ignitionButton.place(x=50, y=200)
abortButton.place(x=50, y=250)
launchButton.place(x=50,y=300)

qu = Queue()
# Create new threads
# xbee_thread = xb_rcv_thread(1, "Xbee-Thread", 1, q=qu, port="COM4")


# Start new Threads
# xbee_thread.start()

#hyroGUI.mainloop()
c = 0
while True:
    if(c > 100):
        c = 0
    c += 1
    chamberPressure.reDraw(value=c)
    hyroGUI.update_idletasks()
    hyroGUI.update()
    time.sleep(0.5)
    if (qu.empty()):
        pass
    else:
        data = qu.get(False)  
        # If `False`, the program is not blocked. `Queue.Empty` is thrown if 
        # the queue is empty
        print(data)
        qu.task_done()
  
    #item = qu.get(block=False)
    #print(item)
    #qu.task_done()

qu.join()
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

