# -*- coding: utf-8 -*-
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt


N,Omegac = signal.buttord(2*np.pi*40,2*np.pi*50,1,30,analog = True)
Fc = Omegac/(2*np.pi)
C,D = signal.butter(N, Omegac, analog = True);


w, h = signal.freqs(C, D)

plt.figure(1)
plt.plot(w/(2*np.pi), abs(h))
plt.axvline(40, color='green') 
plt.axvline(50, color='green') 
plt.axhline(0.707, color='green') 
plt.axhline(1, color='green')
plt.xlim(0,100)

plt.title('Magnitude Response')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Amplitude [dB]')

plt.show()

plt.figure(2)
plt.plot(w/(2*np.pi), 20 * np.log10(abs(h)))
plt.axvline(40, color='green') 
plt.axvline(50, color='green') 
plt.axhline(0, color='green') 
plt.axhline(-30, color='green')
plt.ylim(-80, 0)
plt.xlim(0,100)

plt.title('Log-Magnitude Response')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Amplitude [dB]')
plt.show()

group_delay = -np.diff(np.unwrap(np.angle(h))) / np.diff(w)

plt.figure(3)
plt.plot(w[:group_delay.shape[0]]/(2*np.pi), group_delay)
plt.axvline(40, color='green') 
plt.axvline(50, color='green') 
plt.axhline(.1, color='green') 
plt.axhline(0.05, color='green')
plt.xlim(0,100)
plt.show()


N, Wn = signal.cheb1ord(2*np.pi*40, 2*np.pi*50, 1, 30 , True)
Fc = Wn/(2*np.pi)

b, a = signal.cheby1(N, 1, Wn, 'low', analog=True)

w, h = signal.freqs(b,a)

plt.figure(4)
plt.plot(w/(2*np.pi), abs(h))
plt.axvline(40, color='green') 
plt.axvline(50, color='green') 
plt.axhline(0.707, color='green') 
plt.axhline(1, color='green')
plt.xlim(0,100)

plt.title('Magnitude Response')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Amplitude [dB]')

plt.show()

plt.figure(5)
plt.plot(w/(2*np.pi), 20 * np.log10(abs(h)))
plt.axvline(40, color='green') 
plt.axvline(50, color='green') 
plt.axhline(0, color='green') 
plt.axhline(-30, color='green')
plt.ylim(-80, 0)
plt.xlim(0,100)

plt.title('Log-Magnitude Response')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Amplitude [dB]')
plt.show()

group_delay = -np.diff(np.unwrap(np.angle(h))) / np.diff(w)

plt.figure(6)
plt.plot(w[:group_delay.shape[0]]/(2*np.pi), group_delay)
plt.axvline(40, color='green') 
plt.axvline(50, color='green') 
plt.axhline(.1, color='green') 
plt.axhline(0.05, color='green')
plt.xlim(0,100)
plt.show()

