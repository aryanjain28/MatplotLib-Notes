import matplotlib.pyplot as plt
import numpy as np
import csv
import matplotlib.dates as mdates
from datetime import datetime


dateString1 = '28 December, 1997'
dateObject1 = datetime.strptime(dateString1, '%d %B, %Y')
#Here, %d is used for numerical date === 1,2,3,4....
#Here, %B is used for month name full === January, February....
#Here, %Y is used for 4-digit year === 2019,2014,3091,4043....
print(dateObject1)



dateString2 = '20181228'
dateObject2 = datetime.strptime(dateString2, '%Y%m%d')
#Here, %B is used for month digit === 1,2,3,4.....11,12
print(dateObject2)


dateString3 = '21 March, 1997 11:40:56'
dateObject3 = datetime.strptime(dateString3, '%d %B, %Y %H:%M:%S')
#Here, %H is used for Hours..
#Here, %M is used for Minutes....
#Here, %S is used for Seconds...
print(dateObject3)


dateString4 = '20170214011645'
dateObject4 = datetime.strptime(dateString4, '%Y%m%d%H%M%S')
print(dateObject4)
