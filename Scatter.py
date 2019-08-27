import matplotlib.pyplot as plt

x=[1,2,3,4,5,6,7,8]
y=[5,6,7,8,6,4,3,2]

plt.scatter(x,y,label='Scatter baby!',  marker='^', s=150, edgecolors='k', linewidths=1, c='r')
plt.xlabel('X-axis')
plt.ylabel('Y-label')
plt.title('Scattering!')

plt.legend()

plt.show()

import matplotlib.pyplot as plt
# 
# day = [1,2,3,4,5,6,7]
# 
# coding =    [8,8,7,6,9,12,11]
# sleeping =  [6,7,5,8,6,4,3]
# soccer =    [1,2,3,1,2,3,3]
# college =   [9,7,9,9,7,5,7]
# 
# plt.stackplot(
#     day, 
#     coding,sleeping,soccer,college, 
#     colors=['m','c','y','k'], 
#     baseline='wiggle', 
#     labels=('Coding','Sleeping','Soccer','College')
# )
# 
# plt.legend()
# plt.show()
