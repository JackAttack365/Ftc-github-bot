# import requests

# # Define the endpoint URL
# url = "http://ftc-api.firstinspires.org/v2.0/2024/schedule/{eventCode}"

# # Your API key
# api_key = "0DA2B313-A2B2-4267-A3CC-E05D2DEC04F3"

# # Headers including the API key
# headers = {
#     "Authorization": f"Bearer {api_key}",
#     "Content-Type": "application/json"
# }

# # Make the request
# response = requests.get(url, headers=headers)

# # Check if the request was successful
# if response.status_code == 200:
#     # Parse the JSON response
#     data = response.json()
#     print(data)
# else:
#     print(f"Failed to retrieve data: {response.status_code}")

import requests

# Define the variables
season = "2024"
url = f"https://ftc-api.firstinspires.org/v2.0/{season}/events"

# Your API key
api_key = "0DA2B313-A2B2-4267-A3CC-E05D2DEC04F3"

# Headers including the API key
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "jason_files\\awards.json"
}

# Make the request
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    events = response.json()
    # Print out event codes
    for event in events:
        print(f"Event Name: {event['name']}, Event Key: {event['eventKey']}")
else:
    print(f"Failed to retrieve data: {response.status_code}")
