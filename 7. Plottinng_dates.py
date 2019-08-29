import matplotlib.pyplot as plt
import numpy as np
import random
import csv
import matplotlib.dates as mdates
from datetime import datetime

dates = []
height = []

csvFile = open('example', 'r')
plot = csv.reader(csvFile)

for row in plot:
    dates.append(datetime.strptime(row[0], '%d %B %Y %H:%M:%S'))
    height.append(random.randrange(1,30))

#we cannot directly plot dates, we first need to convert timestamp to datetime object
#then this dat time object is converted to matplotlib dates and fed to plot_date()

matplotlibDate = mdates.date2num(dates)
plt.plot_date(matplotlibDate, height)
plt.show()
