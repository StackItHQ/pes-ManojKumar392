import os
import gspread
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# Path to OAuth credentials and token
creds_path = os.path.join(os.path.dirname(__file__), 'credentials/oauth.json')
token_path = os.path.join(os.path.dirname(__file__), 'credentials/token.json')

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None

# Check if the token already exists
if os.path.exists(token_path):
    creds = Credentials.from_authorized_user_file(token_path, SCOPES)

# If there are no valid credentials, go through OAuth flow
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(creds_path, SCOPES)
        creds = flow.run_local_server(port=0)

    # Save the credentials for the next run
    with open(token_path, 'w') as token_file:
        token_file.write(creds.to_json())

# Authorize gspread with the credentials
client = gspread.authorize(creds)

# Open Google Sheet by name
sheet = client.open("https://docs.google.com/spreadsheets/d/1URQ872xsAaT0xUVk7ePK5YxNtYYHiZSZbX5rAMCB-Ag/edit?usp=sharing").sheet1

# Example: Get all records
data = sheet.get_all_records()
print(data)
