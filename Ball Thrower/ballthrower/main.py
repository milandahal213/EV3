#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.ev3devio import Ev3devSensor


# Write your program here
ev3 = EV3Brick()
ev3.speaker.beep()



sensor_left=Ev3devSensor(Port.S4)
print(sensor_left.read(0))
