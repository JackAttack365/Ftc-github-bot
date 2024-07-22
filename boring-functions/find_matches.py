import json

def find_matches():
    # Load JSON data from the file
    with open("test.json", "r") as file:
        schedule = json.load(file)

    # Extract all parts of the JSON file with matchNumber
    matches_with_number = [match for match in schedule["schedule"] if "matchNumber" in match]

    return matches_with_number

