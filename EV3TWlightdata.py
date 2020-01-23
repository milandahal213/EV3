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
import urequests
print(round(utime.time()))

lit=ColorSensor(Port.S1)

Key = "7157a849-3f05-4436-9936-01c430c24774" # Use your appkey
urlBase = "https://pp-1909111719d4.portal.ptc.io/Thingworx/" # Use your ThingWorx URL
headers = {"Accept":"application/json","Content-Type":"application/json","AppKey":Key}

def Put(thing, property, type, value):
     urlValue = urlBase + 'Things/' + thing + '/Properties/*'

     propValue = {property:value}
     try:
          response = urequests.put(urlValue,headers=headers,json=propValue)
          print(response.text)
          response.close()
     except RuntimeError as e:
          print('error with Put',e)
def CallService(thing, servicename):
     urlValue = urlBase + 'Things/' + thing + '/Services/' + servicename
     try: 
          response = urequests.put(urlValue,headers=headers)
          print(response.text)
          response.close()
     except RuntimeError as e:
          print('error with AddtoTable',e)
       
# Loop
Put('Ev3Data','starttime','NUMBER',round(utime.time()))
while True:
    Put('Ev3Data', 'light', 'NUMBER', lit.ambient())
    Put('Ev3Data', 'time', 'NUMBER', round(utime.time()))
    CallService("Ev3Data","AddData")      
    utime.sleep(300) #sleep for 5 minutes