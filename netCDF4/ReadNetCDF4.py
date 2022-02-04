# Based on source code & tutorial at:
# https://pyhogs.github.io/intro_netcdf4.html

import netCDF4 as nc4

f = nc4.Dataset('Arctic.nc', 'r')
print(f)
#temp_group = f.groups['Temp_data']

#print("JORz meta data for the dataset:")
#print(f)
#print("JORz data for the Temp_data group:")
#print(temp_group)
#print("JORz data for Temperature variable:")
#print(temp_group.variables['Temperature'])

# Query for a list of variables
#print(temp_group.variables.keys())

# Enquire about a specific variable, they are stored in a dictionary
#time_vble = temp_group.variables['Time']
#print(time_vble.ncattrs())
#print(time_vble.getncattr('units'))

# If many attributes, loop
#temp_vble = temp_group.variables['Temperature']
#for attr in temp_vble.ncattrs():
#    print(attr + ': ' + temp_vble.getncattr(attr))

#zlvls = temp_group.variables['Levels'][:]
#print(zlvls)