import pyaudio
import socket
import time
from threading import Thread

frames = []
# current_milli_time=lambda: int(round(time.time()*1000))
def udpStream(CHUNK):

    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # udp.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    udp.bind(("10.0.0.3", 12345))
    udp.settimeout(0.1)
    soundData = ""
    count=0
    while True:
        # print "here"+str(len(frames))
        isTimeout=False
        try:
            soundData, addr = udp.recvfrom(CHUNK * CHANNELS * 2)
        except socket.timeout,e:
            print "time out"
            isTimeout=True
        # print soundData
        # print "there"
        
        if soundData and not isTimeout:
            count+=1
            print count
            udp.sendto(soundData, ('10.0.0.4', 12345))
            frames.append(soundData)

    udp.close()

def play(stream, CHUNK):
    BUFFER = 10
    while True:
            # print current_milli_time()
            # print len(frames)
            if len(frames) == BUFFER:
                while True:
                    # print "plaing"+str(len(frames))
                    if len(frames) == 0:
                        break
                    stream.write(frames.pop(0))

if __name__ == "__main__":

    p = pyaudio.PyAudio()

    FORMAT = pyaudio.paInt16
    CHUNK = 1024
    CHANNELS = 2
    RATE = 44100

    # CHUNK = 1024
    # FORMAT = p.get_format_from_width(1)
    # CHANNELS = 2
    # RATE = 24000

    

    stream = p.open(format=FORMAT,
                    channels = CHANNELS,
                    rate = RATE,
                    output = True,
                    frames_per_buffer = CHUNK,
                    )
    time.sleep(2)
    Ts = Thread(target = udpStream, args=(CHUNK,))
    Tp = Thread(target = play, args=(stream, CHUNK,))
    Ts.setDaemon(True)
    Tp.setDaemon(True)
    Ts.start()
    # time.sleep(0.5)
    Tp.start()
    Ts.join()
    Tp.join()