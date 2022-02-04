from netCDF4 import Dataset
import matplotlib.pylab as plt
from matplotlib import cm as cm
import numpy as np
from mpl_toolkits.basemap import Basemap, addcyclic
import pandas as pd


def basemap1():
    # Set the limits of the map
    x1 = -20.
    x2 = 40.
    y1 = 32.
    y2 = 64.
    # Pick any random point
    lat = 55.1
    lon = -7.1
    # Create the object
    m = Basemap(resolution='l', projection='merc', llcrnrlat=y1, urcrnrlat=y2, llcrnrlon=x1, urcrnrlon=x2, lat_ts=(x1 + x2) / 2)
    plt.figure(figsize=(8,7))
    m.drawcoastlines(linewidth=1.0)
    m.drawcountries(linewidth=1)
    m.fillcontinents(color='gray', lake_color='aqua', alpha=0.5)
    # Select one pritification
    #m.etopo()
    #m.bluemarble()
    m.shadedrelief()

    m.drawmeridians(np.arange(0, 360, 10), labels=[False, True, True, False])
    m.drawparallels(np.arange(-90, 90, 10), labels=[False, True, True, False])
    m.drawmapscale(33, 35, 0, 40, 1000, barstyle='fancy')
    # Create points to use as a marker, everything in map coordinates
    print(' xmin {}\n xmax {}\n ymin {}\n ymax {}'.format(str(m.xmin), str(m.xmax), str(m.ymin), str(m.ymax)))
    x, y = m(lon, lat)
    m.scatter(x, y, 300, marker='D', color='red')
    plt.text(x + 200000, y - 20000, "Buncrana", color='red', size=14)
    plt.show()


def basemap2():
    fl = Dataset('air.sig995.1950.nc')
    air = fl.variables['air'][0, :, :]
    lat = fl.variables['lat'][:]
    lon = fl.variables['lon'][:]
    plt.imshow(air)
    plt.contourf(lon, lat, air, 20)
    plt.colorbar()
    plt.show()


def basemap3():
    fl = Dataset('air.sig995.1950.nc')
    air = fl.variables['air'][0, :, :]
    lat = fl.variables['lat'][:]
    lon = fl.variables['lon'][:]
    m = Basemap(projection='ortho', lat_0=45, lon_0=0, resolution='l')
    lon2, lat2 = np.meshgrid(lon, lat)
    x, y = m(lon2, lat2)
    fig = plt.figure(figsize=(15, 7))
    m.drawcoastlines()
    m.drawparallels(np.arange(-80., 81., 20.))
    m.drawmeridians(np.arange(-180., 181., 20.))
    m.drawmapboundary(fill_color='white')
    cs = m.contourf(x, y, air, 20)
    plt.title('Monthly mean SAT')
    plt.colorbar()
    plt.show()


def basemap4():
    fl = Dataset('air.sig995.1950.nc')
    air = fl.variables['air'][0, :, :]
    lat = fl.variables['lat'][:]
    lon = fl.variables['lon'][:]
    air_cyc, lon_cyc = addcyclic(air, lon)
    lon2, lat2 = np.meshgrid(lon_cyc, lat)

    m = Basemap(projection='cyl', llcrnrlat=-90, urcrnrlat=90, llcrnrlon=0, urcrnrlon=360, resolution='c')
    x, y = m(lon2, lat2)

    fig = plt.figure(figsize=(10, 7))
    m.drawcoastlines()
    m.drawparallels(np.arange(-80., 81., 20.))
    m.drawmeridians(np.arange(-180., 181., 20.))
    m.drawmapboundary(fill_color='white')

    cs = m.contourf(x, y, air_cyc, 20)
    plt.title('Monthly mean SAT')
    plt.colorbar(orientation='horizontal', pad=0.03)

    plt.show()


def basemap5():

    fl = Dataset('air.sig995.1950.nc')
    air = fl.variables['air'][0, :, :]
    lat = fl.variables['lat'][:]
    lon = fl.variables['lon'][:]
    air_cyc, lon_cyc = addcyclic(air, lon)
    lon2, lat2 = np.meshgrid(lon_cyc, lat)

    m = Basemap(projection='robin', lon_0=180, resolution='c')

    x, y = m(lon2, lat2)

    m.drawcoastlines()
    m.drawparallels(np.arange(-80., 81., 20.))
    m.drawmeridians(np.arange(-180., 181., 20.))
    m.drawmapboundary(fill_color='white')
    cs = m.contourf(x, y, air_cyc, 20)
    plt.title('Monthly mean SAT');
    plt.colorbar(orientation='horizontal', pad=0.03)
    plt.show()


def basemap6():
    fl = Dataset('air.sig995.1950.nc')
    air = fl.variables['air'][0, :, :]
    lat = fl.variables['lat'][:]
    lon = fl.variables['lon'][:]
    air_cyc, lon_cyc = addcyclic(air, lon)
    lon2, lat2 = np.meshgrid(lon_cyc, lat)

    width = 28000000;
    lon_0 = 0;
    lat_0 = 40
    m = Basemap(width=width, height=width, projection='aeqd', lat_0=lat_0, lon_0=lon_0)
    x, y = m(lon2, lat2)
    m.drawcoastlines()
    m.drawparallels(np.arange(-80., 81., 20.))
    m.drawmeridians(np.arange(-180., 181., 20.))
    m.drawmapboundary(fill_color='white')
    cs = m.contourf(x, y, air_cyc, 20)
    plt.title('Monthly mean SAT')
    plt.colorbar(orientation='horizontal', pad=0.03)

    plt.show()


basemap5()

