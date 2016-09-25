# First, the required modules are imported. The array-manipulation module
# **numpy** and the matplotlib submodule **pyplot**, to plot 2d graphics. The
# corresponding aliases `np` and `plt` for these two modules are widely used
# conventions
import numpy as np
import matplotlib.pyplot as plt

# The data to plot are 5 means for two different groups and the corresponding
# standard deviations, the first will determine the height of the bars and the
# latter the height of the error lines. For the colours it is possible to use
# html hexadecimal notation or html colour names.
menMeans = (20, 35, 30, 35, 27)
menStd = (2, 3, 4, 1, 2)
womenMeans = (25, 32, 34, 20, 25)
womenStd = (3, 5, 2, 3, 3)


N = len(menMeans)               # number of data entries
ind = np.arange(N)              # the x locations for the groups
width = 0.35                    # bar width

fig, ax = plt.subplots()

rects1 = ax.bar(ind, menMeans,                  # data
                width,                          # bar width
                color='MediumSlateBlue',        # bar colour
                yerr=womenStd,                  # data for error bars
                error_kw={'ecolor':'Tomato',    # error-bars colour
                          'linewidth':2})       # error-bar width

rects2 = ax.bar(ind + width, womenMeans, 
                width, 
                color='Tomato', 
                yerr=womenStd, 
                error_kw={'ecolor':'MediumSlateBlue',
                          'linewidth':2})

axes = plt.gca()
axes.set_ylim([0, 41])             # y-axis bounds

# The next block of code adds some text for labels, title and axes ticks
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(ind + width)
ax.set_xticklabels(('G1', 'G2', 'G3', 'G4', 'G5'))

ax.legend((rects1[0], rects2[0]), ('Men', 'Women'))

# This function prints the data on top of each bar with `text()`, it 
# takes as arguments the x, y coordinates, the text itself and two alignment
# parameters.
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center',            # vertical alignment
                va='bottom'             # horizontal alignment
                )

autolabel(rects1)
autolabel(rects2)

plt.show()                              # render the plot
