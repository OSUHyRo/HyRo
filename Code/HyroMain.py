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
import random
from scipy import integrate

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


class AdrawPlot:
        def __init__(self, mainwindow, x, y, w, h):
            self.x = x
            self.y = y
            self.window = mainwindow
            self.width = w
            self.height = h

            j = []
            k = []
            readFile = open('ASample.txt', 'r')
            sepFile = readFile.read().split('\n')
            readFile.close()
            
            if(len(sepFile) <= 1):
                pass

            else:
                for plotPair in sepFile:
                     if(plotPair == ""):
                        continue
                aAndB = plotPair.split(',')
                j.append(float(aAndB[0]))
                k.append(float(aAndB[1]))


            f = Figure(figsize=(self.width,self.height), dpi=100)
            accel = f.add_subplot(111)
            accel.plot(j,k)
            #a.plot([1,2,3,4],[1,7,8,9])

            self.canvas = FigureCanvasTkAgg(f, master=mainwindow)
            self.canvas.show()

        def reDraw(self):
            #self.canvas.create_line(0, 0, 200, 100)
          
            j = []
            k = []
            readFile = open('ASample.txt', 'r')
            sepFile = readFile.read().split('\n')
            readFile.close()
           

            if(len(sepFile) <= 1):
                pass

            else:
                for plotPair in sepFile:
                    if(plotPair == ""):
                        continue
                    aAndB = plotPair.split(',')
                    j.append(float(aAndB[0]))
                    k.append(float(aAndB[1]))


            f = Figure(figsize=(self.width,self.height), dpi=100)
            accel = f.add_subplot(111)
            accel.plot(j,k)
            self.canvas = FigureCanvasTkAgg(f, self.window)
            self.canvas.show()
            self.canvas.get_tk_widget().place(x = self.x, y = self.y)

        def putScreen(self):
            self.canvas.get_tk_widget().place(x = self.x, y = self.y)

class VdrawPlot:
        def __init__(self, mainwindow, x, y, w, h):
            self.x = x
            self.y = y
            self.window = mainwindow
            self.width = w
            self.height = h

            j = []
            k = []
            readFile = open('ASample.txt', 'r')
            sepFile = readFile.read().split('\n')
            readFile.close()
            
            if(len(sepFile) <= 1):
                pass

            else:
                for plotPair in sepFile:
                    if(plotPair == ""):
                        continue
                    aAndB = plotPair.split(',')
                    j.append(float(aAndB[0]))
                    k.append(float(aAndB[1]))


            f = Figure(figsize=(self.width,self.height), dpi=100)
            velo = f.add_subplot(111)
            velo.plot(j,k)

            self.canvas = FigureCanvasTkAgg(f, master=mainwindow)
            self.canvas.show()

        def reDraw(self):
            #self.canvas.create_line(0, 0, 200, 100)
          
            j = []
            k = []
            readFile = open('VSample.txt', 'r')
            sepFile = readFile.read().split('\n')
            readFile.close()
           

            if(len(sepFile) <= 1):
                pass

            else:
                for plotPair in sepFile:
                    if(plotPair == ""):
                        continue
                    aAndB = plotPair.split(',')
                    j.append(float(aAndB[0]))
                    k.append(float(aAndB[1]))


            f = Figure(figsize=(self.width,self.height), dpi=100)
            accel = f.add_subplot(111)
            accel.plot(j,k)
            self.canvas = FigureCanvasTkAgg(f, self.window)
            self.canvas.show()
            self.canvas.get_tk_widget().place(x = self.x, y = self.y)
        def putScreen(self):
            self.canvas.get_tk_widget().place(x = self.x, y = self.y)

