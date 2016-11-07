#################################################################
###     Starter is initiate audio streaming                   ###
###     Will split wave file to chunk and sending them        ###
#################################################################

import socket, wave, sys, time, pyaudio

if len(sys.argv) < 2:
    print 'Need one params.\nUsage: %s wavefile.wav' % sys.argv[0]
    sys.exit(-1)

wave_file = wave.open(sys.argv[1], 'rb')
broadcast_ip = '10.0.0.255'
port = 12345

print wave_file.getsampwidth()
print wave_file.getnchannels()
print wave_file.getframerate()
# p = pyaudio.PyAudio()
# stream = p.open(format=p.get_format_from_width(1), channels=2, rate=24000, output=True)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
# sock.bind(('10.0.0.255', 0))
seqNumber = 0
count = 0
while True:
    chunk = wave_file.readframes(256)
    if not chunk:
        print 'LAST CHUNK', count
        break
    else:
        sock.sendto(chunk, (broadcast_ip, port))
        seqNumber += 1
        count += 1
        time.sleep(0.001)
    # sock.sendall(wave_file.readframes(1024))
