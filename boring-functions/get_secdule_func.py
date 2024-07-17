import urllib.request
import base64
import json



def get_schedule(season: int, eventcode: str, username: str, password: str,team_num:str) -> dict:
    url = f'https://ftc-api.firstinspires.org/v2.0/{season}/schedule/{eventcode}?tournamentLevel=qual&teamNumber={team_num}&start=1&end=999'
    credentials = f'{username}:{password}'
    encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

    # Create a request object
    request = urllib.request.Request(url)

    # Add the Authorization header to the request
    request.add_header('Authorization', f'Basic {encoded_credentials}')

    # Send the request and get the response
    try:
        with urllib.request.urlopen(request) as response:
            response_body = response.read()
            # Decode and parse the JSON response
            return json.loads(response_body.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f'HTTP error: {e.code} - {e.reason}')
    except urllib.error.URLError as e:
        print(f'URL error: {e.reason}')
    return None

