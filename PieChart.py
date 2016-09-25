# The next command imports the **pyplot** plotting framework with the alias
# `plt`.

import matplotlib.pyplot as plt

# The code below will create the pie chart. The percentages are automatically
# computed, the slices will be ordered and plotted counter-clockwise and the
# default starting angle will be rotated 70 degrees.  For the colours it is
# possible to use html hexadecimal notation or html colour names.
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
colors = ['yellowgreen', 'mediumpurple', 'lightskyblue', 'lightcoral'] 
explode = (0, 0.1, 0, 0)    # proportion with which to offset each wedge

plt.pie(sizes,              # data
        explode=explode,    # offset parameters 
        labels=labels,      # slice labels
        colors=colors,      # array of colours
        autopct='%1.1f%%',  # print the values inside the wedges
        shadow=True,        # enable shadow
        startangle=70       # starting angle
        )
        
# Now we set aspect ratio to `equal` to make sure the pie is drawn as a circle,
# the plot is rendered afterwards.
plt.axis('equal')

plt.show()
