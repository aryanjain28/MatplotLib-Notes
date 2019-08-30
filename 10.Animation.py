import matplotlib.animation as animation
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

figure = plt.figure()
ax1 = plt.subplot(111)

def animate(i):
    fileData = open('example', 'r').read()
    lines = fileData.split('\n')

    xa = []
    ya = []

    for line in lines:
        x,y = line.split(',')
        xa.append(x)
        ya.append(y)

    ax1.clear()
    ax1.plot(xa, ya)

    print(xa)
    print(ya)

a = animation.FuncAnimation(figure, animate, interval=1000)
plt.show()
