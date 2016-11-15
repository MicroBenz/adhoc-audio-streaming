import pyaudio
import socket
import time
from threading import Thread

frames = []
client_ip = '10.0.0.3'
server_ip = '10.0.0.4'
port = 12345

def udpStream(CHUNK):

    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    udp.bind((client_ip, port))
    udp.settimeout(0.1)
    soundData = ""
    count=0
    while True:
        isTimeout=False
        try:
            soundData, addr = udp.recvfrom(CHUNK * CHANNELS * 2)
        except socket.timeout,e:
            print "time out"
            isTimeout = True
        
        if soundData and not isTimeout:
            count+=1
            print count
            udp.sendto(soundData, (server_ip, port))
            frames.append(soundData)

    udp.close()

def play(stream, CHUNK):
    BUFFER = 10
    while True:
            if len(frames) == BUFFER:
                while True:
                    if len(frames) == 0:
                        break
                    stream.write(frames.pop(0))

if __name__ == "__main__":

    p = pyaudio.PyAudio()

    FORMAT = pyaudio.paInt16
    CHUNK = 1024
    CHANNELS = 2
    RATE = 44100

    stream = p.open(format=FORMAT,
                    channels = CHANNELS,
                    rate = RATE,
                    output = True,
                    frames_per_buffer = CHUNK,
                    )
    time.sleep(2)
    threadStream = Thread(target = udpStream, args=(CHUNK,))
    threadPlay = Thread(target = play, args=(stream, CHUNK,))
    threadStream.setDaemon(True)
    threadPlay.setDaemon(True)
    threadStream.start()
    threadPlay.start()
    threadStream.join()
    threadPlay.join()