class CPdrawPlot:
        def __init__(self, mainwindow, x, y, w, h):
            self.x = x
            self.y = y
            self.window = mainwindow
            self.width = w
            self.height = h

            j = []
            k = []
            readFile = open('CPSample.txt', 'r')
            sepFile = readFile.read().split('\n')
            readFile.close()
            
            if(len(sepFile) <= 1):
                pass

            else:
                for plotPair in sepFile:
                    if(plotPair == ""):
                        continue
                    aAndB = plotPair.split(',')
                    j.append(int(aAndB[0]))
                    k.append(int(aAndB[1]))


            f = Figure(figsize=(self.width,self.height), dpi=100)
            accel = f.add_subplot(111)
            accel.plot(j,k)

            self.canvas = FigureCanvasTkAgg(f, master=mainwindow)
            self.canvas.show()

        def reDraw(self):
            #self.canvas.create_line(0, 0, 200, 100)
          
            j = []
            k = []
            readFile = open('CPSample.txt', 'r')
            sepFile = readFile.read().split('\n')
            readFile.close()
           

            if(len(sepFile) <= 1):
                pass

            else:
                for plotPair in sepFile:
                    if(plotPair == ""):
                        continue
                    aAndB = plotPair.split(',')
                    j.append(int(aAndB[0]))
                    k.append(int(aAndB[1]))


            f = Figure(figsize=(self.width,self.height), dpi=100)
            accel = f.add_subplot(111)
            accel.plot(j,k)
            self.canvas = FigureCanvasTkAgg(f, self.window)
            self.canvas.show()
            self.canvas.get_tk_widget().place(x = self.x, y = self.y)

        def putScreen(self):
            self.canvas.get_tk_widget().place(x = self.x, y = self.y)

class CTdrawPlot:
        def __init__(self, mainwindow, x, y, w, h):
            self.x = x
            self.y = y
            self.window = mainwindow
            self.width = w
            self.height = h
            

            j = []
            k = []
            readFile = open('CTSample.txt', 'r')
            sepFile = readFile.read().split('\n')
            readFile.close()
            
            #if file is blank draw nothing
        
            if(len(sepFile) <= 1):
                pass

            else:
                for plotPair in sepFile:
                    if(plotPair == ""):
                        continue
                    aAndB = plotPair.split(',')
                    j.append(int(aAndB[0]))
                    k.append(int(aAndB[1]))


            f = Figure(figsize=(self.width,self.height), dpi=100)
            accel = f.add_subplot(111)
            accel.plot(j,k)

            self.canvas = FigureCanvasTkAgg(f, master=mainwindow)
            self.canvas.show()

        def reDraw(self):
            #self.canvas.create_line(0, 0, 200, 100)
          
            j = []
            k = []
            readFile = open('CTSample.txt', 'r')
            sepFile = readFile.read().split('\n')
            readFile.close()
           

            if(len(sepFile) <= 1):
                pass

            else:
                for plotPair in sepFile:
                    if(plotPair == ""):
                        continue
                    aAndB = plotPair.split(',')
                    j.append(int(aAndB[0]))
                    k.append(int(aAndB[1]))


            f = Figure(figsize=(self.width,self.height), dpi=100)
            accel = f.add_subplot(111)
            accel.plot(j,k)
            self.canvas = FigureCanvasTkAgg(f, self.window)
            self.canvas.show()
            self.canvas.get_tk_widget().place(x = self.x, y = self.y)

        def putScreen(self):
            self.canvas.get_tk_widget().place(x = self.x, y = self.y)

class AltdrawPlot:
        def __init__(self, mainwindow, x, y, w, h):
            self.x = x
            self.y = y
            self.window = mainwindow
            self.width = w
            self.height = h

            j = []
            k = []
            readFile = open('AltSample.txt', 'r')
            sepFile = readFile.read().split('\n')
            readFile.close()
            
            if(len(sepFile) <= 1):
                pass

            else:
                for plotPair in sepFile:
                    if(plotPair == ""):
                        continue
                    aAndB = plotPair.split(',')
                    j.append(int(aAndB[0]))
                    k.append(int(aAndB[1]))


            f = Figure(figsize=(self.width,self.height), dpi=100)
            accel = f.add_subplot(111)
            accel.plot(j,k)

            self.canvas = FigureCanvasTkAgg(f, master=mainwindow)
            self.canvas.show()

        def reDraw(self):
            #self.canvas.create_line(0, 0, 200, 100)
          
            j = []
            k = []
            readFile = open('AltSample.txt', 'r')
            sepFile = readFile.read().split('\n')
            readFile.close()
           

            if(len(sepFile) <= 1):
                pass

            else:
                for plotPair in sepFile:
                    if(plotPair == ""):
                        continue
                    aAndB = plotPair.split(',')
                    j.append(int(aAndB[0]))
                    k.append(int(aAndB[1]))


            f = Figure(figsize=(self.width,self.height), dpi=100)
            accel = f.add_subplot(111)
            accel.plot(j,k)
            self.canvas = FigureCanvasTkAgg(f, self.window)
            self.canvas.show()
            self.canvas.get_tk_widget().place(x = self.x, y = self.y)

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
        value = int(value)
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

