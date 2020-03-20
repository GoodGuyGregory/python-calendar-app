# Allows for builing elements from google auth
from apiclient.discovery import build
# Flows are used to set up Oauthcredentials to the application
from google_auth_oauthlib.flow import InstalledAppFlow

#  Saves Python Objects: in this case it will store our credentials

import pickle

# Permissions to take from the user
#  Found Here: https://developers.google.com/calendar/auth
SCOPE = ['https://www.googleapis.com/auth/calendar']

# Create the Flow for Authentication:
flow = InstalledAppFlow.from_client_secrets_file(
    "client_secret.json", scopes=SCOPE)

credentials = flow.run_console()

# 4/xwHXGn8KomnppAscbzts9PWNlRCe
# AUWnEh-_kRqVQfAJ5vtTWVPYVSc

# Store the Credentials Created
pickle.dump(credentials, open("token.pkl", "wb"))

credentials = pickle.load(open("token.pkl", "rb"))
service = build("calendar", "v3", credentials=credentials)

#  Get All Calendars:
result = service.calendarList().list().execute()

# Returns the First Calendar Items
result['items'][0]

# Get all Events Listed
calendar_id = result['items'][0]['id']

result = service.events().list(calendarId=calendar_id,
                               timeZone="America/Kentucky").execute()
