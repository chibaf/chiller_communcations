#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import serial
import time
import sys

port='/dev/ttyUSB0'
speed=9600
timeout=1
ser = serial.Serial(port,speed,timeout=1)
if len(sys.argv)==1:
  x=0.0
else:
  x=float(sys.argv[1])

# get temperature
get_temp = b'\x04\x30\x30\x53\x31\x05'
ser.write(get_temp)
line = ser.readline()  
#print(line)
line2 = line.strip().decode("utf-8")
#print(line2)
b=line2.split()
print(b[1][:-1])
c=float(b[1][:-2])
d=c+x
print(d)
print("###")

# set temperetue +=x
# set_temp=b'\x04\x30\x30\x02\x53\x31\x20\x20\x20\x20\x33\x34\x2E\x30\x03\x78'
b1=0x53^0x31^0x20^0x20^0x20^0x20
print(b1)
e=str(d)
print(e)
e0=ord(e[0])
e1=ord(e[1])
e2=ord(e[2])
e3=ord(e[3])
print(e0)
print(e1)
print(e2)
print(e3)
bcc=b1^e0^e1^e2^e3^0x03
print(hex(bcc))
set_temp=b'\x04\x30\x30\x02\x53\x31\x20\x20\x20\x20'+bytes(hex(ord(e[0])).encode())+bytes(hex(ord(e[1])).encode())+bytes(hex(ord(e[2])).encode())+bytes(hex(ord(e[3])).encode())+bytes(hex(bcc).encode())
print(set_temp,type(set_temp))
ser.write(set_temp)
line = ser.readline()  
print(line)
line2 = line.strip().decode("utf-8")
print(line2) # return code from chiller
#
# get temperature
get_temp = b'\x04\x30\x30\x53\x31\x05'
ser.write(get_temp)
line = ser.readline()  
print(line)
line2 = line.strip().decode("utf-8")
print(line2)
