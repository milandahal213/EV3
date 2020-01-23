#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import utime
gg=GyroSensor(Port.S4)
touch=TouchSensor(Port.S2)
brick.display.text("milan")
anglecounter=0
motor=Motor(Port.D,Direction.COUNTERCLOCKWISE)
frontmotor=Motor(Port.A,Direction.COUNTERCLOCKWISE)
dist=UltrasonicSensor(Port.S1)
def reverse():
    
    motor=Motor(Port.D,Direction.CLOCKWISE)
    starttime=utime.ticks_ms()
    b=0
    while (not touch.pressed()) and (b<3000):
        motor.run(360)
        currenttime=utime.ticks_ms()
        b=currenttime-starttime
        if motor.stalled():
            break
    motor=Motor(Port.D,Direction.COUNTERCLOCKWISE)
    turn(1,(gg.angle()-anglecounter*10))

def turn(dir,ang):
    if dir==1:
        frontmotor.run_angle(100,ang)
    else:
        frontmotor.run_angle(100,-ang)

while True:
    print("angle",gg.angle())
    motor.run(360)
    
    if dist.distance() <100 or motor.stalled():
        motor.stop()
        reverse()
        anglecounter+=1
    print(gg.angle()-anglecounter*10)
    
utime.sleep(10)