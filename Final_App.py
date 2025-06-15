import api_key
import googlemaps

# Initialize Google Maps client
gmaps = googlemaps.Client(key=api_key.YOUR_API_KEY)

# Geocode a human-readable location to coordinates
def geocode_location(location_name):
    geocode_result = gmaps.geocode(location_name)
    return geocode_result[0]['geometry']['location']

# Find nearby restaurants around given coordinates
def find_nearby_restaurants(location, radius=1000):
    # You could add more parameters like 'keyword' or 'rank_by' to filter results
    # For example, use 'rank_by="distance"' to get the closest restaurants
    result = gmaps.places_nearby(location=location, radius=radius, type='restaurant')
    return result.get('results', [])

# Main program
def main():
    location_input = input("Enter a location (e.g. Nanyang Polytechnic): ")
    origin_location = geocode_location(location_input)

    print(f"\nCoordinates: {origin_location}")

    nearby_restaurants = find_nearby_restaurants(origin_location)

    if not nearby_restaurants:
        print("No nearby restaurants found.")
        return

    print("\nNearby Restaurants:")
    for restaurant in nearby_restaurants:
        # Vicinity refers to the address of the location. For example: NYP's address is 180 Ang Mo Kio Avenue 8, Singapore.
        print(f"- {restaurant['name']} ({restaurant['vicinity']})")
        
        # Calculate distance using your format
        mode = "driving"
        distance_result = gmaps.distance_matrix(
            origins=[origin_location],
            destinations=[restaurant.get("vicinity")],
            mode=mode
        )

        distance_info = distance_result['rows'][0]['elements'][0]
        print(f"  Distance: {distance_info.get('distance', {}).get('text', 'N/A')}")
        print(f"  Duration: {distance_info.get('duration', {}).get('text', 'N/A')}\n")

main()