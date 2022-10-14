#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.parameters import Color, Port
from pybricks.ev3devices import (Motor, TouchSensor,
          ColorSensor, UltrasonicSensor, GyroSensor)
from pybricks.tools import wait, StopWatch
import random

# Initialize the EV3
ev3 = EV3Brick()
#ev3.speaker.beep()
#motor=Motor(Port.A)

import airtable as aaa
record_id =aaa.Put_AT('Table 1','Name','Milan')  # Table 1 is table name, Name is field name and Milan is value, puts value in the end of the column and returns the record id
a=aaa.Get_AT('Table 1','Name')                   # Table 1 is table name, Name is the field name, returns the last value in the column
array=aaa.Get_AT_field('Table 1','Name')        # similar to Get_AT, but returns the whole field , user will have to parse the value [0] is first, [1] is second ,[-1] will give the last value and so on
c=aaa.Delete_AT('Table 1',record_id)             # deletes the record on Table 1 with record_id. finding record id is tricky. you can either save it while putting a value or do a list, which is not included in this library
          

print(record_id)    # prints the record id returned while updating the field    
print(a)            # prints the value of the last record of the field
print(c)            # prints the status of delete- true or false
print(array)        # prints the whole list of field 