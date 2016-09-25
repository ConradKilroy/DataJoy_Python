# First the required libraries are imported:
# * `Axes3D` allows adding 3d objects to a 2d matplotlib plot.
# * The `cm` routine contains many [colour
# maps](http://wiki.scipy.org/Cookbook/Matplotlib/Show_colormaps)
# * The `pyplot` submodule from the **matplotlib** library, a python 2D
# plotting library which produces publication quality figures.  
# * The `numpy` library for efficient numeric-array manipulation
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np

# Now the points to draw the surface of a *hyperbolic paraboloid* are
# computed. Two
# [sequential
# arrays](https://www.getdatajoy.com/learn/How_to_Create_Numpy_Arrays#Sequential_Arrays)
# are created with `arange()`.
X = np.linspace(-4, 4, 80)            # points in the x axis
Y = np.linspace(-4, 4, 80)            # points in the y axis
X, Y = np.meshgrid(X, Y)              # create the "base grid"
Z = (X**2 - Y**2)/2                   # points in the z Axis

# Now we set up the plot. The function `plot_surface()` is the main command
# here; the parameters `rstride` and `cstride` control how much detail in the
# wireframe you get.
fig = plt.figure()
ax = fig.gca(projection='3d')         # set the 3d axes
ax.plot_surface(X, Y, Z, 
                rstride=3, 
                cstride=3, 
                alpha=0.3,            # transparency of the surface 
                cmap=cm.BuPu)         # colour map

# The three contour plots are added with the next code:
cset = ax.contourf(X, Y, Z, 
                   zdir='z',          # direction to project the contour
                   offset=-10,        # how "far" render the contour map
                   cmap=cm.winter)    # winter colour map

cset = ax.contourf(X, Y, Z, 
                   zdir='x', 
                   offset=-6, 
                   cmap=cm.cool)

cset = ax.contourf(X, Y, Z, 
                   zdir='y', 
                   offset=6, 
                   cmap=cm.coolwarm)

# Fine-tuning the plot. Set the axes bounds, labels and title. The
# commands `view_init()` and `dist()` determine the position of the *camera*.
ax.set_xlabel('X')
ax.set_xlim(-6, 6)
ax.set_ylabel('Y')
ax.set_ylim(-6, 6)
ax.set_zlabel('Z')
ax.set_zlim(-10, 10)

ax.set_title('3D surface and contours', va='bottom')

ax.view_init(elev=25, azim=-58)           # elevation and angle
ax.dist=12                                # distance

plt.show()
