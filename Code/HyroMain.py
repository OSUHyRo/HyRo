# !/usr/bin/python3
import datetime
from xbee_threads import *
import time
from queue import Queue
from PIL import ImageTk,Image
import random
from drawingFunctions import *
import os
import tkinter.filedialog as fd

#the ques for the data
qChamberTemp = Queue()
qChamberPressure = Queue()
qAltitude = Queue()
qAccelY = Queue()
qAccelZ = Queue()
qAccelX = Queue()
qGPSLong = Queue()
qGPSLat = Queue()
qTimeStamp = Queue()
sQue = Queue()

stopflag = 0

def sendFill():
       sQue.put("Fill")

hyroGUI.geometry("1500x800")

Back = Canvas(hyroGUI, bg="blue", height=800, width=1500)
backgroundFile = PhotoImage(file = "background.gif")
background_label = Label(hyroGUI, image=backgroundFile)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
Back.pack()

# Create new threads
xbee_thread = None#xb_rcv_thread(1, "Xbee-Thread", 1,  timeStamp=qTimeStamp, chamberTemp=qChamberTemp, chamberPres=qChamberPressure, altitude=qAltitude, accelX=qAccelX, accelY=qAccelY, accelZ=qAccelZ, GPSLon=qGPSLong, GPSLat=qGPSLat, port="COM3",sQue=sQue)

def start():
    global xbee_thread
    global stopflag
    if(xbee_thread == None):
        print("Test2")
        xbee_thread = xb_rcv_thread(1, "Xbee-Thread", 1,  timeStamp=qTimeStamp, chamberTemp=qChamberTemp, chamberPres=qChamberPressure, altitude=qAltitude, accelX=qAccelX, accelY=qAccelY, accelZ=qAccelZ, GPSLon=qGPSLong, GPSLat=qGPSLat, port="COM3",sQue=sQue) 
        xbee_thread.start()   
    if not(xbee_thread.is_alive()):
       print("TEST")
       xbee_thread = xb_rcv_thread(1, "Xbee-Thread", 1,  timeStamp=qTimeStamp, chamberTemp=qChamberTemp, chamberPres=qChamberPressure, altitude=qAltitude, accelX=qAccelX, accelY=qAccelY, accelZ=qAccelZ, GPSLon=qGPSLong, GPSLat=qGPSLat, port="COM3",sQue=sQue) 
       xbee_thread.start()
    stopflag = 0
    print("Started!")
    #Start the XBee thread

    collectData()

def stop():
    global stopflag
    #Stop the XBee thread
    xbee_thread.end()
    print("Stopped!")
    stopflag = 1

def on_closing():
    #Join all the queing threads before Closing
    qTimeStamp.join()
    qChamberTemp.join()
    qChamberPressure.join()
    qAltitude.join()
    qAccelX.join()
    qAccelY.join()
    qAccelZ.join()
    qGPSLong.join()
    qGPSLat.join()
    sQue.join() 
    hyroGUI.destroy()

def load():
    directory = fd.askdirectory()
    #add missing \
    directory += "/"
    print("Loading" + directory)

    #redraw gauges at 0 for this
    chamberPressure.reDraw(value=0)
    chamberTemp.reDraw(value=0)
    altitude.reDraw(value=0)

    #redraw the graphs with the selected files
    chamberPressureGraph.reDraw(directory=directory)
    chamberTempGraph.reDraw(directory=directory)
    altitudeGraph.reDraw(directory=directory)
    velocity.reDraw(directory=directory)
    acceleration.reDraw(directory=directory)        


hyroGUI.protocol("WM_DELETE_WINDOW", on_closing)

menubar = Menu(hyroGUI)
menubar.add_command(label="Start", command=start)
menubar.add_command(label="Stop", command=stop)
menubar.add_command(label="Load Data", command=load)
menubar.add_command(label="Quit!", command=hyroGUI.quit)

# display the menu
hyroGUI.config(menu=menubar)

armButtonImage = PhotoImage(file="armButtonImage.gif")
disarmButtonImage = PhotoImage(file="disarmButtonImage.gif")
fillButtonImage = PhotoImage(file="fillButtonImage.gif")
ignitionButtonImage = PhotoImage(file="ignitionButtonImage.gif")
abortButtonImage = PhotoImage(file="abortButtonImage.gif")
launchButtonImage = PhotoImage(file="launchButtonImage.gif")
gaugeImage = PhotoImage(file="gaugeBackgroundImage.gif")

armButton = Button(hyroGUI, command = lambda: proccessCommand("Arm"))
disarmButton = Button(hyroGUI, command = lambda: proccessCommand("Disarm"))
fillButton = Button(hyroGUI, command = lambda: sendFill())
#ignitionButton = Button(hyroGUI, command = lambda: proccessCommand("Ignition"))
#abortButton = Button(hyroGUI, command = lambda: proccessCommand("Abort"))
launchButton = Button(hyroGUI, command = lambda: proccessCommand("Launch"))

