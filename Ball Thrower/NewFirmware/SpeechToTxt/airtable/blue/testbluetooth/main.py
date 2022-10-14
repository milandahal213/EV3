#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import math
import ubinascii, ujson, urequests, utime
import airtable
brick.sound.beep()   
motorA=Motor(Port.A)

while True:

   voice_command=airtable.Get_AT("Table 1","Name")
   if verdict=="go":
       motorA.run(50)
   elif verdict=="stop":
       motorA.stop()
   else:
       pass

   wait(100)
