import numpy as np

import matplotlib
matplotlib.use('TkAgg')

from matplotlib.figure import Figure

from matplotlib import interactive
interactive(True)
import matplotlib.pyplot as plt

from Tkinter import *
from tkFileDialog import *

root = Tk()
root.wm_title("Read txt file")

w = Label(root, text="Please choose a txt to read")
fileName = askopenfilename(parent=root)

M = np.loadtxt(fileName)

t = M[0,:]
data = M[1,:]

logdata = np.log(data)

f = Figure(figsize=(5, 4), dpi=100)

plt.plot(t,logdata,linewidth=2)

plt.xlim(0, t[np.size(t)-1])

plt.xlabel('t')

plt.ylabel('ln(data)')

plt.show()


raw_input('Press enter...')
