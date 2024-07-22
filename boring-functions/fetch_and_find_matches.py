import urllib.request
import base64
import json
import os


def get_events_into_json(season: int,username: str,password: str,team_num:str) -> dict:
    url = f"https://ftc-api.firstinspires.org/v2.0/{season}/events?teamNumber={team_num}"
    credentials = f"{username}:{password}"
    encoded_credentials = base64.b64encode(credentials.encode("utf-8")).decode("utf-8")
    
    # Create a request object
    request = urllib.request.Request(url)

    # Add the Authorization header to the request
    request.add_header("Authorization", f"Basic {encoded_credentials}")

    #creates the folder for the teams
    PATH = f"team_files\\{team_num}"

    if not os.path.exists(PATH):
        os.makedirs(PATH)
    # Send the request and get the response
    try:
        with urllib.request.urlopen(request) as response:
            response_body = response.read()
            # Decode and parse the JSON response
            schedule = json.loads(response_body.decode("utf-8"))
            pretty_schedule = json.dumps(schedule, indent=4)
            with open(f"team_files\\{team_num}\\{team_num}_events.json", "w") as f:
                f.write(f"{pretty_schedule}")
    except urllib.error.HTTPError as e:
        print(f"HTTP error: {e.code} - {e.reason}")
    except urllib.error.URLError as e:
        print(f"URL error: {e.reason}")
    return None

def contains_string(data, search_str):
    if isinstance(data, dict):
        for key, value in data.items():
            if search_str in str(key) or contains_string(value, search_str):
                return True
    elif isinstance(data, list):
        for item in data:
            if contains_string(item, search_str):
                return True
    elif isinstance(data, str):
        if search_str in data:
            return True
    return False

def get_current_event(season: int, username: str, password: str,team_num:str) -> dict:
    #gets the event code
    with open(f"team_files\\{team_num}\\{team_num}_events.json", "r") as f:
            data = json.load(f)
            # Access the "events" list and get the "code" of the first event
            if "events" in data and len(data["events"]) > 0 and contains_string(data, "Championship"):
                event_code = data["events"][1].get("code")
                print("used code 1")
            else:
                event_code = data["events"][0].get("code")
                print("used code 0")
    


    url = f"https://ftc-api.firstinspires.org/v2.0/{season}/schedule/{event_code}?tournamentLevel=qual&teamNumber={team_num}&start=1&end=999"
    credentials = f"{username}:{password}"
    encoded_credentials = base64.b64encode(credentials.encode("utf-8")).decode("utf-8")

    # Create a request object
    request = urllib.request.Request(url)

    # Add the Authorization header to the request
    request.add_header("Authorization", f"Basic {encoded_credentials}")

    # Send the request and get the response
    try:
        with urllib.request.urlopen(request) as response:
            response_body = response.read()
            schedule = json.loads(response_body.decode("utf-8"))
            pretty_schedule = json.dumps(schedule, indent=4)
            with open(f"team_files\\{team_num}\\{team_num}_current_event.json", "w") as f:
                f.write(f"{pretty_schedule}")
    except urllib.error.HTTPError as e:
        print(f"HTTP error: {e.code} - {e.reason}")
    except urllib.error.URLError as e:
        print(f"URL error: {e.reason}")
    return None

#this function reads a json file and returns a nicer to read list
def find_matches(team_number):
    # Load JSON data from the file
    with open(f"team_files\\{team_number}\\{team_number}_current_event.json", "r") as file:
        schedule = json.load(file)

    # Find matches for the specified team number
    matches = []
    for match in schedule["schedule"]:
        # Find the station of the specified team
        team_info = next((team for team in match["teams"] if team["displayTeamNumber"] == team_number), None)
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

def find_match_nums(team_number):
    # Load JSON data from the file
    with open(f"team_files\\{team_number}\\{team_number}_current_event.json", "r") as file:
        data = json.load(file)
    
    # Extract match numbers from the schedule
    match_numbers = [match["matchNumber"] for match in data["schedule"]]
    
    return match_numbers