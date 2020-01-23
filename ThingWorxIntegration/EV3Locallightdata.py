#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
brick.sound.beep() #program has successfully started
#importing libraries
import os
import utime
#define an object for colorsensor on port S2
light=ColorSensor(Port.S1)
f = open('data.csv', 'w')           #opens the file in write mode
while True:         
    a=light.ambient()        
    f.write(str(a)+",")         #writes the value to the file and adds a comma
    utime.sleep(300)                #sleeps for 5 minutes

f.close()