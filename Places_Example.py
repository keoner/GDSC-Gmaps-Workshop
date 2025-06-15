import googlemaps

# Initialize Google Maps client
gmaps = googlemaps.Client(key='YOUR_API_KEY')

location = (43.0617713, 141.3544507)  # Sapporo, Japan (latitude, longitude)
radius = 1000  # Search within a 1000-meter radius
place_type = 'restaurant'  # Searching for restaurants

# Fetch the nearby places
places_result = gmaps.places_nearby(location=location, radius=radius, type=place_type)

# Display the results
print("Nearby Restaurants:")
for place in places_result['results']:
    print(f"Name: {place['name']}")
    print(f"Address: {place['vicinity']}")
    print("-" * 40)