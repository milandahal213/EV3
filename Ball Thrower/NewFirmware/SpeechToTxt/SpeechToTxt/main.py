#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.parameters import Color, Port
from pybricks.ev3devices import (Motor, TouchSensor,
          ColorSensor, UltrasonicSensor, GyroSensor)
from pybricks.tools import wait, StopWatch
import random
import ujson, urequests
ev3 = EV3Brick()
ev3.sound.beep()