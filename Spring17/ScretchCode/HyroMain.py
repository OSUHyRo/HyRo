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

#the queuess for the data
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

#Flag to stop the main loop when in operation, 0 means not set, 1 mean set
stopflag = 0

#Puts fill commands in the send que for the Xbee thread to process
def sendFill():
       sQue.put("Fill")

#Set screen geometry of the GUI
hyroGUI.geometry("1500x800")

#Setup backround image file.
Back = Canvas(hyroGUI, bg="blue", height=800, width=1500)
backgroundFile = PhotoImage(file = "background.gif")
background_label = Label(hyroGUI, image=backgroundFile)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
Back.pack()

# Create new threads
#Before start stop, this was the orginal spot to create the xbee thread, as you can see in the comment none just set it to none.
xbee_thread = None#xb_rcv_thread(1, "Xbee-Thread", 1,  timeStamp=qTimeStamp, chamberTemp=qChamberTemp, chamberPres=qChamberPressure, altitude=qAltitude, accelX=qAccelX, accelY=qAccelY, accelZ=qAccelZ, GPSLon=qGPSLong, GPSLat=qGPSLat, port="COM3",sQue=sQue)

#Called when start menu item is clicked, sets up the global XBee thread variable, sets stop flag to off, and calls collect data
def start():
    global xbee_thread
    global stopflag
    #Only create thread when its variable is set to none or the thread is not alive
    if(xbee_thread == None):
        xbee_thread = xb_rcv_thread(1, "Xbee-Thread", 1,  timeStamp=qTimeStamp, chamberTemp=qChamberTemp, chamberPres=qChamberPressure, altitude=qAltitude, accelX=qAccelX, accelY=qAccelY, accelZ=qAccelZ, GPSLon=qGPSLong, GPSLat=qGPSLat, port="COM3",sQue=sQue) 
        xbee_thread.start()   
    if not(xbee_thread.is_alive()):
       xbee_thread = xb_rcv_thread(1, "Xbee-Thread", 1,  timeStamp=qTimeStamp, chamberTemp=qChamberTemp, chamberPres=qChamberPressure, altitude=qAltitude, accelX=qAccelX, accelY=qAccelY, accelZ=qAccelZ, GPSLon=qGPSLong, GPSLat=qGPSLat, port="COM3",sQue=sQue) 
       xbee_thread.start()
    stopflag = 0
    print("Started!")
    #Start the XBee thread

    #Run main loop
    collectData()

#Called when a user clicks stop in the GUI. Responsible for stopping xbee thread and setting stop flag to stop the main loop
def stop():
    global stopflag
    #Stop the XBee thread
    xbee_thread.end()
    print("Stopped!")
    stopflag = 1

#classed when the program is exiting by the user clicking the quit button. Joins all queues and destroys the GUI.
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

#Called when auser clicks on load. Opens up a directory dialog and lets the user choose the folder they want to load.
#Then redraws the graph based off that data.
def load():
    directory = fd.askdirectory()
    #add missing \
    directory += "/"
    print("Loading" + directory)

    #redraw gauges at 0 for this
    chamberPressure.reDraw(value=0, unit="Pa x 50,000")
    chamberTemp.reDraw(value=0, unit="C x 10")
    altitude.reDraw(value=0, unit="M x 200")

    #redraw the graphs with the selected files
    chamberPressureGraph.reDraw(directory=directory)
    chamberTempGraph.reDraw(directory=directory)
    altitudeGraph.reDraw(directory=directory)
    velocity.reDraw(directory=directory)
    acceleration.reDraw(directory=directory)        

#Set function for the event WM_DELETE_WINDOW
hyroGUI.protocol("WM_DELETE_WINDOW", on_closing)

#Setup the menu in the GUI
menubar = Menu(hyroGUI)
menubar.add_command(label="Start", command=start)
menubar.add_command(label="Stop", command=stop)
menubar.add_command(label="Load Data", command=load)
menubar.add_command(label="Quit!", command=hyroGUI.quit)

# display the menu
hyroGUI.config(menu=menubar)

