#!/usr/bin/env python3

import serial
s=serial.Serial("/dev/ttyACM0",115200)
print(s.read(100))
