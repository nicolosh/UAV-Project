import threading
import socket
import sys
import time
import platform

# the drone is receiving the commands from 
# other scripts 
# and want take off ('VOLARE') with this script

host = ""
port = 9000
local_address = (host, port)

#Create UDP socket (does not matter if we loose some packages (better wrt TCIP socker/connection))
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Create a connection with the drone (bind with the drone)
sock.bind(local_address)

# stream containing the tello address ****
tello_address = ("192.168.10.1", "8889")


## Try sending something to the drone ****
#sock.sendto(b'command', local_address)
sock.sendto(b"takeoff", local_address)
#sock.sendto(b"left 25", local_address)
#sock.sendto(b"backward 25", local_address)
#sock.sendto(b"right 25", local_address)
#sock.sendto(b"forward 25", local_address)

sock.sendto(b"battery?", local_address)

# 1024 is the size of the message payload received back from the drone
response, ip = socket.recvform(1024)
print(response)

sock.sendto(b"land", local_address)
# close communication ****
sock.close()