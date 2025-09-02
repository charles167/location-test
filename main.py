from folium import Map

# Get latitude and longitude values
latitude = 40.09
longitude = 3.47

antipode_latitude = latitude * -1

# Add 180 for negative longitudes.
# Subtract 180 for positive longitudes
if longitude <= 0:
    antipode_longitude = longitude + 180
else:
    antipode_longitude = longitude - 180

location = [antipode_latitude, antipode_longitude]

mymap = Map(location)
mymap.save("antipode.html")

print(antipode_latitude)
print(antipode_longitude)
print(mymap)
