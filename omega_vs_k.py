import numpy as np   #array syntax

import pylab as plt  #plot

from matplotlib import *
from matplotlib.figure import Figure
from cmath import sqrt

interactive(True)

v0 = 1
WP = 1

k = np.linspace(0,2,1000)

a = np.sqrt(WP**2*(8*k**2*v0**2+WP**2))
omega = np.lib.scimath.sqrt((2*k**2*v0**2+WP**2-a)/2)

om_im = omega.imag

f = Figure(figsize=(5, 4), dpi=100)

plt.plot(k,om_im,linewidth=2)

plt.xlabel('k')

plt.ylabel('omega')

plt.show()

gamma_max = np.amax(om_im)
print 'Maximum growth rate: ', gamma_max
idx = np.argmax(om_im)
k_max = k[idx]
print 'k for maximizing growth rate: ', k_max

L = 3*2*np.pi/(np.sqrt(3.0/2)/2.)
mode = 3
k_sim = 2*np.pi/L*mode
a_sim = np.sqrt(WP**2*(8*k_sim**2*v0**2+WP**2))
omega_sim = np.lib.scimath.sqrt((2*k_sim**2*v0**2+WP**2-a_sim)/2)

print 'Growth rate: ', omega_sim

raw_input('Press enter...')
