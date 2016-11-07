import pyaudio
import wave
import sys

CHUNK_SIZE = 1024

if len(sys.argv) < 2:
    print("Plays a wave file.\n\nUsage: %s filename.wav" % sys.argv[0])
    sys.exit(-1)

# READ WAVE FILE
wf = wave.open(sys.argv[1], 'rb')

# instantiate PyAudio (1)
p = pyaudio.PyAudio()

# open PyAudio stream (2)
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

print wf.getsampwidth()
print wf.getnchannels()
print wf.getframerate()

while True:
    chunk = wf.readframes(CHUNK_SIZE)
    if not chunk:
        print 'LAST CHUNK'
        break
    else:
        stream.write(chunk)



# # read data
# data = wf.readframes(CHUNK)

# # play stream (3)
# while len(data) > 0:
#     stream.write(data)
#     data = wf.readframes(CHUNK)

# # stop stream (4)
# stream.stop_stream()
# stream.close()

# # close PyAudio (5)
# p.terminate()