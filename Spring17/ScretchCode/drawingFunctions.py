from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import Tk
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import image
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from scipy import integrate
from math import *
import time
from scipy.interpolate import spline

hyroGUI = Tk() # Setupd the main window object
coneSep = False
secDeployed = False

matplotlib.rcParams.update({'font.size': 10})
#np.seterr(divide='ignore', invalid='ignore')

#a Generic class to template a drawing function
class drawCanvas:
        #Sets self values including position, window, and Tkinter canvas details.
        def __init__(self, mainwindow, x, y, w, h):
            self.x = x
            self.y = y
            self.window = mainwindow
            self.width = w
            self.height = h
            self.canvas = Canvas(hyroGUI, width=w, height=h)
            self.canvas.config(background='white')

        #Template - Call when you want to put the object on the screen initially
        def putScreen(self):
            self.canvas.place(x = self.x, y = self.y)

        #Template - Call when you want to reDraw, this one is silly and just draws lines and a rectangle. Not actually used.
        def redraw(self):
            self.canvas.create_line(0, 0, 200, 100)
            self.canvas.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))

            self.canvas.create_rectangle(50, 25, 150, 75, fill="blue")

#Acceleration drawing class, Resposible for representing the functions and compents needed to draw the acceleration graph.
class AdrawPlot:
        #set basic self variables like in the template and draw initial graph
        def __init__(self, mainwindow, x, y, w, h):
            self.x = x
            self.y = y
            self.window = mainwindow
            self.width = w
            self.height = h

            j = []
            k = []
            #Open acceleation file and read in contents
            readFile = open('ASample.txt', 'r')
            sepFile = readFile.read().split('\n')
            readFile.close()
            
            if(len(sepFile) <= 1):
                pass

            else:
                #setup array of dat values
                for plotPair in sepFile:
                     if(plotPair == ""):
                        continue
                aAndB = plotPair.split(',')
                j.append(float(aAndB[0]))
                k.append(float(aAndB[1]))

            #plot that array of data values on the acceleration graph
            self.f = Figure(figsize=(self.width,self.height), dpi=100)
            self.accel = self.f.add_subplot(111)
            self.accel.set_ylabel('Gs')
            
            self.accel.yaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter('%.2f'))
            self.accel.plot(j,k)
            #a.plot([1,2,3,4],[1,7,8,9])
            self.f.tight_layout()

            #Draw the new plot on the GUI
            self.canvas = FigureCanvasTkAgg(self.f, master=mainwindow)
            self.canvas.show()
        
        #Graph redrawing function called when new data arrives
        def reDraw(self, directory):
            #repeates the process of the init function as commented above
            j = []
            k = []
            readFile = open(directory+'ASample.txt', 'r')
            sepFile = readFile.read().split('\n')
            readFile.close()
           

            if(len(sepFile) <= 1):
                return

            else:
                for plotPair in sepFile:
                    if(plotPair == ""):
                        continue
                    aAndB = plotPair.split(',')
                    j.append(float(aAndB[0]))
                    k.append(float(aAndB[1]))


            self.accel.clear()
            self.f = Figure(figsize=(self.width,self.height), dpi=100)
            self.accel = self.f.add_subplot(111)
            #newj = np.array(j)
            #newk = np.array(k)

            #x_smooth = np.linspace(newj.min(), newj.max(), 300)
            #y_smooth = spline(newj, newk, x_smooth)

            self.accel.plot(j ,k)
            self.accel.set_ylabel('Gs')
            self.accel.yaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter('%.2f'))
            self.f.tight_layout()

            #self.canvas = FigureCanvasTkAgg(self.f, self.window)
            self.canvas.show()
            self.canvas.get_tk_widget().place(x = self.x, y = self.y)

        #where to initially put the canvas widget, called in HyroMain on initialization
        def putScreen(self):
            self.canvas.get_tk_widget().place(x = self.x, y = self.y)