#You will see a lot of commented out buttons, this is because the orignal providers of the design where not actually part of this year team 
#and mislead us with information. After expo the rocket team might want a couple of these and we are ready to put them in when desired. 

#setup graphics for the buttons and backgrounds
#armButtonImage = PhotoImage(file="armButtonImage.gif")
#disarmButtonImage = PhotoImage(file="disarmButtonImage.gif")
fillButtonImage = PhotoImage(file="fillButtonImage.gif")
#ignitionButtonImage = PhotoImage(file="ignitionButtonImage.gif")
#abortButtonImage = PhotoImage(file="abortButtonImage.gif")
#launchButtonImage = PhotoImage(file="launchButtonImage.gif")
gaugeImage = PhotoImage(file="gaugeBackgroundImage.gif")

#Initialize buttons as tkinter button widgets

#armButton = Button(hyroGUI, command = lambda: proccessCommand("Arm"))
#disarmButton = Button(hyroGUI, command = lambda: proccessCommand("Disarm"))
fillButton = Button(hyroGUI, command = lambda: sendFill())
#ignitionButton = Button(hyroGUI, command = lambda: proccessCommand("Ignition"))
#abortButton = Button(hyroGUI, command = lambda: proccessCommand("Abort"))
#launchButton = Button(hyroGUI, command = lambda: proccessCommand("Launch"))

#Configure the buttons
#armButton.config(image=armButtonImage, width="125", height="50", bg="#666666", bd=0, relief=SUNKEN, overrelief=RAISED)
#disarmButton.config(image=disarmButtonImage, width="125", height="50", bg="#666666", bd=0, relief=SUNKEN, overrelief=RAISED)
fillButton.config(image=fillButtonImage, width="125", height="50", bg="#666666", bd=0, relief=SUNKEN, overrelief=RAISED)
#ignitionButton.config(image=ignitionButtonImage, width="125", height="50", bg="gray", bd=0, relief=SUNKEN, overrelief=RAISED)
#abortButton.config(image=abortButtonImage, width="125", height="50", bg="gray", bd=0, relief=SUNKEN, overrelief=RAISED)
#launchButton.config(image=launchButtonImage, width="150", height="60", bg="#666666", bd=0, relief=SUNKEN, overrelief=RAISED)

#Initialize gauge classes with initial parameters
chamberPressure = drawGuage(mainwindow=hyroGUI, x=300, y=50, h=150, w=200, min=10 , max=100000)
chamberTemp = drawGuage(mainwindow=hyroGUI, x=600, y=50, h=150, w=200, min=10, max=100)
altitude = drawGuage(mainwindow=hyroGUI, x=900, y=50, h=150, w=200, min=10 , max=4000)

#Initialize graph classes with initial parameters
acceleration = AdrawPlot(mainwindow=hyroGUI, x=440, y=290, h=2, w=3.5)
velocity = VdrawPlot(mainwindow=hyroGUI, x=920, y=290, h=2, w=3.5)
#chamberPressureGraph = drawPlot(mainwindow=hyroGUI, x=300, y=575, h=2, w=3.5)
#altitudeGraph = drawPlot(mainwindow=hyroGUI, x=1050, y=575, h=2,w=3.5)
chamberPressureGraph = CPdrawPlot(mainwindow=hyroGUI, x=250, y=575, h=2, w=3.5)
chamberTempGraph = CTdrawPlot(mainwindow=hyroGUI, x=680, y=575, h=2, w=3.5)
altitudeGraph = AltdrawPlot(mainwindow=hyroGUI, x=1115, y=575, h=2, w=3.5)

#Place the guages on the screen
chamberPressureGraph.putScreen()
chamberTempGraph.putScreen()
altitudeGraph.putScreen()

#Place the graphs on the screen
chamberTemp.putScreen()
altitude.putScreen()
chamberPressure.putScreen()
chamberTemp.putScreen()
acceleration.putScreen()
velocity.putScreen()

#Place the buttons on the screen
#armButton.place(x=50, y=50)
#disarmButton.place(x=50, y=100)
fillButton.place(x=50, y=150)
#ignitionButton.place(x=50, y=200)
#abortButton.place(x=50, y=250)
#launchButton.place(x=10,y=700)

