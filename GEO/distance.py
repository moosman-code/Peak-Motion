import json
import math
import heapq  # Min-heap for efficient closest selection

def haversine(lat1, lon1, lat2, lon2):
    """Calculate the great-circle distance between two coordinates in meters."""
    R = 6371000  # Earth radius in meters
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

    print(R * c)
    return R * c  # Distance in meters

def haversine(lat1, lon1, lat2, lon2):
    """Calculate the great-circle distance between two coordinates in meters."""
    R = 6371000  # Earth radius in meters
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

    return R * c  # Distance in meters

def find_nearest_within_distance(json_file, lon, lat, max_distance_m, n=5):
    """Find up to n closest objects within a max distance (in meters), excluding the same coordinates."""
    with open(json_file, 'r') as f:
        data = json.load(f)

    objects = data['features']
    
    # Compute distances, filter out exact coordinate matches
    valid_objects = [
        (haversine(lat, lon, obj['geometry']['coordinates'][1], obj['geometry']['coordinates'][0]), obj)
        for obj in objects
        if (obj['geometry']['coordinates'][0], obj['geometry']['coordinates'][1]) != (lon, lat)  # Exclude exact matches
    ]

    valid_objects = [entry for entry in valid_objects if entry[0] <= max_distance_m]

    # Get up to 'n' closest nodes
    closest_objects = heapq.nsmallest(n, valid_objects, key=lambda x: x[0])

    return closest_objects 


def get_n_neighbors(longitude, latitude, max_distance, n):
    json_file = 'filtered_file3.geojson'
    closest = find_nearest_within_distance(json_file, longitude, latitude, max_distance, n)

    return closest
            
if __name__ == '__main__':
    # Example usage
    
    longitude, latitude = 23.2515266, 42.6261266 # Example coordinates
    max_distance = 300  
    
    print(get_n_neighbors(longitude, latitude, max_distance, n = 5))

    # Print results
    
