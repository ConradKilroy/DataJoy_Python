# First, the required modules are imported. The array-manipulation module
# **numpy**, the matplotlib submodule **pyplot** and the map-plotting toolkit
# **basemap**.
# It is common practice to use the aliases `np` and `plt` for `numpy` and
# `pyplot` respectively.
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

# Now the map is created. It uses the *Orthographic Projection* centred at 50
# degrees latitude and -100 degrees longitude. There
# are [many other 
# projections](http://matplotlib.org/basemap/users/mapsetup.html)
# available. The `resolution` is set to `l`ow, it is also possible to draw
# `i`ntermediate, `c`rude, `h`igh and `f`ull resolution maps. The parameter 
# `area_thresh` is the minimal area, in square kilometres, for a coastline or
# lake to be included in the map.
map = Basemap(projection = 'ortho', lat_0 = 50, lon_0 = -100,
              resolution = 'l', area_thresh = 1000.)
      
# The next lines will:
# * add the coastlines
# * add the country borders
# * fill the land in the `mediumpurple` colour. Html hexadecimal notation and html
# colour names can be used here
# * draw the edge of the map projection region (the projection limb)
map.drawcoastlines()
map.drawcountries()
map.fillcontinents(color = 'mediumpurple')
map.drawmapboundary()

# Now we draw the latitude-longitude grid lines every 30 degrees.
map.drawmeridians(np.arange(0, 360, 30))
map.drawparallels(np.arange(-90, 90, 30))

# Below the latitude, longitude and names of 5 cities are added to the map.
lats = [19.4, 32.73, 38.55, 48.25]
lons = [-99.15, -117.16, -77.00, -114.21]
cities=['Mexico City','San Diego, CA',
        'Washington, DC','Whitefish, MT']
x,y = map(lons, lats)                        # compute the projection
map.plot(x, y, 'o', color='Crimson')         # add the points

for name,xpt,ypt in zip(cities,x,y):
    plt.text(xpt+50000, ypt+50000, name, 
             color='Crimson', weight='bold', fontsize=10)

# Now we make up some data to create the contour lines
nlats = 73; nlons = 145; delta = 2.*np.pi/(nlons-1)
lats = (0.5*np.pi-delta*np.indices((nlats,nlons))[0,:,:])
lons = (delta*np.indices((nlats,nlons))[1,:,:])
wave = 0.75*(np.sin(2.*lats)**8*np.cos(4.*lons))
mean = 0.5*np.cos(2.*lats)*((np.sin(2.*lats))**2 + 2.)
x, y = map(lons*180./np.pi, lats*180./np.pi)

# The next commands add the contour data over the map and display the plot.
CS = map.contour(x, y, wave+mean, 8, linewidths=1.5)

plt.show()
