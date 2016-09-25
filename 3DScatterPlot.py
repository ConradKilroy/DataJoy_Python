# First, the required modules are imported. The array-manipulation
# module**numpy**, the matplotlib submodule **pyplot** and the 3d graphics
# object `axes3d` from the submodule **mplot3d**. The corresponding aliases 
# `np`,  `plt` for these modules are widely used conventions.
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

# Now we read the data from a csv file with `genfromtxt()`.
thedata = np.genfromtxt(
                        '3DScatterPlot.csv',      # file name
                        delimiter='\t',         # column delimiter
                        dtype='int',            # data type
                        usecols = (0,1,2),      # use firs 3 columns only
                        names=['a','b','c']     # column names
                        )

# The code below will set up the plot, adding the title, axes labels, axes limits and
# the angle and distance of the *camera* from the plot.

fig = plt.figure()
ax = fig.gca(projection='3d')

ax.set_title('3D Scatter Plot')
ax.set_xlabel('Column a')
ax.set_ylabel('Column b')
ax.set_zlabel('Column c')

ax.set_xlim(-6, 56)
ax.set_ylim(-6, 66)
ax.set_zlim(-6, 76)

ax.view_init(elev=12, azim=40)              # elevation and angle
ax.dist=12                                  # distance
                        
# Finally, the plot is created with `scatter()`, manually adjusting the marker
# shape and colour.
ax.scatter(
           thedata['a'], thedata['b'], thedata['c'],  # data
           color='purple',                            # marker colour
           marker='o',                                # marker shape
           s=30                                       # marker size
           )

plt.show()                                            # render the plot