armButton.config(image=armButtonImage, width="125", height="50", bg="gray", bd=0, relief=SUNKEN, overrelief=RAISED)
disarmButton.config(image=disarmButtonImage, width="125", height="50", bg="gray", bd=0, relief=SUNKEN, overrelief=RAISED)
fillButton.config(image=fillButtonImage, width="125", height="50", bg="gray", bd=0, relief=SUNKEN, overrelief=RAISED)
#ignitionButton.config(image=ignitionButtonImage, width="125", height="50", bg="gray", bd=0, relief=SUNKEN, overrelief=RAISED)
#abortButton.config(image=abortButtonImage, width="125", height="50", bg="gray", bd=0, relief=SUNKEN, overrelief=RAISED)
launchButton.config(image=launchButtonImage, width="125", height="50", bg="gray", bd=0, relief=SUNKEN, overrelief=RAISED)

chamberPressure = drawGuage(mainwindow=hyroGUI, x=300, y=50, h=150, w=200, min=10 , max=100)
chamberTemp = drawGuage(mainwindow=hyroGUI, x=600, y=50, h=150, w=200, min=10, max=100)
altitude = drawGuage(mainwindow=hyroGUI, x=900, y=50, h=150, w=200, min=10 , max=100)

acceleration = AdrawPlot(mainwindow=hyroGUI, x=440, y=290, h=2, w=3.5)
velocity = VdrawPlot(mainwindow=hyroGUI, x=920, y=290, h=2, w=3.5)
#chamberPressureGraph = drawPlot(mainwindow=hyroGUI, x=300, y=575, h=2, w=3.5)
#altitudeGraph = drawPlot(mainwindow=hyroGUI, x=1050, y=575, h=2,w=3.5)
chamberPressureGraph = CPdrawPlot(mainwindow=hyroGUI, x=250, y=575, h=2, w=3.5)
chamberTempGraph = CTdrawPlot(mainwindow=hyroGUI, x=680, y=575, h=2, w=3.5)
altitudeGraph = AltdrawPlot(mainwindow=hyroGUI, x=1115, y=575, h=2, w=3.5)

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
#ignitionButton.place(x=50, y=200)
#abortButton.place(x=50, y=250)
launchButton.place(x=10,y=700)


def collectData():
    global stopflag
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M-%S')

    #Check if directory exists, it shouldn't but safer, then create it
    #Each run of this software will create a new time stamped directory with files representing each flight of the rocket
    directory = "data\\"+st+"\\"
    #os.chdir(os.path.dirname(os.path.realpath(__file__)))
    if not os.path.exists(directory):
        print("TPONE")
        os.makedirs(directory)
    
    file = open(directory+"CTSample.txt", "w")
    file.truncate()
    file.close()

    file = open(directory+"CPSample.txt", "w")
    file.truncate()
    file.close()

    file = open(directory+"AltSample.txt", "w")
    file.truncate()
    file.close()

    file = open(directory+"ASample.txt", "w")
    file.truncate()
    file.close()

    file = open(directory+"VSample.txt", "w")
    file.truncate()
    file.close()

    while True:
        if(stopflag == 1):
            print("Stopping!")
            return

        time.sleep(0.5)
        if(qTimeStamp.empty()):
            pass
        else:
            data = qTimeStamp.get(False)
            #print("Time Stamp: " + data)
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

            #print("Chamber Pressure: " + data)
            t = round(time.clock())
            file = open(directory+"CPSample.txt", "a")
            file.write("\n")
            file.write(str(t)+","+str(data));
            file.close()
            chamberPressureGraph.reDraw(directory=directory)
            chamberPressure.reDraw(value=data)
            #convert, store in long term, and write to file with timestamp
            qChamberPressure.task_done()
        
        if(qChamberTemp.empty()):
            pass
        else:
            data = qChamberTemp.get(False)
            t = round(time.clock())
            file = open(directory+"CTSample.txt", "a")
            file.write("\n")
            file.write(str(t)+","+str(data));
            file.close()
            #print("Chamber Temperature: " + data)
            chamberTempGraph.reDraw(directory=directory)
            chamberTemp.reDraw(value=data)
            qChamberTemp.task_done()

        if(qAltitude.empty()):
            pass
        else:
            data = qAltitude.get(False)
            #print("Altitude: " + data)

            t = round(time.clock())
            file = open(directory+"AltSample.txt", "a")
            file.write("\n")
            file.write(str(t)+","+str(data));
            file.close()
            altitudeGraph.reDraw(directory=directory)
            altitude.reDraw(value=data)
            qAltitude.task_done()

        if(qAccelX.empty() | qAccelY.empty() | qAccelZ.empty()):
            pass
        else:
            data = qAccelX.get(False)
            #print("Velocity X: " + data)
            qAccelX.task_done()

            data = qAccelY.get(False)
            #print("Velocity Y: " + data)
            t = round(time.clock())
            file = open(directory+"ASample.txt", "a")
            file.write("\n")
            file.write(str(t)+","+str(data));
            file.close()

            convVel(value = data, directory = directory)
            velocity.reDraw(directory=directory)
            acceleration.reDraw(directory=directory)
            qAccelY.task_done()

            data = qAccelZ.get(False)
            #print("Velocity Z: " + data)
            qAccelZ.task_done()

        if(qGPSLat.empty()):
            pass
        else:
            data = qGPSLat.get(False)
            #print("GPS Lat: " + data)
            qGPSLat.task_done()

        if(qGPSLong.empty()):
            pass
        else:
            data = qGPSLong.get(False)
            #print("GPS Lon: " + data)
            qGPSLong.task_done()

        hyroGUI.update_idletasks()
        hyroGUI.update()

hyroGUI.mainloop()

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

