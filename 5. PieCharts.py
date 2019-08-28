import matplotlib.pyplot as plt
import numpy as np

activity = ['Sleeping', 'Soccer', 'Code', 'Eating']
time = ['8','5','7','5']
colors = ['m','b','r','c']

plt.pie(
    time,
    labels=activity,
    colors=colors,
    startangle=0,
    counterclock=True,
    shadow=True,
    frame=False,
    explode=(0.05,0.05,0.05,0.05),
    autopct='%1.1f%%',
    wedgeprops= {'linewidth':3},
    rotatelabels=False
)

plt.show()
