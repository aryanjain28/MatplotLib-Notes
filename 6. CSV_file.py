import matplotlib.pyplot as plt
import numpy as np
import csv

plt.figure(figsize=(9,5))

plt.subplot(121)

x = []
y = []

with open('example', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.plot(x, y, 'r',label="loaded from file")

plt.xlabel('X')
plt.ylabel('Y')
plt.title("Graph 1")
plt.legend()


plt.subplot(122)

x, y = np.loadtxt('example', delimiter=',', unpack=True)

plt.plot(x, y, label="loaded from file")

plt.xlabel('X')
plt.ylabel('Y')
plt.title("Graph 2")
plt.legend()
plt.show()
