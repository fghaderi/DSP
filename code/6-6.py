# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pylab as plt
from copy import deepcopy

B = 10
Fs = B
tau = 10
dt = 1e-4
t = np.arange(0.0, tau, dt)

xc = np.sin(np.pi*B*t**2/tau)

nT = np.arange(0.0, tau, 1.0/Fs)

xn = np.sin(np.pi*B*nT**2/tau)


ind = B*t/tau > Fs/2.0
yr = deepcopy(xc)
yr[ind] = -np.sin(2.0*np.pi*(Fs-B*t[ind]/tau/2.0)*t[ind])

f, axarr = plt.subplots(3)
axarr[0].plot(t,xc)

axarr[1].plot(nT,xn, ".-")

axarr[2].plot(t,yr)
axarr[2].plot(nT,xn, ".")

plt.show()


