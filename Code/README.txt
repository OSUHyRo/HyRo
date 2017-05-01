
                           
               _           
 ___ ___ ___ _| |_____ ___ 
|  _| -_| .'| . |     | -_|
|_| |___|__,|___|_|_|_|___|

OSU Hybrid rocket team (HYRO) Readme

How to run:

(1) environment:

Development environment: Visual Studio community 2017 preview and Windows 8.1 / Windows 10.
Preview must be used to be able to install the python extension.
This was done during installation, see MSDN website for instructions of how to do this post install.
Again the python extension said it only worked in the preview version of 2017.
Other version of visual studio should work, but will require the download of the python extentions.
Information about the extension here: https://www.visualstudio.com/vs/python/

Python v.3.6 -
As a note here we persnoally experienced different results installing the packaged based on the python version. We settled on 3.6, but some packages had to be manually installed
using wheel files.

Main:
	HyroMain.py

Supplementary Files:
	xbee_threads.py
	drawingFunctions.py

Sample Data Directory:
	[SOURCE ROOT}\data
	
	*SOURCE ROOT is the directory your running the python program from.
	
Sample Data Files:
	ASample.txt
	AltSample.txt
	CPSample.txt
	CTSample.txt
	VSample.txt

	*Every time the user clicks start a new directory is made under the data folder. This directory is name the time stamp and date of when the user clicked start. 
	Under each one of these directories you will find files with the above names.
	
Visual Studio Packages:
	cycler
	matplotlib
	numpy *
	olefile
	Pillow
	pip
	plot
	pyparsing
	pyserial
	python-dateutil
	pytz
	scipy *
	setuptools
	six
	typing
	XBee

	These two packages we had trouble with using Python 3.6 they had to manually installed using the correct wheel files.
	These files can be found here ( http://www.lfd.uci.edu/~gohlke/pythonlibs/#debug-information-files ) according to your system.
	
	


(2) Installation Instructions on Windows

1. Aquire visual studio 2017 preview and install python extension along side.

2. Download the python 3.6 environment standalone or through visual studio.

3. From the python evironment install all required packages. Some may need to be manually installed using a wheel file.

4. Create a new project and place all files from the repo into the project directory. NOT INCLUDING, for you conviences, any files UNDER the 
   data directory. The data directory itself needs to exist in the project folder.
   
**NOTE) You may want to choose to leave thes files intact if you do not want to receraete this setup. You'll be able to load previously recorded data from these files
	if you want to test the loading feature and see what the data looks like.
   
5. Add HyroMain.py, drawingFunctions.py, and xbee_threads.py to the project.

6. Set HyroMain.py as the entry point of the program.

7. You can now run the program through visual studio, instuctions on the user interface after the next section.

**Note) all graphics are included in the repor and are needed to make the program work. Just make sure to take all files
except the ones UNDER the data directory, but including the data directory itself. 

(3) Installation Instructions for beagle bone radnom data test and Xbee usb board to computer.

**NOTE) These steps require a beagle bone black micro computer, 2 XBee Pro S1 radio transcievers, a bread board, wire, solder, and a usb break out board for said Xbees.

**NOTE) Real data is comming from the avionics bay developed by the ECE team. They have posession of the bay and have not yielded it to us full time, only briefly for integration testing.
Hence the needs to have a constant setup at least supplying fake data.

1 ) You'll need to connect one of the XBees to a usb break out board designed for them. Once connected connect it to you computer via USB. Drivers should install automatically, if not
look at break out board documentation for installation instructions. 

2 ) Download the XTCU program by digi  key ( https://www.digi.com/products/xbee-rf-solutions/xctu-software/xctu ) that you use to adjust the XBees. 

3 ) Follow instuctions from them to change the XBee's mode to API. Unplug your xbee and repeat these steps for the second. Leave one connected to your main computer.

4) To install an XBee to the beage bone black the ghetto way first solder wires to pins 1, 2, 3, and 10 on the XBee.

5) Places these wires or route them through a bread board (what we did) then place them into the coresponding pins on the beage bone black (BBB).
	XBee(Pin 10) --> BBB (Pin 1) (Ground)
	XBee(Pin 1) --> BBB ( Pin 3) (Power)
	XBee(Pin 2) --> BBB (Pin 22) (Serial RX)
	XBee(Pin 3) --> BBB (Pin 21) (Serial TX)
	
6) Connect the BBB to your computer via usb and start a console session with putty. Log in to the system.

**NOTE) You will need the BBB drivers installed on your computers, instructions can be found on the popup drive when the BBB is connected.
**NOTE) Usually you ssh to 192.168.7.2

7) Setup whatever folder you like for this testing and make sure the python installation is up to date (minimum in 3.x).

8) Run this command to enable UART2 (this is what you connected the rx and tx lines to) 
echo BB-UART2 > /sys/devices/bone_capemgr.*/slots

10) Copy the files test.py and XBeeAPI.py to the folder you created. XBeeAPI.py is the API the ECE team decided to use and is used in this test file to make
	sure the API are compatable. 

11) Change line 53 to addr = [YOUR USB BREAK OUT BOARD XBEES MAC ADDRESS]

**NOTE) This can be obtained threw XTCU
 
12) If all has gone well go ahead and run "python test.py" without the quotes. This will begin random data sending and you'll se "ready..." over and over again on the
	console. To terminate the test program hit CTRL-C.
	
**NOTE) This only sends random data to the graphs. We originally tested the fill command reception with it, but since the change have only tested the sending with the acutally ECE
team. It does work, but is not included in this test. 

Using The Interface:


 Once you have started the test program and launching the interfaces throughv visual  studio you'll be present with a GUI on the left you'll see a fill button. This wont do anything
 not attached to the real avionics bay. On the right hand side you'll see gauges and graphs. These will be filled with data once you start data collection. On the top you'll se menu
 with buttons labeled start, stop, load, quit. Quit will close the GUI, start will start the data collection (test.py needs to be running to see the test data, and a warning its very
 random). Hit stop to stop data collection. You can reload previous data by clicking on load, if you do so load will bring up a selection diaglog. Navigate to the data folder under
 the python visual studio project directory and choose the folder with the correct timestamp. This will load that sessions data. 
 
 **NOTE) You may have to change the com port in start() in HyroMain.py to the comport selected by your system for the XBee. Ours currently is using COM3.
