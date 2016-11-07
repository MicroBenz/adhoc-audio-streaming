import socket
import time
import os
import pyaudio
import array
import threading

broadcast_ip = '10.0.0.255'
port = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sock.bind(('', port))

p = pyaudio.PyAudio()
stream = p.open(format=p.get_format_from_width(1), channels=2, rate=24000, output=True)

maxSeq = 0
arr = []

def play():
    global arr
    print 'play'
    while len(arr) != 0:
        if len(arr) > 200:
            sound = ''.join(arr)
            stream.write(sound)
            # arr = arr[2:]
            arr = []

t1 = threading.Thread(target=play)
t1.start()

while True:
    # data, address = sock.recvfrom(1024)
    # seqNumber, chunk = data.split('!|!')
    # if int(seqNumber) > maxSeq:
    #     print 'Received from ', address
    #     raw = array.array('B')
    #     raw.fromstring(chunk)
    #     stream.write(raw)        
    #     # arr.append(chunk)
    #     maxSeq = int(seqNumber)
    #     sock.sendto(data, (broadcast_ip, port))
    data, _ = sock.recvfrom(1024)
    arr.append(data)

    
    # arr.append(1)