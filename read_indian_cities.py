import json

# Open and read the JSON file
with open("../indian_cities.json", "r", encoding="utf-8") as f:
    indian_cities = json.load(f)

# Now you can access the dictionary
print(indian_cities["Kerala"])  # Example: prints the list of cities in Kerala
