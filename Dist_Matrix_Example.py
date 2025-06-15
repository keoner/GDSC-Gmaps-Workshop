import api_key
import googlemaps

# Initialize Google Maps client
gmaps = googlemaps.Client(key=api_key.YOUR_API_KEY)

origin = "1600 Pennsylvania Ave NW, Washington, DC 20500"  # Example origin address
destination = "The White House, Washington, DC"  # Example destination address
# Origin & destination can be either latitude and longitude coordinates or a human-readable address.

distance_result = gmaps.distance_matrix(origins=origin, destinations=destination, mode="driving")
# Mode can be set to walking, bicycling, transit or driving
distance_info = distance_result['rows'][0]['elements'][0]
print(f"Distance: {distance_info.get('distance', {}).get('text', 'N/A')}")
print(f"Duration: {distance_info.get('duration', {}).get('text', 'N/A')}")