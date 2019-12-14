import numpy as np
import pyaudio
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import scipy.signal as sig

A = 1
B = 10. #Hz
Fs = 100 #Hz
tau = 100 #s
N = tau*Fs
beta = B/Fs/N


n = np.arange(N+1)
x = np.cos(np.pi*beta*n**2)

plt.plot(x)
plt.show()

plt.figure(2)
pylab.specgram(x, NFFT=1024, Fs=Fs, noverlap=900)#, cmap=pylab.cm.gist_heat)
plt.show()

input_array = x #np.random.rand(10000000)
# instantiate PyAudio (1)
p = pyaudio.PyAudio()

# open stream (2), 2 is size in bytes of int16
stream = p.open(format=p.get_format_from_width(2),
                channels=1,
                rate=44100,
                output=True)

# play stream (3), blocking call
stream.write(input_array)

# stop stream (4)
stream.stop_stream()
stream.close()

# close PyAudio (5)
p.terminate()


a = 0.95
b = 1-np.abs(a)

B = [b]
A = [1, -a]

Z = sig.lfilter(B, A, x)
plt.figure(4)
plt.plot(x, '.-')
plt.plot(Z, '.-')
plt.show()
