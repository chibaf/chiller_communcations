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
#get_temp = b'0x04'+b'0x30'+b'0x30'+b'0x53'+b'0x31'+b'0x05'
get_temp = b'\x04\x30\x30\x53\x31\x05'
#get_temp = b'0x040x300x300x530x310x05'
print(get_temp)
ser.write(get_temp)
line = ser.readline()  
print(line)
line2 = line.strip().decode("utf-8")
#print(line2)
b=line2.split()
print(b[1][:-1])
#print(b)
#exit()
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
print(bytes(hex(ord(e[0])).encode()))
print(bytes(hex(ord(e[1])).encode()))
print(bytes(hex(ord(e[2])).encode()))
print(bytes(hex(ord(e[3])).encode()))
print(bytes(hex(bcc).encode()))
f0=bytes(hex(ord(e[0])).encode())
f0=str(hex(ord(e[0])))
#f0[0]=b'0x92'
print(f0)
#exit()
f1=bytes(hex(ord(e[1])).encode())
f2=bytes(hex(ord(e[2])).encode())
f3=bytes(hex(ord(e[3])).encode())
f4=bytes(hex(bcc).encode())
#ff=f0+f1+f2+f3+f4
#print(ff)
#exit()
#set_temp=b'0x04'+b'0x30'+b'0x30'+b'0x02'+b'0x53'+b'0x31'+b'0x20'+b'0x20'+b'0x20'+b'0x20'+f0+f1+f2+f3+f4
#set_temp=b'\x04\x30\x30\x02\x53\x31'+b'\x20\x20\x20\x20'+ff+
set_temp=b'\x04\x30\x30\x02\x53\x31'+b'\x20\x20\x20\x20'+hex(ord(e[0])).encode()+hex(ord(e[1])).encode()+hex(ord(e[2])).encode()+hex(ord(e[3])).encode()+hex(bcc).encode()
#set_temp=ff
print(set_temp)#,type(set_temp))
ser.write(set_temp)
line = ser.readline()  
print(line)
line2 = line.strip().decode("utf-8")
print(line2) # return code from chiller
#
# get temperature
get_temp = b'\x04\x30\x30\x53\x31\x05'
print(get_temp)
ser.write(get_temp)
line = ser.readline()  
print(line)
line2 = line.strip().decode("utf-8")
print(line2)
