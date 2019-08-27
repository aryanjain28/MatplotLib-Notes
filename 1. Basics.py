import matplotlib.pyplot as plt

#plt.plot([1,2,3,4])     #if we give single list in plot function it takes it as Y-values and generates
                        #corresponding X-values with first value of x being 0.
                        #Therefore we get a graph with (0,1)(1,2)(2,3)(3,4) as co-ordinates.
#plt.show()

#plt.plot([1,2,3,4],[1,4,9,16])    #coordinates as X and Y
#plt.xlabel('Some numbers...')
#plt.ylabel('Some more numbers...')
#plt.show()

# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'c-', linewidth=2, label='X-axis')    #here c- means that color is cyan and linestyle is solid
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'rx', markersize=12)
# plt.show()

# plt.plot([1,2,3,4,5],[1,8,27,64,125],'k-',linewidth=2)        #params :: Xcoordinates, Ycoordinates, (k==blackcolor -==solidline), linewidth
# plt.plot([1,2,3,4,5],[80,80,80,80,80],'c:')
# plt.plot([1,2,3,4,5],[60,60,60,60,80],'ro',markersize=10)
# plt.xlabel('Some numbers..')
# plt.ylabel('Some more numbers..')
# plt.axis([0,6,-5,130])         #params :: minX, maxX, minY, maxY
# plt.show()

# t = numpy.arange(0,5,0.2)
# plt.plot(t,t,'r--', t, t**2, 'bs', t, t**3, 'g^')       #we can even plot multiple values in one plot
# plt.show()

# names = ['A', 'B', 'C']
# values = [1,10,100]
# 
# plt.figure(figsize=(7 ,7))      #decides the size of figure
# 
# plt.subplot(321)                #creates a grid with 3 rows and 2 coloumns and index number accordingly
# plt.bar(names, values)
# 
# plt.subplot(324)
# plt.plot(names, values)
# 
# plt.subplot(325)
# plt.scatter(names, values)
# 
# plt.suptitle("Categorical plots")
# list1 = []
# list2 = []
#
# [list1.append(x) for x in range(0,25)]
# [list2.append(x**4) for x in range(0,25)]
#
# plt.figure(figsize=(9,9))
#
# plt.subplot(132)
# plt.plot(list1, list2, label='Line!')
#
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
#
# plt.legend()
#
# plt.title("This is a\ngreat graph!!\n")
#
# plt.show()


