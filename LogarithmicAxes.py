# First, the required modules are imported. The array-manipulation module
# **numpy** and the matplotlib submodule **pyplot**, to plot 2d graphics. The 
# corresponding aliases `np` and `plt` for these two modules are widely used
# python conventions. The numbers in array `t` are the points to plot on the
# x-axis.
import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0.01, 20.0, 0.01)

# ### Logarithmic Scale On The y Axis

# The command `semilogy` will enable logarithmic scale on the y-axis, the
# additional option `basey` can be used to manually set the logarithm base
plt.figure()
plt.semilogy(t, np.exp(-t/5.0), 
             color='purple', 
             linewidth = 2)
plt.title('Semilog y-axis')
plt.grid(True)


# ---

# Logarithmic Scale On The x Axis
# -------------------------------

# The command `semilogx` will enable logarithmic scale on the y-axis, the
# additional option `basex` manually sets the logarithm base to use.

plt.figure()
plt.semilogx(t, np.sin(2*np.pi*t), 
             basex=10,
             color='darkred', 
             linewidth = 0.5)
plt.title('Semilog x-axis')
plt.grid(True)

# ---

# Logarithmic Scale On Both Axes
# ------------------------------

# The command `loglog()` will use logarithmic scales on both axes, the base for
# each axes can be set with the `basex` and `basey` parameters.
plt.figure()
plt.loglog(t, 20*np.exp(-t/10.0), 
          basex=2, 
          color='darkgreen', 
          linewidth = 2)
plt.grid(True)
plt.title('log base 2 on x \n log base 10 on y')

plt.show()
