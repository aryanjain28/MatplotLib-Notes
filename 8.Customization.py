import matplotlib.pyplot as plt
import numpy as np
import random
import csv
import time
import matplotlib.dates as mdates
from datetime import datetime
import urllib.request

x = np.arange(10,210,10)
y = [20,40,20,30,20,40,20,30,20,40,20,30,20,40,20,30,20,40,20,30]


plt.figure(figsize=(19,6))


plt.xlabel(
    'X-axis',
    text='X-label',
    color='r',
    rotation=-12,
    rotation_mode='default',
    fontfamily='serif',
    fontsize='21',
    fontstretch='ultra-expanded',
    fontstyle='italic',
    fontweight='extra bold',
    verticalalignment='center',
    horizontalalignment='center',
    backgroundcolor = 'cyan',
    alpha = 0.75,
    visible = True,
    linespacing = 0.22,
    clip_on = True
)



plt.ylabel(
    'Y-axis',
    text='Y-label',
    color='b',
    rotation=12,
    rotation_mode='anchor',
    fontfamily='cursive',
    fontsize=34,
    fontstretch=23,
    fontstyle='oblique',
    fontvariant='small-caps',
    fontweight='book',
    verticalalignment='center_baseline',
    horizontalalignment='right',
    backgroundcolor='yellow',
    alpha=1.0,
    visible=True,
    linespacing=0.52

)

plt.fill([50,70,70,50],[27.5,27.5,35,35],'b',alpha=0.5)       #used to fill colors between defined coordinates
plt.fill([20,30,40],[27.5,35,27.5],'r',alpha=0.5)

plt.fill_between(x, y,y[0], alpha=0.5)
# plt.fill_between(x, y,  30,   where=(30 < y[0]), facecolor='r', alpha=0.5)              #used to fill the space inside plotted line

plt.plot(x,y,label='X')

plt.grid(True)
plt.legend()
plt.show()
