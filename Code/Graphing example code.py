# Jason Klindtworth
# Physics 213 Exam 1 extra credit
# 
# Goal:
# The goal of this program is to calculate the electric force and acceleration of a horizontal stirrer when placed close to a stationary vertical 
# rod. We are given the dimentions of the rod and stirrer and the distance between them, as well as the charge of each. We are going to integrate the force
# both the rod and stirrer together as the stirrer is repeled away from the rod since both of the objects are positivly charged.

from visual import *
from math import *
from visual.graph import *

universe = display (x=0, y=0, width=600, height=600, center=(.2,0,0), range = vector(0.3,0.3,0.3)) # sets up display and size of universe to scale that will be useful

graph1 = gdisplay(x=600,y=0,xtitle="time",ytitle="Position") # creates graph to track the position of the stirrer
positionGraph = gcurve(color=color.blue)

graph2 = gdisplay(x=600,y=400,xtitle="time",ytitle="Acceleration") # creates graph to track the acceleration of the stirrer
accelerationGraph = gcurve(color=color.red)

#Rod ---------------------------------------
H = 0.55 #height of rod in meters
dh = .001 #small amount of height in meters
q1 = 137e-9 #Charge in C
dq1 = .001 # small amount of charge

#stirrer -----------------------------------
L = 0.06 # length of stirrer in meters
dl = .001 #small amount of length in meters
m = 0.0005 #Mass in kg
q2 = 93e-9 #Charge in C
dq2 = .001 #small amount of charge

#universe ----------------------------------
d = 0.023#distance between rod and stirrer in m
K = 8.99e9 # constant for 1 over 4 pi epsilon not
s = vector(d   ,0.0 ,0.0) #initial position of stirrer in m
v = vector(0.0 ,0.0 ,0.0) #initial velocity of stirrer in m/s
a = vector(0.0 ,0.0 ,0.0) #initial acceleration of stirrer in m/s^2
F = 0 #Force variable to sum forces
df = 0 #calculation of each force (each time through the loop it will calculate a different value)
h = 0 #sum of the change in heights

t = 0 #time in seconds
dt = .001 #time interval in seconds

rod = cylinder(pos = (0,-H/2,0), axis = (0,H,0), radius = .01, color = color.blue) #creates rod object on the screen
stirrer = cylinder(pos=s, axis=(L,0,0), radius = .01, color = color.red) #creates stirrer object on the screen

rod_label_pos = label(pos=stirrer.pos, text = 'Sx=%1.2f' %(d), xoffset=50,yoffset=90)#creates a label for the position of the stirrer
rod_label_acc = label(pos=stirrer.pos, text = 'Sx=%1.2f' %(d), xoffset=50,yoffset=50)# creates a label for the acceleration of the stirrer


#loop inside of loop to get the acceleration of the stirrer, and to calculate the change in acceleration as it moves away from the rod.
while d < .35:
    rate(10000)
    h = 0 # resets h after the inside loop runs each time
    F = 0 # resets F after th einside loop runs each time
    while h < H/2: #inside integral bounds are from h to H/2 (Integrated half of the rod, and added a multiplier of 2 to the function because of symmetry)
        df = - (q1 * q2 * K / (L * H)) * 2 * (1/sqrt(((L+d)**2 + h**2)) - 1/sqrt(d**2 + h**2))*dh #Integral calculation of the Rod and the Stirrer
        F = F + df #adding the calculation of df into F each time the loop runs
        h = h + dh #adding the calculation of df into h each time the loop runs
        rate(10000)
        a = F/m # updating acceleration with new values
        
    v.x = v.x + a*dt #updating the velocity of the stirrer
    d = d + v.x*dt #updating the distance the stirrer is from the rod
    rod_label_pos.pos = stirrer.pos #changes the position of the position label 
    rod_label_pos.text = 'distance from Rod=%1.3f m' %d # updates the text of the position label
    rod_label_acc.pos = stirrer.pos #changes the position of the acceleration label 
    rod_label_acc.text = 'acceleration of Stirrer=%1.3f m' %a # updates the text of the acceleration label
    stirrer.pos = (d,0.0,0.0) # updates the new position of the stirrer
    positionGraph.plot(pos=(t,d)) # updates the graph for position
    accelerationGraph.plot(pos=(t,a)) # updates the graph for acceleration
    if t==0:
        print ('The Fnet on the stirrer at initial time in Newtons is: %1.5f'%F) # prints the initial force of the system
        print ('The acceleration at initial time in m/s^2 is: %1.5f'%a) # prints the initial acceleration of the system
    t = t + dt #increments time


print "Program Complete"
