import pyaudio
import socket
from threading import Thread
import sys
import wave

frames = []

client_ip = '10.0.0.1'
server_ip = '10.0.0.3'
port = 12345

def udpStream():
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
    udp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  
    udp.bind((client_ip, port))
    while True:
        if len(frames) > 0:
            udp.sendto(frames.pop(0), (server_ip, port))

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

    stream = p.open(format = FORMAT,
                    channels = CHANNELS,
                    rate = RATE,
                    input = True,
                    frames_per_buffer = CHUNK,
                    )

    # read data
    frame = wf.readframes(CHUNK)

    threadRecord = Thread(target = record, args = (stream, CHUNK,))
    threadStream = Thread(target = udpStream)
    threadRecord.setDaemon(True)
    threadStream.setDaemon(True)
    threadRecord.start()
    threadStream.start()
    threadRecord.join()
    threadStream.join()