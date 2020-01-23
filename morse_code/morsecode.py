#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import utime
brick.display.text("milan")
utime.sleep(1)
dots=[None] *10
dashes=[None] *10
t=TouchSensor(Port.S1)
dot_counter=0
dash_counter=0
howmany=10

f = open('data.csv', 'w')           #opens the file in write mode

brick.display.text("Hold down for DOTS")
f.write("Dots ,")
while True:  
    while(t.pressed()==False):
        print("") 
    a=utime.ticks_ms()
    while (t.pressed()):
        print("")
    b=utime.ticks_ms()
    brick.display.text("Entry "+str(dot_counter+1)+" "+str(b-a)+" ms")
    dots[dot_counter]=b-a
    f.write(str(b-a)+",")
    dot_counter+=1
    if(dot_counter==howmany):
        break

f.write("\nDash ,")
brick.display.text("Hold down for DASHES")
while True:
    while(t.pressed()==False):
        print("")
    a=utime.ticks_ms()
    while (t.pressed()):
        print("")
    b=utime.ticks_ms()
    brick.display.text("Entry "+str(dash_counter+1)+" "+str(b-a)+" ms")
    dashes[dash_counter]=b-a
    f.write(str(b-a)+",")
    dash_counter+=1
    if(dash_counter==howmany):
        break
f.close()





