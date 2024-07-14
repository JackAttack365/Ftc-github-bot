import gspread
from oauth2client.service_account import ServiceAccountCredentials

def add_row_to_sheet(sheet_url, string_to_add):
    # Define the scope
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    
    # Add your credentials here
    creds = ServiceAccountCredentials.from_json_keyfile_name("noble-sum-428623-d2-7bee39b502f8.json", scope)
    client = gspread.authorize(creds)
    
    # Open the Google Sheet
    sheet = client.open_by_url(sheet_url).sheet1
    
    # Find the next empty row
    next_row = len(sheet.get_all_values()) + 1
    
    # Add the string to the next row
    sheet.update_cell(next_row, 1, string_to_add)

# Example usage
sheet_url = 'https://docs.google.com/spreadsheets/d/1Ad4Dnh2_DoW7ypHcuKGsgvaa-FaGoGE4o0AVUv-otl4/edit?gid=0'
string_to_add = 'Your string here'
add_row_to_sheet(sheet_url, string_to_add)
