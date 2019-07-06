import socket
import sys
from _thread import *
import servocon
#import rpi_camera_surveillance_system

host=""
port=6666
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    s.bind((host,port))
except socket.error as e:
    print(str(e))


s.listen(5)
print("Waiting for connection")

def threaded_clint(conn):
    conn.send
    while True:
        data=conn.recv(2048)
        if not data:
            break
        fd=str(data).split("""'""")
        print(fd[1])
        if('p'in fd[1]):
            print("pan")
            pval=fd[1].split("p")
            print(pval[1])
            servocon.sposition(0,int(pval[1]))
        elif('t'in fd[1]):
            tval=fd[1].split("t")
            print(tval[1])
            print("tilt")
            servocon.sposition(1,int(tval[1]))
        elif('re' in fd[1]):
            print('reset')
            servocon.reset()
        conn.sendall(str.encode("ok"))
    conn.close()

while True:
    conn, addr= s.accept()
    print("Connected to: "+addr[0]+":"+str(addr[1]))
    start_new_thread(threaded_clint,(conn,))    
