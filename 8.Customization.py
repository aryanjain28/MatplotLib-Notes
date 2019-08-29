import matplotlib.pyplot as plt
import numpy as np

x = np.arange(10,210,10)
y = [20,40,20,30,20,40,20,30,20,40,20,30,20,40,20,30,20,40,20,30]


figure, ax1 = plt.subplots(nrows=1,ncols=1)


#using axes.... (preferred!)

ax1.xaxis.label.set_color('r')
ax1.xaxis.label.set_text('X-label')
ax1.xaxis.label.set_size(15)
ax1.xaxis.label.set_rotation((12))
ax1.xaxis.label.set_fontfamily('serif')
ax1.xaxis.label.set_fontstyle('italic')
ax1.xaxis.label.set_fontweight('extra bold')
ax1.xaxis.label.set_backgroundcolor('cyan')
ax1.xaxis.label.set_verticalalignment('center')
ax1.xaxis.label.set_horizontalalignment('center')
ax1.xaxis.label.set_alpha(0.75)
ax1.xaxis.label.set_visible(True)
ax1.xaxis.label.set_linespacing(0.56)


#using plt...
#
# plt.xlabel(
#     'X-axis',
#     text='X-label',
#     color='r',
#     rotation=-12,
#     rotation_mode='default',
#     fontfamily='serif',
#     fontsize='21',
#     fontstretch='ultra-expanded',
#     fontstyle='italic',
#     fontweight='extra bold',
#     verticalalignment='center',
#     horizontalalignment='center',
#     backgroundcolor = 'cyan',
#     alpha = 0.75,
#     visible = True,
#     linespacing = 0.22,
#     clip_on = True
# )



plt.ylabel(
    'Y-axis',
    text='Y-label',
    color='b',
    rotation=12,
    rotation_mode='anchor',
    fontfamily='cursive',
    fontsize=34,
    fontstretch=23,
    fontstyle='oblique',
    fontvariant='small-caps',
    fontweight='book',
    verticalalignment='center_baseline',
    horizontalalignment='right',
    backgroundcolor='yellow',
    alpha=1.0,
    visible=True,
    linespacing=0.52

)

plt.fill([50,70,70,50],[27.5,27.5,35,35],'b',alpha=0.5)       #used to fill colors between defined coordinates
plt.fill([20,30,40],[27.5,35,27.5],'r',alpha=0.5)

plt.fill_between(x, y,y[0], alpha=0.5)          #used to fill the space inside plotted line


#spines are the lines that over which ticks are constructed
ax1.spines['left'].set_color('r')
ax1.spines['bottom'].set_color('r')
ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)
ax1.spines['bottom'].set_linewidth(5)
ax1.spines['left'].set_linewidth(5)


#axhline line draw a horizontal line
ax1.axhline(30, color='k', linewidth=2, alpha=0.65)

#axvline line draw a vertical line
ax1.axvline(50, color='k', linewidth=2, alpha=0.65)

plt.plot(x,y,label='X')
plt.grid(True)
plt.legend()
plt.show()
