import socket
import sys
import time

c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ip=''
port=6666

def connectw(ipd):
    ip=ipd
    address=(ipd,port)
    print("connecting with : "+ip)
    c.connect(address)
    print("connected with : "+ip)

def senddata(val):
    c.sendall(str.encode(val))

    
