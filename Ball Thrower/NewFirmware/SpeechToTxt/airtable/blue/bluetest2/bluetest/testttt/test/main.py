#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.
# Initialize the EV3
ev3 = EV3Brick()
#dist=UltrasonicSensor(Port.S1)
wheel=Motor(Port.A)
#scoop=Motor(Port.B)
clamp=Motor(Port.B)
wheel.reset_angle(0)
clamp.reset_angle(0)
#claw.reset_angle(0)
ang=clamp.run_until_stalled(90,duty_limit=30)
clamp.reset_angle(0)
clamp.run_target(50,-300)
#a=10
#b=0
#while True:
  #wheel.run(a)
  #scoop.run(0)
while True:
  if Button.UP in ev3.buttons.pressed():
    ang=clamp.run_until_stalled(90,duty_limit=30)
    wait(2000)         
    print(ang)
    if (abs(ang)>80):
      ev3.speaker.say("trash detected")

    else:
      ev3.speaker.say("trash not detected")

  if Button.DOWN in ev3.buttons.pressed():
    clamp.run_until_stalled(90,duty_limit=30)
    clamp.reset_angle(0)
    clamp.run_target(50,-300)

  
'''if dist.distance()<60:       #if distance is less than vf  60
    wheel.reset_angle(0)      
    wheel.run_target(90,90)   #move the robot to put the trash under the claw
    claw.run_until_stalled(90,duty_limit=50)    #close the claw
    scoop.run_target(30,-50)  #move the scoop up
    wait(3000)
  wait(3)
'''
'''
while True:
  y.run_target(50,-10)


  x.run_target(50,0)
  y.run_target(50,10 )

  x.run_target(50,10)
  x.run_target(50,30, wait=False)
  y.run_target(50,30)

  wait(2)         
 '''                                                                                
# t=TouchSensor(Port.S1)
#import urequests
#import utime, ubinascii, ujson, urequests
'''Key='efd544cd-a592-42d6-9a23-8c9d01edd6ab'
urlBase = "https://pp-1909111719d4.portal.ptc.io/Thingworx/" # Use your ThingWorx URL
headers = {'Accept':'application/json','Content-Type':'application/json','AppKey':Key}
i=0
gs = GyroSensor(Port.S2)
while True:
  
  angle = gs.angle()
  #ev3.screen.print(angle)
  print(angle)
  wait(1)



  us = UltrasonicSensor(Port.S4)
  dist = us.distance()
  ev3.screen.print(dist)
  i += 1
def Put(thing, property, type, value):
     urlValue = urlBase + 'Things/' + thing + '/Properties/*'
     propValue = {property:value}
     try:
          response = urequests.put(urlValue,headers=headers,json=propValue)
          print(response.text)
          response.close()
     except:
          print('error with Put')
Put('Day3', 'KateNajibTom', 'STRING', '40')
# ev3.speaker.say("Press Touch Sensor to Begin")
def Get(thing, property):
   urlValue = urlBase + 'Things/' + thing + '/Properties/' + property
   print(urlValue)
   try:
     response = urequests.get(urlValue,headers=headers)
     print(response)
     value = response.text
     response.close()
     print(value)
     data = ujson.loads(value)
     result = data.get("rows")[0].get(property)
     print(result)
     #result="dd"
   except:
     print('error')
     result = 'error'
   return result
thingworxValue = Get('Day3', 'KateNajibTom')
print(thingworxValue)
ev3.screen.print(thingworxValue)
wait(5000)'''