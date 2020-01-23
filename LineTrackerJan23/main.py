#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import utime
from pybricks.ev3devio import Ev3devSensor

class MySensor(Ev3devSensor):
    _ev3dev_driver_name='ev3-analog-01'

    def readvalue(self):
        self._mode('ANALOG')
        return self._value(0)

sensor_left=MySensor(Port.S1)
sensor_right=MySensor(Port.S4)
# Write your program here
brick.sound.beep()

left=[None] *10
right=[None] *10
def calibrate():
    for i in range(10):
        left[i]= sensor_left.readvalue()
        right[i]=sensor_right.readvalue()
        utime.sleep(0.5)
    l_threshold=sum(left)/len(left)
    r_threshold=sum(right)/len(right)
    return(l_threshold,r_threshold)

while True:

    l_threshold,r_threshold=calibrate()
    print("left",sensor_left.readvalue(),"threshold",l_threshold)
    print("right",sensor_right.readvalue(),"threshold",r_threshold)
    utime.sleep(1)
'''motor_left=Motor(Port.A)
motor_right=Motor(Port.D)
motor_left.run(-100)
motor_right.run(-100)
utime.sleep(10)
'''



