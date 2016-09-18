# First the required libraries are imported:
# * `Axes3D` allows adding 3d objects to a 2d matplotlib plot.
# * The `rcPArams` method to customize the legend font size.
# * The `pyplot` submodule from the **matplotlib** library, a python 2D
# plotting library which produces publication quality figures.  
# * The `numpy` library for efficient numeric-array manipulation
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import rcParams
import matplotlib.pyplot as plt
import numpy as np

# First, we set up the data to plot. This will create a spiral whirling around
# the z-axis. The `linspace()` function creates 300 points evenly spaced
# between -4pi and 4pi.
theta = np.linspace(-4 * np.pi, 4 * np.pi, 300)
x = np.cos(theta)
y = np.sin(theta)

# To create the plot a new set of 3D-axes is created, afterwards the `plot()`
# routine is used with a few extra parameters to tune up its appearance. For
# the colour of the curve it is possible to use either **html colour names**,
# **html hexadecimal** codes or 3-tuples representing **rgb values**.
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(x, y, theta, 
        label = 'Parametric Curve', # label of the curve
        color = 'DarkMagenta',      # colour of the curve
        linewidth = 3.2,            # thickness of the line
        linestyle = '--'            # available styles - -- -. :
        )
rcParams['legend.fontsize'] = 11    # legend font size
ax.legend()                         # adds the legend

# The code below sets the axes bounds and the axes labels.
ax.set_xlabel('X axis')
ax.set_xlim(-1.2, 1.2)
ax.set_ylabel('Y axis')
ax.set_ylim(-1.2, 1.2)
ax.set_zlabel('Z axis')
ax.set_zlim(-4*np.pi, 4*np.pi)

# Finally the plot title, the camera elevation, angle and distance are set.
ax.set_title('3D line plot,\n parametric curve', va='bottom')

ax.view_init(elev=18, azim=-27)             # camera elevation and angle 
ax.dist=9                                   # camera distance
plt.show()                                  # display the plot
