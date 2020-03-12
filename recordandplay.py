#!/usr/bin/env pybricks-micropython
#brickrun -r -- pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.parameters import Color, Port
from pybricks.ev3devices import Motor
from pybricks.iodevices import AnalogSensor, UARTDevice
# Initialize the EV3
ev3 = EV3Brick()
ev3.speaker.beep()
import os

def record(length):
    os.system("arecord -D plughw:3,0 -t wav --duration="+str(length)+" test.wav")

def playback():
    os.system("aplay -D plughw:3,0 test.wav")

record(3)
wait(2000)
playback()