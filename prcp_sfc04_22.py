#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 16:03:14 2024

@author: rileynewton
"""
#import necessary modules
import matplotlib.pyplot as plt
import cartopy.feature as cf
import cartopy.crs as ccrs
import pygrib

#open file and pull precipitation data (converting to inches)
grbGFS = pygrib.open ('gfs_4_20110422_1800_006.grb2')

grbGFS.select(name='Total Precipitation')
precip = grbGFS[226]; prcp = precip['values']
lats, lons=precip.latlons()

prcpIN = prcp * 0.0394

#Plot the figure and set the region to focus on the Eastern/Mid US
fig = plt.figure(figsize=(4,4))
proj=ccrs.LambertConformal(central_longitude=-96.,central_latitude=40.,standard_parallels=(40.,40.))
ax=plt.axes(projection=proj)

#add details to the map
ax.set_extent([-100.,-75.,30.,50.])
ax.add_feature(cf.LAND,color='white')
ax.add_feature(cf.OCEAN,color='lightblue')
ax.add_feature(cf.COASTLINE,edgecolor='black')
ax.add_feature(cf.STATES,edgecolor='black')
ax.add_feature(cf.BORDERS,edgecolor='black')
ax.add_feature(cf.LAKES,color='lightblue')

#input the data onto the plot and create the legend for the precipitation data
bounds = [0.1,.5,1,1.5,2]
plt.contourf(lons, lats, prcpIN, bounds, cmap='summer', transform=ccrs.PlateCarree())

cbar = plt.colorbar(location='bottom')
cbar.set_label('Precipitation (in)')

plt.savefig('prcp_sfcmap2.png')
plt.show()
plt.close

grbGFS.close()