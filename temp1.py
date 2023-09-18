#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import serial
import time
import sys

ser = serial.Serial('/dev/ttyUSB0',9600,timeout=1)
if len(sys.argv)==1:
  x=0.0
else:
  x=float(sys.argv[1])  # get increment of temperature

# get setting temperature
get_temp = b'\x04\x30\x30\x53\x31\x05'
ser.write(get_temp)  # send command to the chiller for get temp setting
line = ser.readline()  
print(line)
line2 = line.strip().decode("utf-8")
b=line2.split()
print("setting temp ",b[1][:-1])
c=float(b[1][:-2])
d=c+x
print("new setting temp=",d)
print("")

# calculation BCC
b1=0x53^0x31^0x20^0x20^0x20^0x20
e=str(d)
print(e)
e0=ord(e[0])
e1=ord(e[1])
e2=ord(e[2])
e3=ord(e[3])
bcc=b1^e0^e1^e2^e3^0x03
print(hex(bcc))

# put new setting temperature to chiller
set_temp=b'\x04\x30\x30\x02\x53\x31'+b'\x20\x20\x20\x20'+hex(ord(e[0])).encode()+hex(ord(e[1])).encode()+hex(ord(e[2])).encode()+hex(ord(e[3])).encode()+b'0x03'+hex(bcc).encode()
print(set_temp)
ser.write(set_temp)
line = ser.readline()  
print(line)
line2 = line.strip().decode("utf-8")
print(line2) # return code from chiller

# get setteing temperature of chiller
get_temp = b'\x04\x30\x30\x53\x31\x05'
print(get_temp)
ser.write(get_temp)
line = ser.readline()  
print(line)
line2 = line.strip().decode("utf-8")
print(line2)
