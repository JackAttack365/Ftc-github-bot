import json

def find_matches(team_number):
    # Load JSON data from the file
    with open("test.json", "r") as file:
        schedule = json.load(file)

    # Find matches for the specified team number
    matches = []
    for match in schedule["schedule"]:
        # Find the station of the specified team
        team_info = next((team for team in match["teams"] if team["teamNumber"] == team_number), None)
        if team_info:
            station = team_info["station"]
            # Determine the corresponding partner station
            if station == "Red1":
                partner_station = "Red2"
            elif station == "Red2":
                partner_station = "Red1"
            elif station == "Blue1":
                partner_station = "Blue2"
            elif station == "Blue2":
                partner_station = "Blue1"
            else:
                partner_station = None
            
            # Get partner team(s) at the matching partner station
            partner_teams = [
                f"{team["teamName"]} (Team #{team["teamNumber"]})"
                for team in match["teams"] if team["station"] == partner_station
            ]
            matches.append({
                "description": match["description"],
                "partners": partner_teams
            })

    # Create a string to hold the match information
    match_results = []
    for match in matches:
        match_results.append(f"Match Description: {match["description"]}")
        match_results.append(f"Partner Team: {", ".join(match["partners"])}\n")

    return "\n".join(match_results)

# Example usage:
# print(find_matches(22064))  # Replace 22064 with the actual team number you"re interested in
