import json

def find_matches(team_number):
    # Load JSON data from the file
    with open("test.json", "r") as file:
        schedule = json.load(file)

    # Find matches for the specified team number
    matches = []
    for match in schedule["schedule"]:
        if any(team['teamNumber'] == team_number for team in match['teams']):
            partner_teams = [team['teamName'] for team in match['teams'] if team['teamNumber'] != team_number]
            matches.append({
                "description": match["description"],
                "partners": partner_teams
            })

    # Create a string to hold the match information
    match_results = []
    for match in matches:
        match_results.append(f"Match Description: {match['description']}")
        match_results.append(f"Partner Teams: {', '.join(match['partners'])}\n")

    return "\n".join(match_results)

# Example usage
