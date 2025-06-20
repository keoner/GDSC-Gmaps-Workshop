import api_key
import googlemaps

# Initialize Google Maps client
gmaps = googlemaps.Client(key=api_key.YOUR_API_KEY)

address = "1600 Pennsylvania Ave NW, Washington, DC 20500"

# Geocode the address (human-readable location to coordinates)
geocode_result = gmaps.geocode(address)

# Output the result
print("Geocoding Result:")
if geocode_result:
    for result in geocode_result:
        print(f"Formatted Address: {result['formatted_address']}")
        print(f"Latitude: {result['geometry']['location']['lat']}")
        print(f"Longitude: {result['geometry']['location']['lng']}")
        print("-" * 40)