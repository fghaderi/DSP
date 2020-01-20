import numpy as np
from scipy import signal
import matplotlib.pyplot as plt


bpass = signal.remez(72, [0, 0.1, 0.2, 0.4, 0.45, 0.5], [0, 1, 0])
#bpass = signal.remez(50, [0, 0.2, 0.3, 0.5], [1, 0])

freq, response = signal.freqz(bpass)
ampl = np.abs(response)
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.semilogy(freq/(2*np.pi), ampl, 'b-')  # freq in Hz
plt.show()