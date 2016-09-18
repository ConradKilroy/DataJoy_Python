# First the required libraries are imported:
# * `malab` library of with Matlab-compatible commands.
# * The `cm` routine contains many [colour
# maps](http://wiki.scipy.org/Cookbook/Matplotlib/Show_colormaps)
# * The `pyplot` submodule from the **matplotlib** library, a python 2D
# plotting library which produces publication quality figures.  
# * The `numpy` library for efficient numeric-array manipulation
import matplotlib
import matplotlib.mlab as mlab
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np


# The data whose contour maps will be plotted is difference of two random
# bivariate Gaussian distributions.
delta = 0.025
x = np.arange(-3.0, 3.0, delta)
y = np.arange(-2.0, 2.0, delta)
X, Y = np.meshgrid(x, y)
Z1 = mlab.bivariate_normal(X, Y, 1.0, 1.0, 0.0, 0.0)
Z2 = mlab.bivariate_normal(X, Y, 1.5, 0.5, 1, 1)
# difference of Gaussians
Z = 10.0 * (Z2 - Z1)

# The next two lines will affect all subsequent plots, they set the tick
# markers  outwards, for a better-looking output.
matplotlib.rcParams['xtick.direction'] = 'out'
matplotlib.rcParams['ytick.direction'] = 'out'
0
# ---

# Contour Plot, customized label locations, line colours and line widths
# ----------------------------------------------------------------------

# The code below will create a contour map with 6 automatically computed
# contour lines, the labels will be manually set by means of the array
# `manual_locations` which contains 6 tuples with the coordinates for each
# label. The colour of the lines is also manually set.
manual_locations = [(-1, -1.4), (-0.62, -0.7), (-2, 0.5), 
                    (1.7, 1.2), (2.0, 1.4), (2.4, 1.7)]

line_colours = ('BlueViolet', 'Crimson', 'ForestGreen', 
        'Indigo', 'Tomato', 'Maroon')

line_widths = (1, 1.5, 2, 2.5, 3, 3.5)

plt.figure()
CS = plt.contour(X, Y, Z, 6,                        # add 6 contour lines
                 linewidths=line_widths,            # line widths
                 colors = line_colours)             # line colours

plt.clabel(CS, inline=1,                            # add labels
          fontsize=10,                             # label font size 
          manual=manual_locations)                 # label locations
plt.title('Contour Plot - customized lines')        # title
# plt.show()

# ---

# Contour Plots, manual contour lines and single colours
# ------------------------------------------------------

# In the next example the contour levels to plot are explicity declared, all
# the levels are plotted in the same colour, using dashed lines for negative
# values and a fixed line width for all of them.
levels = np.arange(-1.2, 1.6, 0.4)              # contour levels

plt.figure()

matplotlib.rcParams['contour.negative_linestyle'] = 'dashed'

CS = plt.contour(Z, levels,                     # levels lot plot
                 colors='black',                # lines colour 
                 linewidths=3                   # line widths
                 )
plt.clabel(CS, fontsize=10, inline=1)           # labels
plt.title('Single color - negative dashed')
# plt.show()

# ---

# Contour Map, background colour and colour bars
# ----------------------------------------------

# This example is more complex. The levels are manually set, the colour for the
# level curves is set to `hot()` and a blue background image is added, along
# with horizontal and vertical bars.
plt.figure()

plt.hot()                                    # set 'hot' as default colour map
im = plt.imshow(Z, interpolation='bilinear', # creates background image
                origin='lower', cmap=cm.Blues, 
                extent=(-3,3,-2,2))

levels = np.arange(-1.2, 1.6, 0.2)           # levels

CS = plt.contour(Z, levels,
                 origin='lower',             # origin in lower-left corner
                 linewidths=2,               # line width
                 extent=(-3,3,-2,2))         # outer pixel boundaries

CB = plt.colorbar(CS, shrink=0.8,                 # vertical colour bar
                  extend='both')

CBI = plt.colorbar(im, orientation='horizontal',  # horizontal colour bar
             shrink=0.8)

l,b,w,h = plt.gca().get_position().bounds
ll,bb,ww,hh = CB.ax.get_position().bounds
CB.ax.set_position([ll, b+0.1*h, ww, h*0.8])      # shrinks the vertical bar

plt.title('Contour Plot - colour bars')           # title

plt.show()