#Velcoity drawing class, Resposible for representing the functions and compents needed to draw the Chamber
#teperature graph.
class VdrawPlot:
        #Sets basic self variables like in the template and draw initial graph
        def __init__(self, mainwindow, x, y, w, h):
            self.x = x
            self.y = y
            self.window = mainwindow
            self.width = w
            self.height = h

            #Setup arrays and open the Velocity data files for reading
            j = []
            k = []
            readFile = open('VSample.txt', 'r')
            sepFile = readFile.read().split('\n')
            readFile.close()
            
            if(len(sepFile) <= 1):
                pass

            else:
                #read in data values and place into arrays
                for plotPair in sepFile:
                    if(plotPair == ""):
                        continue
                    aAndB = plotPair.split(',')
                    j.append(float(aAndB[0]))
                    k.append(float(aAndB[1]))

            #Plot the values with the graphiging widget
            self.f = Figure(figsize=(self.width,self.height), dpi=100)
            self.velo = self.f.add_subplot(111)
            self.velo.plot(j,k)
            self.velo.set_ylabel('Gs')
            self.velo.yaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter('%.2f'))
            self.f.tight_layout()
            #Construct inital canvas
            self.canvas = FigureCanvasTkAgg(self.f, master=mainwindow)
            self.canvas.show()

        #Chamber pressure redrawing function. Called from HyRo main when new data arrives
        def reDraw(self, directory):
            #This funcitno follows same steps as the init function
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


            self.velo.clear()
            #self.f = Figure(figsize=(self.width,self.height), dpi=100)
            #self.accel = self.f.add_subplot(111)
            self.velo.plot(j,k)
            self.velo.set_ylabel('Gs')
            self.velo.yaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter('%.2f'))
            self.f.tight_layout()
            #self.canvas = FigureCanvasTkAgg(self.f, self.window)
            self.canvas.show()
            self.canvas.get_tk_widget().place(x = self.x, y = self.y)

        #Place the canvas widget on the screen initially, called in Hyro main during initialization
        def putScreen(self):
            self.canvas.get_tk_widget().place(x = self.x, y = self.y)

#Chamber Pressure drawing class, Resposible for representing the functions and compents needed to draw the Chamber
#pressure graph.
class CPdrawPlot:
        #Sets basic self vairables like in the template and draw initial graph
        def __init__(self, mainwindow, x, y, w, h):
            self.x = x
            self.y = y
            self.window = mainwindow
            self.width = w
            self.height = h

            #Setup arrays and open the Chamber pressure data file for reading
            j = []
            k = []
            readFile = open('CPSample.txt', 'r')
            sepFile = readFile.read().split('\n')
            readFile.close()
            
            #read in data values and place into arrays
            if(len(sepFile) <= 1):
                pass

            else:
                for plotPair in sepFile:
                    if(plotPair == ""):
                        continue
                    aAndB = plotPair.split(',')
                    j.append(float(aAndB[0]))
                    k.append(float(aAndB[1]))

            #Setup widget and initialize on screen
            self.f = Figure(figsize=(self.width,self.height), dpi=100)
            self.accel = self.f.add_subplot(111)
            self.accel.plot(j,k)
            self.accel.set_ylabel('Pa')
            #self.accel.yaxis.set_major_formatter(matplotlib.ticker.ScalarFormatter(useMathText=True, useOffset=False))
            #self.accel.yaxis.get_major_formatter().set_powerlimits((0,1))
            self.f.tight_layout()
            self.canvas = FigureCanvasTkAgg(self.f, master=mainwindow)
            self.canvas.show()

        #Chamber Pressure redraw function.
        def reDraw(self, directory):
            #Follows same procedure as the initialzation
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
                    j.append(float(aAndB[0]))
                    k.append(float(aAndB[1]))

            self.accel.clear()
            #self.f = Figure(figsize=(self.width,self.height), dpi=100)
            #self.accel = self.f.add_subplot(111)
            self.accel.plot(j,k)
            self.accel.set_ylabel('Pa')
            #self.accel.yaxis.set_major_formatter(matplotlib.ticker.ScalarFormatter(useMathText=True, useOffset=False))
            #self.accel.yaxis.get_major_formatter().set_powerlimits((0,1))
            self.f.tight_layout()
            #self.canvas = FigureCanvasTkAgg(self.f, self.window)
            self.canvas.show()
            self.canvas.get_tk_widget().place(x = self.x, y = self.y)

        #Place the canvas widget intially on the screen, called from Hyro main during initialization of program
        def putScreen(self):
            self.canvas.get_tk_widget().place(x = self.x, y = self.y)

