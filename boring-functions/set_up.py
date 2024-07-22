import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
def set_up(server_name):
# Define the scope
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

    # Path to your service account key file
    creds = ServiceAccountCredentials.from_json_keyfile_name("jason_files\GoogleSheets.json", scope)

    # Authorize the client
    client = gspread.authorize(creds)

    #the sheets names
    spreed_sheet_parts_name = f"{server_name}'s requested parts"
    spreed_sheet_timeline_name = f"{server_name}'s time line"

    # Create a new spreadsheet
    spreadsheet_parts = client.create(f"{spreed_sheet_parts_name}")
    spreadsheet_timeline = client.create(f"{spreed_sheet_parts_name}")

    # Share the spreadsheet with anyone who has the link
    spreadsheet_parts.share(None, perm_type="anyone", role="reader")
    spreadsheet_timeline.share(None, perm_type="anyone", role="reader")

    # Get the spreadsheet URL
    spreadsheet_parts_url = spreadsheet_parts.url
    spreadsheet_timeline_url = spreadsheet_timeline.url

    # Print the spreadsheet URL
    # print("The spreadsheet is available at:", spreadsheet_parts_url)
    # print("The spreadsheet is available at:", spreadsheet_timeline_url)

    #creates the folder for the teams
    PATH = f"team_files\\{server_name}"

    if not os.path.exists(PATH):
        os.makedirs(PATH)

    with open(f"team_files\\{server_name}\\{server_name}google_seets.txt", "w") as file:
        file.write(f"{spreadsheet_parts_url}\n{spreadsheet_timeline_url}")

    # Open the new spreadsheet by title
    sheet = client.open("New Spreadsheet").sheet1

    # Add data to the first row and column
    sheet.update_cell(1, 1, "Hello, World!")