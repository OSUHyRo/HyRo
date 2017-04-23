from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import Tk
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import image
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from scipy import integrate
from math import *
import time

hyroGUI = Tk()

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

        def reDraw(self, directory):
            #self.canvas.create_line(0, 0, 200, 100)
          
            j = []
            k = []
            readFile = open(directory+'ASample.txt', 'r')
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

        def reDraw(self, directory):
            #self.canvas.create_line(0, 0, 200, 100)
          
            j = []
            k = []
            readFile = open(directory+'VSample.txt', 'r')
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

        def reDraw(self, directory):
            #self.canvas.create_line(0, 0, 200, 100)
          
            j = []
            k = []
            readFile = open(directory + 'CPSample.txt', 'r')
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

        def reDraw(self, directory):
            #self.canvas.create_line(0, 0, 200, 100)
          
            j = []
            k = []
            readFile = open(directory+'CTSample.txt', 'r')
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

        def reDraw(self, directory):
            #self.canvas.create_line(0, 0, 200, 100)
          
            j = []
            k = []
            readFile = open(directory + 'AltSample.txt', 'r')
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

    def reDraw(self, value, unit):
        #self.canvas.create_line(0, 0, 200, 100)
        self.canvas.delete("all")
        value = int(value)
        scale = self.max - self.min
        r = pi
        p = pi + (pi * (value / scale))
        count = 0

        #Append the unit to the center of the gauge
        self.canvas.create_text(self.width / 2, self.height / 2 + 50, text=unit)

        while r <= 2 * pi:
            xpos = 100*cos(r) + self.width / 2
            #print("x")
            #print(xpos)
            ypos = 100*sin(r) + self.height
            #print("y")
            #print(ypos)
            if(count % 2 == 0):
                self.canvas.create_line(75*cos(r) + self.width / 2, 75*sin(r) + self.height, xpos, ypos, width = 4)
                if not (count == 0 or count == 20):
                    self.canvas.create_text(xpos, ypos - 10, text=count)
            else:
                self.canvas.create_line(75*cos(r) + self.width / 2, 75*sin(r) + self.height, xpos, ypos, width = 1)
            count += 1
            r += (pi / 2) / 10
        self.canvas.create_line(self.width / 2, self.height, 95*cos(p) + self.width / 2, 95*sin(p) + self.height, width = 4, fill="red");

def convVel(value, directory):
    j = []
    k = []
    readFile = open(directory+'ASample.txt', 'r')
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
        file = open(directory+"VSample.txt", "a")
        file.write("\n")
        file.write(str(t)+","+str(data));
        file.close()
        #print("Velocity: " + str(data))