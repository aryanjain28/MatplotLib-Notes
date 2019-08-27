import matplotlib.pyplot as plt
import numpy as np
import random

x = [21,22,23,4,5,6,77,8,9,10,31,32,33,34,35,36,37,18,49,50,100]
bins = 5

print(sorted(x))

plt.hist(x, bins,edgecolor='white')
plt.show()
