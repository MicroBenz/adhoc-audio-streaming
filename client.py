import pyaudio
import socket
from threading import Thread
import sys
import wave

frames = []

def udpStream():
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
    udp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  
    # print 
    while True:
        if len(frames) > 0:
            udp.sendto(frames.pop(0), ("127.0.0.1", 12345))

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
                    # frames_per_buffer = CHUNK,
                    )

    # read data
    frame = wf.readframes(CHUNK)

    Tr = Thread(target = record, args = (stream, CHUNK,))
    Ts = Thread(target = udpStream)
    Tr.setDaemon(True)
    Ts.setDaemon(True)
    Tr.start()
    Ts.start()
    Tr.join()
    Ts.join()