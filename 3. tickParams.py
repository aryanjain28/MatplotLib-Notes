import matplotlib.pyplot as plt

fig = plt.figure(figsize=(9,3))
myAxes = fig.add_subplot(111)

myAxes.plot([1,2,3,4,5,6,7,8,9],[1,4,9,16,25,36,49,64,81])

myAxes.tick_params(

    axis='both',        #x, y, both
    which = 'both',      #major, minor, both
    direction = 'inout',     #in, out, inout
    length = 5,
    width = 2,
    color = 'r',
    pad = 5.0,
    labelsize = 8,
    labelcolor= 'b',
    labelrotation = 12,
    bottom = False,
    top = True,
    labelleft = True,
    labelright = True,
    grid_color = 'k'
)

plt.show()
