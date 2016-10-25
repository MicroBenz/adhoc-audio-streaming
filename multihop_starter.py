import socket
import time

broadcast_ip = '10.0.0.255'
port = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
i = 0
while True:
    sock.sendto(str(i) , (broadcast_ip, port))
    i += 1
    time.sleep(1)