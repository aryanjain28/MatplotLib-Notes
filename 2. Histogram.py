import matplotlib.pyplot as plt
import numpy as np
import random

x = [21,22,23,4,5,6,77,8,9,10,31,32,33,34,35,36,37,18,49,50,100]
bins = 5    #it kind of tells the number of pillars in histogram

plt.hist(x, bins,edgecolor='white')
plt.show()

#companyGrowth = [random.randrange(50,120) for _ in range(30)]
#
# print(sorted(companyGrowth))
#
# n, bins, patches = plt.hist(companyGrowth, 20, edgecolor='black', facecolor='yellow',linewidth=1, linestyle='-')
#
# for i in range(0, len(patches)):
#     print(str(patches[i].xy[0])+"  "+str(patches[i]))
#
#
# plt.plot(
#     [int(patches[i].xy[0]) for i in range(len(patches))],
#     [int(patches[i].get_height()) for i in range(len(patches))],
#     'r--'
# )
#
# plt.show()
