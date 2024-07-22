import urllib.request
import base64
import json



def get_schedule(season: int, eventcode: str, username: str, password: str,team_num:str) -> dict:
<<<<<<< HEAD
    url = f"https://ftc-api.firstinspires.org/v2.0/{season}/schedule/{eventcode}?tournamentLevel=qual&teamNumber={team_num}&start=1&end=999"
    credentials = f"{username}:{password}"
    encoded_credentials = base64.b64encode(credentials.encode("utf-8")).decode("utf-8")
=======
    url = f'https://ftc-api.firstinspires.org/v2.0/{season}/schedule/{eventcode}?tournamentLevel=qual&teamNumber={team_num}&start=1&end=999'
    credentials = f'{username}:{password}'
    encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')
>>>>>>> d158eb7ec0519de229885686d10d8820cd23ed98

    # Create a request object
    request = urllib.request.Request(url)

    # Add the Authorization header to the request
<<<<<<< HEAD
    request.add_header("Authorization", f"Basic {encoded_credentials}")
=======
    request.add_header('Authorization', f'Basic {encoded_credentials}')
>>>>>>> d158eb7ec0519de229885686d10d8820cd23ed98

    # Send the request and get the response
    try:
        with urllib.request.urlopen(request) as response:
            response_body = response.read()
            # Decode and parse the JSON response
<<<<<<< HEAD
            return json.loads(response_body.decode("utf-8"))
    except urllib.error.HTTPError as e:
        print(f"HTTP error: {e.code} - {e.reason}")
    except urllib.error.URLError as e:
        print(f"URL error: {e.reason}")
=======
            return json.loads(response_body.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f'HTTP error: {e.code} - {e.reason}')
    except urllib.error.URLError as e:
        print(f'URL error: {e.reason}')
>>>>>>> d158eb7ec0519de229885686d10d8820cd23ed98
    return None

