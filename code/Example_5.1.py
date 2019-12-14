import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig

#f = .209
f = 0.02  # 0.05 =2*pi/20
a = 0.8
b = 1-np.abs(a)
n = np.arange(0, 100)
x = np.sin(2*np.pi*f*n)

y = np.zeros_like(x)

for i in range(x.shape[0]-1):    
    y[i+1] = a*y[i]+b*x[i+1]
"""
plt.plot(x, '.-')
plt.plot(y, '.-')
plt.show()
"""


B = [b]
A = [1, -a]
[w, h] = sig.freqz(B, A)

plt.figure(2)
plt.plot(w, abs(h))
plt.plot(w, np.angle(h))
plt.show()


Z = sig.lfilter(B, A, x)
plt.figure(3)
plt.plot(x, '.-')
plt.plot(Z, '.-')
plt.plot(y-Z, '.-')
plt.show()

