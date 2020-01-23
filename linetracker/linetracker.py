#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
import utime
from pybricks.ev3devio import Ev3devSensor

brick.sound.beep() #program has successfully started



class MySensor(Ev3devSensor):
    _ev3dev_driver_name='ev3-analog-01'

    def readvalue(self):
        self._mode('ANALOG')
        return self._value(0)


left=MySensor(Port.S4)
right=MySensor(Port.S1)
leftM=Motor(Port.A,Direction.CLOCKWISE)
rightM=Motor(Port.D,Direction.CLOCKWISE)
while True:
    print("left",left.readvalue()) 
    print("right",right.readvalue()) 
    if (right.readvalue()<800):
        leftM.run(40)
        rightM.run(0)
    elif (left.readvalue()<400):
        rightM.run(40)
        leftM.run(0)
    else:
        leftM.run(30)
        rightM.run(30)
    utime.sleep(1)