#Chamber temperature drawing class, Resposible for representing the functions and compents needed to draw the Chamber
#teperature graph.
class CTdrawPlot:
        #Sets basic self variables like the template and draw initial graph
        def __init__(self, mainwindow, x, y, w, h):
            self.x = x
            self.y = y
            self.window = mainwindow
            self.width = w
            self.height = h
            
            #Setup arrays and open the Chamber temperature data file for reading
            j = []
            k = []
            readFile = open('CTSample.txt', 'r')
            sepFile = readFile.read().split('\n')
            readFile.close()
            
            #if file is blank draw nothing
            #read in data values and place into arrays
            if(len(sepFile) <= 1):
                pass

            else:
                for plotPair in sepFile:
                    if(plotPair == ""):
                        continue
                    aAndB = plotPair.split(',')
                    j.append(float(aAndB[0]))
                    k.append(float(aAndB[1]))

            #Setup widget and initialize on screen
            self.f = Figure(figsize=(self.width,self.height), dpi=100)
            self.accel = self.f.add_subplot(111)
            self.accel.plot(j,k)
            self.accel.set_ylabel('C')
            self.f.tight_layout()
            self.canvas = FigureCanvasTkAgg(self.f, master=mainwindow)
            self.canvas.show()

        #Chamber Temperature redraw function.
        def reDraw(self, directory):
            #Follows same procedure as the initialzation
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
                    j.append(float(aAndB[0]))
                    k.append(float(aAndB[1]))


            self.accel.clear()
            #self.f = Figure(figsize=(self.width,self.height), dpi=100)
            #self.accel = self.f.add_subplot(111)
            self.accel.plot(j,k)
            self.accel.set_ylabel('C')
            self.f.tight_layout()
            #self.canvas = FigureCanvasTkAgg(self.f, self.window)
            self.canvas.show()
            self.canvas.get_tk_widget().place(x = self.x, y = self.y)

        #Place the canvas widget intially on the screen, called from Hyro main during initialization of program
        def putScreen(self):
            self.canvas.get_tk_widget().place(x = self.x, y = self.y)

#Altitude drawing class, Resposible for representing the functions and compents needed to draw the Chamber
#teperature graph.
class AltdrawPlot:
        #Sets basic self variables like the template and draw initial graph
        def __init__(self, mainwindow, x, y, w, h):
            self.x = x
            self.y = y
            self.window = mainwindow
            self.width = w
            self.height = h

            #Setup arrays and open the altitude data file for reading
            j = []
            k = []
            readFile = open('AltSample.txt', 'r')
            sepFile = readFile.read().split('\n')
            readFile.close()
            
            #if file is blank draw nothing
            #read in data values and place into arrays
            if(len(sepFile) <= 1):
                pass

            else:
                for plotPair in sepFile:
                    if(plotPair == ""):
                        continue
                    aAndB = plotPair.split(',')
                    j.append(float(aAndB[0]))
                    k.append(float(aAndB[1]))


            #Setup widget and initialize on screen
            self.f = Figure(figsize=(self.width,self.height), dpi=100)
            self.accel = self.f.add_subplot(111)
            self.accel.plot(j,k)
            self.accel.set_ylabel('M')
            self.accel.yaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter('%4d'))
            self.f.tight_layout()
            self.canvas = FigureCanvasTkAgg(self.f, master=mainwindow)
            self.canvas.show()

        #Redraw functino for altitude graph
        def reDraw(self, directory):
            #Follows same procedure as init function
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
                    j.append(float(aAndB[0]))
                    k.append(float(aAndB[1]))

            self.accel.clear()
            #self.f = Figure(figsize=(self.width,self.height), dpi=100)
            #self.accel = self.f.add_subplot(111)
            self.accel.plot(j,k)
            self.accel.set_ylabel('M')
            self.accel.yaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter('%4d'))
            self.f.tight_layout()
            #self.canvas = FigureCanvasTkAgg(self.f, self.window)
            self.canvas.show()
            self.canvas.get_tk_widget().place(x = self.x, y = self.y)

        #Initially place the widget on the screen, called from HyroMain during initialization
        def putScreen(self):
            self.canvas.get_tk_widget().place(x = self.x, y = self.y)

