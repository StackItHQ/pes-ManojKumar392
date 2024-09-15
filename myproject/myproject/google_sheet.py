import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Setup Google Sheets API
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("../myapp/credentials/credentials.json", scope)
client = gspread.authorize(creds)

# Open a Google Sheet by its URL or name
sheet = client.open("superjoin").sheet1

# Get all records
data = sheet.get_all_records()
for row in data:
    print(row)

# # Update a cell
# sheet.update_cell(2, 1, "Updated Value")
