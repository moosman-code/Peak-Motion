import json

# File paths
txt_file_path = "cleaned_plants.txt"  # Change this to your actual file path
json_file_path = "plantnet300K_species_id_2_name.json"  # Change this to your actual file path
output_matches_path = "matching_species.txt"

# Load species list from the .txt file
with open(txt_file_path, "r", encoding="utf-8") as file:
    txt_species = {line.strip() for line in file if line.strip()}

# Load species list from the JSON file
with open(json_file_path, "r", encoding="utf-8") as file:
    plantnet_species = set(json.load(file).values())

# Find matching species
matches = sorted(txt_species.intersection(plantnet_species))

# Save the matches to a new file
with open(output_matches_path, "w", encoding="utf-8") as file:
    file.write("\n".join(matches))

print(f"Found {len(matches)} matching species. Saved to {output_matches_path}.")
