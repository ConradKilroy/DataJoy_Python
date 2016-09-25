# First, the required modules are imported. The array-manipulation module
# **numpy** and the **matplotlib** submodule **pyplot**, to plot 2d graphics.
# The corresponding aliases np and plt for these two modules are widely used
# conventions.
import numpy as np
import matplotlib.pyplot as plt

# Now the coordinates for both graphs are computed
theta = np.linspace(-np.pi, np.pi, 100)  
r1 = 1 - np.sin(3*theta)
r2 = 1 + np.cos(theta)

# The code below creates the plot, the colour for several elements can be set
# using html hexadecimal codes or html colour names.

ax = plt.subplot(111, polar=True,      # add subplot in polar coordinates 
                 axisbg='Azure')       # background colour

ax.set_rmax(2.2)                       # r maximum value
ax.grid(True)                          # add the grid
                 
ax.plot(theta, r1,
        color='Tomato',                # line colour
        ls='--',                       # line style
        lw=3,                          # line width
        label='a 3-fold curve')        # label

ax.plot(theta, r2, 
        color='purple',
        linewidth=3,
        ls = '-',
        label = 'a cardioid')
        
# Lastly, the legend and title are added. A dictionary with the font
# attributes is used to configure the title font.
ax.legend(loc="lower right")           # legend location

titlefont = {
        'family' : 'serif',
        'color'  : 'black',
        'weight' : 'bold',
        'size'   : 16,
        }

ax.set_title("A plot in polar coordinates", # title
             va='bottom',                   # some space below the title
             fontdict = titlefont           # set the font properties
             )

plt.show()
