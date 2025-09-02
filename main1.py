import folium

# Get latitude and longitude values
latitude = 40.09
longitude = 3.47

antipode_latitude = -latitude

# Add 180 for negative longitudes.
# Subtract 180 for positive longitudes
if longitude <= 0:
    antipode_longitude = longitude + 180
else:
    antipode_longitude = longitude - 180

# Antipode location
location = [antipode_latitude, antipode_longitude]

# Create map centered at antipode
mymap = folium.Map(location=location, zoom_start=3)

# Add a marker
folium.Marker(
    location,
    popup=f"Antipode: {antipode_latitude}, {antipode_longitude}",
    tooltip="Antipode Location"
).add_to(mymap)

# Save map
mymap.save("antipode.html")

print("Antipode Latitude:", antipode_latitude)
print("Antipode Longitude:", antipode_longitude)
print("Map saved as antipode.html")
