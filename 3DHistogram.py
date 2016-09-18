# The first step is to import the needed packages. The aliases `plt` and `np`
# are python coding conventions.
# * `Axes3D` allows adding 3d objects to a 2d matplotlib plot.
# * The `pyplot` submodule from the **matplotlib** library, a python 2D
# plotting library which produces publication quality figures.  
# * The `numpy` library for efficient numeric-array manipulation
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


# Read the data from a *csv* file and store it in `thedata`. The data is 
# grouped in two columns.
thedata = np.genfromtxt(
                        '3DHistogramdata.csv',       # file to read
                        skip_header=0,      # lines to skip at the top
                        skip_footer=0,      # lines to skip at the bottom 
                        delimiter=',',      # column delimiter
                        dtype='float32'     # data type
                        )
                        
x = thedata[:,0]    # data from the first column
y = thedata[:,1]    # data from the second column

# Te next chunk of code will compute the points on the corners of the boxes and
# the height of each bar with `histogram2d()`. The important option to notice
# is`bins=4`, which will draw the bivariate histogram in a 4 x 4 grid, a
# 2-tuple can be used instead to manually set the number of bars to add on each
# dimension. If the number of bins is changed the arrays containing the colours
# and labels should be updated to match the shape of the grid. The arrays
# `xpos` and `ypos` are *shrunk* versions of the original edges, to keep the
# bars apart by 0.25, which makes them look better.
hist, xedges, yedges = np.histogram2d(x, y, bins=4)

elements = (len(xedges) - 1) * (len(yedges) - 1)    # number of boxes
xpos, ypos = np.meshgrid(xedges[:-1]+0.25, yedges[:-1]+0.25)
xpos = xpos.flatten()           # x-coordinates of the bars
ypos = ypos.flatten()           # y-coordinates of the bars
zpos = np.zeros(elements)       # zero-array
dx = 0.5 * np.ones_like(zpos)   # length of the bars along the x-axis
dy = dx.copy()                  # length of the bars along the y-axis
dz = hist.flatten()             # height of the bars

# The code below will draw the plot by means of the `bar3d()` function using
# the data computed above.

fig = plt.figure()
ax = Axes3D(fig)

bar_colors = ['red', 'green', 'blue', 'aqua',
          'burlywood', 'cadetblue', 'chocolate', 'cornflowerblue',
          'crimson', 'darkcyan', 'darkgoldenrod', 'darkgreen',
          'purple', 'darkred', 'darkslateblue', 'darkviolet']


boxes = []
for thecolor in bar_colors:
    boxes.append(plt.Rectangle((0, 0), 1, 1, fc=thecolor)) # set legend colours

legends = ['label1', 'label2', 'label3', 'label4',
           'label5', 'label6', 'label7', 'label8',
           'label9', 'label10', 'label11', 'label12',
           'label12', 'label14', 'label15', 'label16']

ax.legend(boxes, legends)       # adds the legend labels

ax.bar3d(xpos, ypos, zpos,      # lower corner coordinates
         dx, dy, dz,            # width, depth and height
         color=bar_colors,      # bar colour
         alpha=0.6              # transparency of the bars
         )

ax.w_xaxis.set_ticklabels([])   # remove x-axis tick labels
ax.w_yaxis.set_ticklabels([])   # remove y-axis tick labels
ax.set_title('3D Histogram')    # title

ax.view_init(elev=28, azim=60)  # camera elevation and angle
ax.dist=12                      # camera distance

plt.show()                      # display the plot
