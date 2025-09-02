import folium

# Original location: Lagos, Nigeria
latitude = 6.5244
longitude = 3.3792

# Calculate antipode latitude (opposite side of Earth)
antipode_latitude = -latitude

# Calculate antipode longitude (180° away)
if longitude <= 0:
    antipode_longitude = longitude + 180
else:
    antipode_longitude = longitude - 180

# Antipode location
antipode_location = [antipode_latitude, antipode_longitude]
original_location = [latitude, longitude]

# Create map centered on Nigeria
mymap = folium.Map(location=original_location, zoom_start=3)

# Add marker for original location
folium.Marker(
    original_location,
    popup=f"Lagos, Nigeria: {latitude}, {longitude}",
    tooltip="Original Location",
    icon=folium.Icon(color="green")
).add_to(mymap)

# Add marker for antipode location
folium.Marker(
    antipode_location,
    popup=f"Antipode: {antipode_latitude}, {antipode_longitude}",
    tooltip="Antipode Location",
    icon=folium.Icon(color="red")
).add_to(mymap)

# Save map
mymap.save("antipode.html")

print("Original Location (Nigeria):", original_location)
print("Antipode Location:", antipode_location)
print("Map saved as antipode.html")
