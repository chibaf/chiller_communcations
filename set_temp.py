#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import serial
import time

port='/dev/ttyUSB0'
speed=9600
timeout=1
ser = serial.Serial(port,speed,timeout=1)

request_00S1 = b'\x04\x30\x30\x02\x4A\x4F\x31\x03\x37'
ser.write(request_00S1)
line = ser.readline()  
print(line)
line2 = line.strip().decode("utf-8")
print(line2)

S1_25=b'\x04\x30\x30\x02\x53\x31\x20\x20\x20\x20\x33\x34\x2E\x30\x03\x78'
ser.write(S1_25)
line = ser.readline()  
print(line)
line2 = line.strip().decode("utf-8")
print(line2)