w = Canvas(hyroGUI, 
           width=100, 
           height=100)

w.config(background='white')

w.create_text(20,
              20,
              text="Nose Cone Seperated")


#This is a continous loop that is run to collect data from the rocket!
def collectData():
    global stopflag
    #Get timestamp for data folder
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M-%S')

    #Check if directory exists, it shouldn't but safer, then create it
    #Each run of this software will create a new time stamped directory with files representing each flight of the rocket
    directory = "data\\"+st+"\\"
    #os.chdir(os.path.dirname(os.path.realpath(__file__)))
    if not os.path.exists(directory):
        print("TPONE")
        os.makedirs(directory)
    
    #Open all files and truncate (shouldn't need to but for safety)
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

    #This loop checks all the queues it shares with the XBee thread. If something is found in that queue the data is processed.
    while True:
        global coneSep
        print(coneSep)
        if(coneSep == 1):
            print("JLKSDFJDSK:LJ")
            w.place(x=10,y=400)

        if(stopflag == 1):
            print("Stopping!")
            return

        #stime.sleep(0.5)
        if(qTimeStamp.empty()):
            pass
        else:
            data = qTimeStamp.get(False)
            qTimeStamp.task_done()

        if (qChamberPressure.empty()):
            pass
        else:
            #There is data in the chamber pressure queue
            data = qChamberPressure.get(False)

            #print("Chamber Pressure: " + data)
            #Get time and data value and store in sample file.
            t = round(time.clock())
            file = open(directory+"CPSample.txt", "a")
            file.write("\n")
            file.write(str(t)+","+str(data));
            file.close()
            #Call the redraw function
            chamberPressureGraph.reDraw(directory=directory)
            chamberPressure.reDraw(value=data, unit="Pa x 50,000")
            #Remove item from queue
            qChamberPressure.task_done()
        
        if(qChamberTemp.empty()):
            pass
        else:
            #same procedure as above
            data = qChamberTemp.get(False)
            t = round(time.clock())
            file = open(directory+"CTSample.txt", "a")
            file.write("\n")
            file.write(str(t)+","+str(data));
            file.close()
            #print("Chamber Temperature: " + data)
            chamberTempGraph.reDraw(directory=directory)
            chamberTemp.reDraw(value=data, unit="C x 10")
            qChamberTemp.task_done()

        if(qAltitude.empty()):
            pass
        else:
            #same procedure as above
            data = qAltitude.get(False)
            #print("Altitude: " + data)

            t = round(time.clock())
            file = open(directory+"AltSample.txt", "a")
            file.write("\n")
            file.write(str(t)+","+str(data));
            file.close()
            altitudeGraph.reDraw(directory=directory)
            altitude.reDraw(value=data, unit="M x 200")
            qAltitude.task_done()

        if(qAccelX.empty() | qAccelY.empty() | qAccelZ.empty()):
            pass
        else:
            data = qAccelX.get(False) #we only care about acceleration in the Y for now so just remove this from the queue
            #print("Velocity X: " + data)
            qAccelX.task_done()

            #take acceleration y data and store it in Asample with a timestamp
            data = qAccelY.get(False)
            #print("Velocity Y: " + data)
            t = round(time.clock())
            file = open(directory+"ASample.txt", "a")
            file.write("\n")
            file.write(str(t)+","+str(data));
            file.close()

            #Now run the velocity conversion function to convert the acceraltion data to velcoity
            convVel(value = data, directory = directory)
            velocity.reDraw(directory=directory) #redraw velocity after conversion
            acceleration.reDraw(directory=directory)
            qAccelY.task_done()

            #dont care right now, just delete from queue
            data = qAccelZ.get(False)
            #print("Velocity Z: " + data)
            qAccelZ.task_done()

        #This is a stretch goal, but we will be implementing this before the rocket flight, but after expo.
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

hyroGUI.mainloop() #Keep GUI thread running


#This was test code to find the port, but was not implemented. Might do it after expo for fun if we have time.

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

