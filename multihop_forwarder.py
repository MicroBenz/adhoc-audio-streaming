import socket
import time
import os

broadcast_ip = '10.0.0.255'
port = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sock.bind(('', port))
maxSeq = 0
arr = []
while True:
    data, address = sock.recvfrom(1024)
    if int(data) > maxSeq:
        print 'Received from ', address
        arr.append(int(data))
        print arr
        maxSeq = int(data)
        sock.sendto(data, (broadcast_ip, port))
        time.sleep(1)