#Class for drawing a guage on the screen, each class instance changes certain parameters to make the gauges behave differently
class drawGuage(drawCanvas):
    #setups self varibales including the gauges minimum and maximum values
    def __init__(self, min, max, *args, **kwargs):
        self.min = min
        self.max = max
        super(drawGuage, self).__init__(*args, **kwargs)

    def reDraw(self, value, unit):
        #erase gauge widget
        self.canvas.delete("all")
        value = float(value)
        scale = self.max - self.min #creates the range of the scale which is divided amongst tic marks
        r = pi #radius of gauges
        p = pi + (pi * (value / scale)) #calculates the degrees the needle needs to be at
        count = 0

        #Append the unit to the center of the gauge
        self.canvas.create_text(self.width / 2, self.height / 2 + 50, text=unit)

        #run through pi to 2 * pi radiuns
        while r <= 2 * pi:
            #xpos of tic mark
            xpos = 100*cos(r) + self.width / 2
            #print("x")
            #print(xpos)
            #ypos of tic mark
            ypos = 100*sin(r) + self.height
            #print("y")
            #print(ypos)
            
            if(count % 2 == 0):
                #draw thicker tic marks every other tic mark
                self.canvas.create_line(75*cos(r) + self.width / 2, 75*sin(r) + self.height, xpos, ypos, width = 4)
                if not (count == 0 or count == 20):
                    if(self.max == 5000):
                        t = int(count * 5 / 2)
                        self.canvas.create_text(xpos, ypos - 10, text=t) # draw tic mark number

                    else:
                        t = int((count / 2) * 10)
                        self.canvas.create_text(xpos, ypos - 10, text=t) # draw tic mark number
            else:
                #draw thinner line on every other tic mark
                self.canvas.create_line(75*cos(r) + self.width / 2, 75*sin(r) + self.height, xpos, ypos, width = 1)
            count += 1
            r += (pi / 2) / 10 #increments while counter, inscrease by one tenth of pi over 2
        #finally draw the need at the proper location
        self.canvas.create_line(self.width / 2, self.height, 95*cos(p) + self.width / 2, 95*sin(p) + self.height, width = 4, fill="red");

#This function will convert the acceleration data into velocity data using scipy's numerical integration.
def convVel(value, directory):
    #open acceration data file and read in contents
    j = []
    k = []
    readFile = open(directory+'ASample.txt', 'r')
    sepFile = readFile.read().split('\n')
    readFile.close()
           
    #need enough points to integrate
    if(len(sepFile) < 3):
        pass

    else:
        # add values to array to integrate
        for plotPair in sepFile:
            if(plotPair == ""):
                continue
            aAndB = plotPair.split(',')
            #print(aAndB)

            if(int(aAndB[0]) == "0"):
                #j.append(float(aAndB[0]))
                j.append(time.clock())
            else:
                #j.append(float(aAndB[0]))
                j.append(time.clock())
            #print(aAndB[0])
            if(aAndB[1] == "0.0"):
                k.append(float(aAndB[1]))
                #k.append(time.clock())
            else:
                k.append(float(aAndB[1]))
                #k.append(time.clock())

            #print(aAndB[1])
        #Uses simpsion functino to numerically integrate the acceration data
        for i in k:
            print(i)
        data = integrate.simps(k, x=j) * 1000
        
        t = round(time.clock()) #get clock time for value
        #open and write velocity data to VSample.txt for use by the velocity redrawing function
        file = open(directory+"VSample.txt", "a")
        file.write("\n")
        file.write(str(t)+","+str(data)); 
        file.close()
        #print("Velocity: " + str(data))