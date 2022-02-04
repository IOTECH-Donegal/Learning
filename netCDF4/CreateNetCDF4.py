# Based on source code & tutorial at:
# https://pyhogs.github.io/intro_netcdf4.html

import numpy as np
import netCDF4 as nc4
from datetime import datetime

# Create some dummy data as numpy arrays, start, finish, step
lon = np.arange(45, 101, 2)
lat = np.arange(-30, 25, 2.5)
z = np.arange(0, 200, 10)
x = np.random.randint(10, 25, size=(len(lon), len(lat), len(z)))
noise = np.random.rand(len(lon), len(lat), len(z))
temp_data = x+noise

# Create a dataset and open to write, f is the root group, but has no variables
f = nc4.Dataset('Arctic.nc', 'w', format='NETCDF4')
temp_group = f.createGroup('Temp_data')

# Create dimensions
temp_group.createDimension('lon', len(lon))
temp_group.createDimension('lat', len(lat))
temp_group.createDimension('z', len(z))
temp_group.createDimension('time', None)

# Preallocate variables for data storage, name, datatype and shape
longitude = temp_group.createVariable('Longitude', 'f4', 'lon')
latitude = temp_group.createVariable('Latitude', 'f4', 'lat')
levels = temp_group.createVariable('Levels', 'i4', 'z')
temp = temp_group.createVariable('Temperature', 'f4', ('time', 'lon', 'lat', 'z'), zlib=True)
time = temp_group.createVariable('Time', 'i4', 'time')

#print(f)
#print(f.groups['Temp_data'])
#print(temp_group.variables.keys())
#print(temp_group.dimensions.keys())

# Pass data into the variables created previously
longitude[:] = lon
latitude[:] = lat
levels[:] = z
temp[0, :, :, :] = temp_data

# Get time in days since Jan 01,01
today = datetime.today()
time_num = today.toordinal()
time[0] = time_num

# Add global attributes
f.description = "Example dataset containing one group"
f.history = "Created " + today.strftime("%d/%m/%y")

# Add local attributes to variable instances
longitude.units = 'degrees west'
latitude.units = 'degrees north'
time.units = 'days since Jan 01, 0001'
temp.units = 'Kelvin'
levels.units = 'meters'
temp.warning = 'This data is not real!'

# Close the dataset
f.close()





