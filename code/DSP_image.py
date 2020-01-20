from PIL import Image as img
import webbrowser
import numpy as np
from matplotlib import pyplot as plt
from scipy import ndimage
from scipy import signal as sig
from copy import deepcopy
#plt.imshow(np.random.randn(100,100))
#plt.show()

m = 5.0
n = m
mask = 1./(m*n)*np.ones((m, n))

#im = img.open("C:\Users\TECHNOSUN\Dropbox\Lectures\DSP\Python\DSP.png")
im = img.open("C:\Users\SONY\Dropbox\Lectures\DSP\Python\DSP.png")


pixels = np.array(im.getdata())
p = np.reshape(pixels, (100, 300))



#print p.shape, p2.shape
plt.figure(1)
plt.imshow(p, cmap = plt.get_cmap('gray'), vmin = 0, vmax = 255)
plt.show()

r = 10.0

p1 = ndimage.zoom(p, 1/r)
plt.figure(2)
plt.imshow(p1, cmap = plt.get_cmap('gray'), vmin = 0, vmax = 255)
plt.show()

p2 = ndimage.zoom(p1, r)
plt.figure(3)
plt.imshow(p2, cmap = plt.get_cmap('gray'), vmin = 0, vmax = 255)
plt.show()




#pf = sig.convolve2d(p, mask)

ps  = 255*np.ones((p.shape[0]+((m-1)/2)*2, p.shape[1]+((m-1)/2)*2))
ps[(m-1)/2:-(m-1)/2, (m-1)/2:-(m-1)/2] = deepcopy(p)
psf = sig.convolve2d(ps, mask)
#pf2 = psf[(m-1)/2+1:-(m-1)/2-1, (m-1)/2+1:-(m-1)/2-1]

pf2 = psf[(m-1):-(m-1), (m-1):-(m-1)]


plt.figure(4)
plt.imshow(pf2, cmap = plt.get_cmap('gray'), vmin = 0, vmax = 255)
plt.show()


r = 10.0

pfs1 = ndimage.zoom(pf2, 1/r)
plt.figure(5)
plt.imshow(pfs1, cmap = plt.get_cmap('gray'), vmin = 0, vmax = 255)
plt.show()

r = 10.0

pfs2 = ndimage.zoom(pfs1, r)
plt.figure(6)
plt.imshow(pfs2, cmap = plt.get_cmap('gray'), vmin = 0, vmax = 255)
plt.show()

"""
p2 = ndimage.zoom(pf2, r)
plt.figure(7)
plt.imshow(p2, cmap = plt.get_cmap('gray'), vmin = 0, vmax = 255)
plt.show()
"""

