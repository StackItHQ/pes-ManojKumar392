from django.http import HttpResponse
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def google_sheets_example(request):
    # Setup Google Sheets API
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("sheets/credentials/credentials.json", scope)
    client = gspread.authorize(creds)

    # Open a Google Sheet by its URL or name
    sheet = client.open("superjoin").sheet1

    # Get data
    data = sheet.get_all_records()

    # Return a response
    return HttpResponse(f"Data from the sheet: {data}")
