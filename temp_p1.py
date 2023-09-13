#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import serial
import time

port='/dev/ttyUSB0'
speed=9600
timeout=1
ser = serial.Serial(port,speed,timeout=1)

# get temperature
request_00S1 = b'\x04\x30\x30\x53\x31\x05'
ser.write(request_00S1)
line = ser.readline()  
print(line)
line2 = line.strip().decode("utf-8")
print(line2)
b=line2.split()
print(b[1][:-1])
c=float(b[1][:-2])
print(c+1)
print("###")

# set temperetue=34.0C
#S1_25=b'\x04\x30\x30\x02\x53\x31\x20\x20\x20\x20\x33\x34\x2E\x30\x03\x78'
#ser.write(S1_25)
#line = ser.readline()  
#print(line)
#line2 = line.strip().decode("utf-8")
#print(line2) # return code from chiller
#
# get temperature
#request_00S1 = b'\x04\x30\x30\x53\x31\x05'
#ser.write(request_00S1)
#line = ser.readline()  
#print(line)
#line2 = line.strip().decode("utf-8")
#print(line2)
