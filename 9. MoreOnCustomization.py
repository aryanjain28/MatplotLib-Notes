import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style
import csv
import datetime

dates = []
high = []
low = []


csvDataFile = open('example', 'r')
source = csvDataFile.read().split('\n')
csvDataFile.close()

plot = csv.reader(source)

for p in plot:
    dateObject = datetime.datetime.strptime(p[0], '%Y-%m-%d')
    dates.append(mdates.date2num(dateObject))
    high.append(p[2])
    low.append(p[3])


style.use('fivethirtyeight')
print(plt.style.available)

ax1 = plt.subplot(111)
ax1.plot_date(dates, low, 'r-')
ax1.plot_date(dates, high, 'b-')

for label in ax1.xaxis.get_ticklabels():
    label.set_rotation(45)
    label.set_size(7)
    label.set_color('r')
    label.set_backgroundcolor('yellow')
    label.set_fontfamily('serif')
    label.set_fontstyle('italic')
    label.set_fontweight('bold')

w = 0

for label in ax1.yaxis.get_ticklabels():
    label.set_size(6)
    label.set_rotation(22)
    label.set_backgroundcolor('c')
    label.set_color('b')


ax1.tick_params(left=True)
ax1.set_title('High Graph')
ax1.title.set_size(25)

plt.show()
