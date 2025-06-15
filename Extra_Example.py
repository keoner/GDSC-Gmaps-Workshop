import googlemaps

# Initialize Google Maps client
gmaps = googlemaps.Client(key='YOUR_API_KEY')

address = (38.8976763, -77.0365298)

# Geocode the address
geocode_result = gmaps.reverse_geocode(address)

# Output the result
print("Geocoding Result:")
if geocode_result:
    place_id = geocode_result[0]['place_id']
    place_details = (gmaps.place(place_id=str(geocode_result[0]['place_id'])))
    print(place_details['result']['name'])
    print(f"Formatted Address: {geocode_result[0]['formatted_address']}")
    print(f"Place_ID: {place_id}")