class drawGraph(drawCanvas):
    def reDraw(self):
        self.canvas.create_line(0, 0, 200, 100)

class drawMultiGraph(drawCanvas):
    def reDraw(self):
        self.canvas.create_line(0, 0, 200, 100)
    

def convVel(value):
    j = []
    k = []
    readFile = open('ASample.txt', 'r')
    sepFile = readFile.read().split('\n')
    readFile.close()
           
    #need enough points to integrate
    if(len(sepFile) < 3):
        pass

    else:
        for plotPair in sepFile:
            if(plotPair == ""):
                continue
            aAndB = plotPair.split(',')
            j.append(float(aAndB[0]))
            k.append(float(aAndB[1]))
        data = integrate.simps(k, x=j)

        t = round(time.clock())
        file = open("VSample.txt", "a")
        file.write("\n")
        file.write(str(t)+","+str(data));
        file.close()
        print("Velocity: " + str(data))
        velocity.reDraw()

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

acceleration = AdrawPlot(mainwindow=hyroGUI, x=400, y=330, h=2, w=3.5)
velocity = VdrawPlot(mainwindow=hyroGUI, x=775, y=330, h=2, w=3.5)
#chamberPressureGraph = drawPlot(mainwindow=hyroGUI, x=300, y=575, h=2, w=3.5)
#chamberTempGraph = drawPlot(mainwindow=hyroGUI, x=675, y=575, h=2, w=3.5)
#altitudeGraph = drawPlot(mainwindow=hyroGUI, x=1050, y=575, h=2,w=3.5)
chamberPressureGraph = CPdrawPlot(mainwindow=hyroGUI, x=300, y=575, h=2, w=3.5)
chamberTempGraph = CTdrawPlot(mainwindow=hyroGUI, x=675, y=575, h=2, w=3.5)
altitudeGraph = AltdrawPlot(mainwindow=hyroGUI, x=1050, y=575, h=2, w=3.5)

chamberPressureGraph.putScreen()
chamberTempGraph.putScreen()
altitudeGraph.putScreen()


chamberTemp.putScreen()
#chamberTemp.reDraw(value=30)
altitude.putScreen()


chamberPressure.putScreen()
chamberTemp.putScreen()
#altitude.reDraw(value=50)

acceleration.putScreen()
velocity.putScreen()

armButton.place(x=50, y=50)
disarmButton.place(x=50, y=100)
fillButton.place(x=50, y=150)
ignitionButton.place(x=50, y=200)
abortButton.place(x=50, y=250)
launchButton.place(x=50,y=300)

#the ques for the data
qChamberTemp = Queue()
qChamberPressure = Queue()
qAltitude = Queue()
qAccelX = Queue()
qAccelY = Queue()
qAccelZ = Queue()
qGPSLong = Queue()
qGPSLat = Queue()
qTimeStamp = Queue()

# Create new threads
xbee_thread = xb_rcv_thread(1, "Xbee-Thread", 1,  timeStamp=qTimeStamp, chamberTemp=qChamberTemp, chamberPres=qChamberPressure, altitude=qAltitude, accelX=qAccelX, accelY=qAccelY, accelZ=qAccelZ, GPSLon=qGPSLong, GPSLat=qGPSLat, port="COM3")


