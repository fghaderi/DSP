# -*- coding: utf-8 -*-
import numpy as np
import scipy.signal as sig
import matplotlib.pylab as plt

def ideallp(omc, M):
    n = np.arange(M+1) - M/2
    h = (omc/np.pi)/np.ones((n.shape))
    ind = ~(n ==0)
    h[ind] = np.sin(omc*n[ind])/(np.pi*n[ind])
    return h




wp = 0.25*np.pi
ws = 0.35*np.pi
Ap = 0.1
As = 50

deltap = (10**(Ap/20)-1)/(10**(Ap/20)+1)
deltas = (1+deltap)/(10**(As/20))
delta = min(deltap,deltas)
A = -20*np.log10(delta)


Deltaw = ws-wp
omegac = (ws+wp)/2

L = np.ceil(6.6*np.pi/Deltaw)+1
M=L-1 #  Window length and order

hd = ideallp(omegac,M)
h = hd*sig.hamming(L)

nfft = 512
H = np.fft.fft(h, nfft)

plt.figure(1)
plt.stem(h)

plt.figure(2)
#plt.plot(np.arange(nfft/2.)/(nfft/2.), 20*np.log10(abs(H[:nfft/2])))
plt.plot(20*np.log10(abs(H)))
plt.show()
