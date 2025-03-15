import json

def remove_id_only(json_file):
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Filter out features with only '@id' in properties
    filtered_features = [
        feature for feature in data["features"]
        if len(feature["properties"]) > 1  # Keeps only features with more than one property
    ]

    # Update the GeoJSON data
    data["features"] = filtered_features

    # Save the cleaned GeoJSON file
    with open("filtered_file.geojson", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Filtered GeoJSON saved as 'filtered_file.geojson' with {len(filtered_features)} features.")

def remove_features_by_keyword(geojson_file, keyword, output_file):
    """
    Removes features from a GeoJSON file if any property contains the given keyword.

    :param geojson_file: Path to the input GeoJSON file.
    :param keyword: The keyword to check in properties.
    :param output_file: Path to save the filtered GeoJSON.
    """
    # Load GeoJSON file
    with open(geojson_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Filter features: Keep only those that do NOT contain the keyword
    filtered_features = [
        feature for feature in data.get("features", [])
        if not any(keyword in str(value) for value in feature.get("properties", {}).values())
    ]

    # Update the GeoJSON data
    data["features"] = filtered_features

    # Save the cleaned GeoJSON file
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Filtered GeoJSON saved as '{output_file}' with {len(filtered_features)} features.")

def get_features_with_single_property(geojson_file):
    """
    Returns features from a GeoJSON file that contain only one property.

    :param geojson_file: Path to the input GeoJSON file.
    :return: List of features that have only one property.
    """
    # Load GeoJSON file
    with open(geojson_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Filter features: Keep only those with exactly one property
    single_property_features = [
        feature for feature in data.get("features", [])
        if len(feature.get("properties", {})) == 3
    ]

    return single_property_features

import json
from collections import defaultdict

def merge_features_with_same_coordinates(geojson_file, output_file):
    """
    Merges features in a GeoJSON file that have the same coordinates by combining their properties.
    
    :param geojson_file: Path to the input GeoJSON file.
    :param output_file: Path to save the merged GeoJSON file.
    """
    # Load GeoJSON file
    with open(geojson_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Create a dictionary to store features by their coordinates
    coordinates_map = defaultdict(list)

    # Iterate through features and group them by their coordinates
    for feature in data.get("features", []):
        coordinates = tuple(feature["geometry"]["coordinates"])
        coordinates_map[coordinates].append(feature)

    # Merge features with the same coordinates by combining their properties
    merged_features = []
    for coords, features in coordinates_map.items():
        # Start with the first feature
        merged_feature = features[0].copy()

        # Merge properties for features with the same coordinates
        merged_properties = {}
        for feature in features:
            merged_properties.update(feature["properties"])

        # Assign the merged properties to the feature
        merged_feature["properties"] = merged_properties

        # Append the merged feature to the list
        merged_features.append(merged_feature)

    # Update the GeoJSON data with the merged features
    data["features"] = merged_features

    # Save the merged GeoJSON file
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Merged GeoJSON saved as '{output_file}' with {len(merged_features)} features.")


def main():
    remove_id_only('export-4.geojson')
    remove_features_by_keyword('filtered_file.geojson', 'guidepost', 'filtered_file2.geojson')
    merge_features_with_same_coordinates('filtered_file2.geojson', 'filtered_file3.geojson')
    
    
    
if __name__ == '__main__':
    main()