# Start new Threads
xbee_thread.start()

file = open("CTSample.txt", "w")
file.truncate()
file.close()
file = open("CPSample.txt", "w")
file.truncate()
file.close()
file = open("AltSample.txt", "w")
file.truncate()
file.close()
file = open("ASample.txt", "w")
file.truncate()
file.close()
file = open("VSample.txt", "w")
file.truncate()
file.close()
#hyroGUI.mainloop()
CPvalue = 35
CTvalue = 50
AltValue = 0
while True:
    #if(CPvalue > 40):
        #CPvalue = 35
    #CPvalue += 1
    #chamberPressure.reDraw(value=CPvalue)
    #if(CTvalue > 60):
        #CTvalue = 50
    #CTvalue += 1
    #chamberTemp.reDraw(value=CTvalue)
    #if(AltValue > 85):
        #AltValue = 0
    #AltValue += 1
    #altitude.reDraw(value=AltValue)
    #acceleration.reDraw(random.randrange(0,100),random.randrange(0,100), 0, 100)

    time.sleep(0.5)
    if(qTimeStamp.empty()):
        pass
    else:
        data = qTimeStamp.get(False)
        print("Time Stampe: " + data)
        #convert, store in long term, and write to file with timestamp
        qTimeStamp.task_done()

    if (qChamberPressure.empty()):
        pass
    else:
        #data = qu.get(False)  
        # If `False`, the program is not blocked. `Queue.Empty` is thrown if 
        # the queue is empty
        #print(data)
        #qu.task_done()

        #go through queues and send data to coverter for long term storage
        data = qChamberPressure.get(False)

        print("Chamber Pressure: " + data)
        t = round(time.clock())
        file = open("CPSample.txt", "a")
        file.write("\n")
        file.write(str(t)+","+str(data));
        file.close()
        chamberPressureGraph.reDraw()
        chamberPressure.reDraw(value=data)
        #convert, store in long term, and write to file with timestamp
        qChamberPressure.task_done()

    if(qChamberTemp.empty()):
        pass
    else:
        data = qChamberTemp.get(False)
        t = round(time.clock())
        file = open("CTSample.txt", "a")
        file.write("\n")
        file.write(str(t)+","+str(data));
        file.close()
        print("Chamber Temperature: " + data)
        chamberTempGraph.reDraw()
        chamberTemp.reDraw(value=data)
        qChamberTemp.task_done()

    if(qAltitude.empty()):
        pass
    else:
        data = qAltitude.get(False)
        print("Altitude: " + data)

        t = round(time.clock())
        file = open("AltSample.txt", "a")
        file.write("\n")
        file.write(str(t)+","+str(data));
        file.close()
        altitudeGraph.reDraw()
        altitude.reDraw(value=data)
        qAltitude.task_done()

    if(qAccelX.empty() | qAccelY.empty() | qAccelX.empty()):
        pass
    else:
        data = qAccelX.get(False)
        print("Velocity X: " + data)
        qAccelX.task_done()

        data = qAccelY.get(False)
        print("Velocity Y: " + data)
        t = round(time.clock())
        file = open("ASample.txt", "a")
        file.write("\n")
        file.write(str(t)+","+str(data));
        file.close()

        convVel(value = data)
        acceleration.reDraw()
        qAccelY.task_done()

        data = qAccelZ.get(False)
        print("Velocity Z: " + data)
        qAccelZ.task_done()

    if(qGPSLat.empty()):
        pass
    else:
        data = qGPSLat.get(False)
        print("GPS Lat: " + data)
        qGPSLat.task_done()

    if(qGPSLong.empty()):
        pass
    else:
        data = qGPSLong.get(False)
        print("GPS Lon: " + data)
        qGPSLong.task_done()

    hyroGUI.update_idletasks()
    hyroGUI.update()

qTimeStamp.join()
qChamberTemp.join()
qChamberPressure.join()
qAltitude.join()
qAccelX.join()
qAccelY.join()
qAccelZ.join()
qGPSLong.join()
qGPSLat.join()

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

