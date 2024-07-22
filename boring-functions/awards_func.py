import json

def print_award_info(file_path, award_id):
    # Read the JSON file
    with open(file_path, "r") as file:
        awards_data = json.load(file)

    # Find the award with the specified ID
    award = next((award for award in awards_data["awards"] if award["awardId"] == award_id), None)
    
    if award:
        # Print the award details in a readable way
        print(f"Award ID: {award["awardId"]}")
        print(f"Name: {award["name"]}")
        print(f"Description: {award["description"] if award["description"] else "No description available."}")
        print(f"For Person: {"Yes" if award["forPerson"] else "No"}")
    else:
        print("Award not found.")

# Example usage
file_path = "awards.json"
print_award_info(file_path, 108)
