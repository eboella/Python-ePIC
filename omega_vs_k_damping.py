import numpy as np   #array syntax

import pylab as plt  #plot

from matplotlib import *
from matplotlib.figure import Figure
from cmath import sqrt

interactive(True)

WP = 1

k = np.linspace(0.001,10,1000)

ld = 1

om_im = -WP * np.sqrt(np.pi/8.)*(1/(k*ld))**3*np.exp(-3./2.)*np.exp(-1/(2.*k**2*ld**2))

f = Figure(figsize=(5, 4), dpi=100)

plt.plot(k,om_im,linewidth=2)

plt.xlabel('k')

plt.ylabel('omega')

plt.show()

L = 12
mode = 1
k_sim = 2*np.pi/L*mode
om_sim = -WP * np.sqrt(np.pi/8.)*(1/(k_sim*ld))**3*np.exp(-3./2.)*np.exp(-1/(2.*k_sim**2*ld**2))

print 'Damping rate: ', om_sim

raw_input('Press enter...')
