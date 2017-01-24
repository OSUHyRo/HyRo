# !/usr/bin/python3
from tkinter import *

from tkinter import messagebox


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

class drawGuage(drawCanvas):
    def reDraw(self):
        self.canvas.create_line(0, 0, 200, 100)

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

tankPressure = drawGuage(mainwindow=hyroGUI, x=200, y=25, h=200, w=200)
temperature = drawGuage(mainwindow=hyroGUI, x=450, y=25, h=200, w=200)

tankPressure.putScreen()
tankPressure.reDraw()

temperature.putScreen()
temperature.reDraw()

#w = Canvas(hyroGUI, width=200, height=100)
#w.place(x=250, y=100);

#w.create_line(0, 0, 200, 100)
#w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))

#w.create_rectangle(50, 25, 150, 75, fill="blue")

armButton.place(x=50, y=50)
disarmButton.place(x=50, y=100)
fillButton.place(x=50, y=150)
ignButton.place(x=50, y=200)
abortButton.place(x=50, y=250)
launchButton.place(x=50,y=300)

hyroGUI.mainloop()