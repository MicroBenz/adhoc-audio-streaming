import pyaudio
import socket
from threading import Thread
import sys
import wave

frames = []

broadcast_ip = '10.0.0.1'
port = 12345

def udpStream():
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
    udp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  
    # udp.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    udp.bind((broadcast_ip, port))
    # print 
    while True:
        if len(frames) > 0:
            udp.sendto(frames.pop(0), (broadcast_ip, port))

    udp.close()

def record(stream, CHUNK):    
    while True:
        frames.append(wf.readframes(CHUNK))

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Plays a wave file.\n\nUsage: %s filename.wav" % sys.argv[0])
        sys.exit(-1)

    wf = wave.open(sys.argv[1], 'rb')

    p = pyaudio.PyAudio()

    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100

    # CHUNK = 1024
    # FORMAT = p.get_format_from_width(1)
    # CHANNELS = 2
    # RATE = 24000

    

    stream = p.open(format = FORMAT,
                    channels = CHANNELS,
                    rate = RATE,
                    input = True,
                    frames_per_buffer = CHUNK,
                    )

    # read data
    frame = wf.readframes(CHUNK)

    Tr = Thread(target = record, args = (stream, CHUNK,))
    # Tr2 = Thread(target = record, args = (stream, CHUNK,))
    # Tr3 = Thread(target = record, args = (stream, CHUNK,))
    Ts = Thread(target = udpStream)
    Tr.setDaemon(True)
    # Tr2.setDaemon(True)
    # Tr3.setDaemon(True)
    Ts.setDaemon(True)
    Tr.start()
    # Tr2.start()
    # Tr3.start()
    Ts.start()
    Tr.join()
    # Tr2.join()
    # Tr3.join()
    Ts.join()