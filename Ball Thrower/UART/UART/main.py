#!/usr/bin/env python3
import ev3dev.auto as ev3
from ev3dev2.button import Button
from ev3dev2.sound import Sound
import time


screen = ev3.Screen()
btn = Button()
sound = Sound()
x1=10
y1=10
x2=60
y2=20
while not btn.any():
    
    x1=x2
    y1=y2
    x2+=2
    y2+=0
    screen.draw.rectangle((x1,y1,x2,y2), fill='black')
    time.sleep(0.1)




