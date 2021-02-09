# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 22:19:20 2021

@author: garla
"""

from __future__ import print_function
import pickle
import pandas as pd
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import random as r

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1AvJ4GP7O0Qw6q5WvzWsKxI0CztH8KAtEpF0iKk0WF3k'
SAMPLE_RANGE_NAME = 'Form Responses!B:M'

def GetSurvey():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,range = SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])
    headers = values.pop(0)
    df = pd.DataFrame(values)
    df.columns = headers
    
    return df

# surveyresults = GetSurvey()


# headers = surveyresults.columns.tolist()
# target = headers[r.randint(4,len(headers)-1)]
# possibleoptions = surveyresults[target].unique()
# targetindex = r.randint(0,len(surveyresults)-1)
# targetplayer = surveyresults.loc[targetindex,'First Name']
# correct = surveyresults.loc[targetindex,target]

# if len(possibleoptions) == 2:
#     ABCD = ['A','B']
#     location = ABCD.pop(r.randint(0,len(ABCD)-1))
#     answer = {location : correct}
#     options = {}
#     options[location] = correct
#     while len(options) < 2:
#         toadd = possibleoptions[r.randint(0,len(possibleoptions)-1)]
#         while toadd in options.values():
#             toadd = possibleoptions[r.randint(0,len(possibleoptions)-1)]
#         location1 = ABCD.pop(r.randint(0,len(ABCD)-1))
#         options[location1] = toadd

# elif len(possibleoptions) == 3:
#     ABCD = ['A','B','C']
#     location = ABCD.pop(r.randint(0,len(ABCD)-1))
#     answer = {location : correct}
#     options = {}
#     options[location] = correct
#     while len(options) < 3:
#         toadd = possibleoptions[r.randint(0,len(possibleoptions)-1)]
#         while toadd in options.values():
#             toadd = possibleoptions[r.randint(0,len(possibleoptions)-1)]
#         location1 = ABCD.pop(r.randint(0,len(ABCD)-1))
#         options[location1] = toadd
        
# elif len(possibleoptions) >= 4:
#     ABCD = ['A','B','C','D']
#     location = ABCD.pop(r.randint(0,len(ABCD)-1))
#     answer = {location : correct}
#     options = {}
#     options[location] = answer
#     while len(options) < 4:
#         toadd = possibleoptions[r.randint(0,len(possibleoptions)-1)]
#         while toadd in options.values():
#             toadd = possibleoptions[r.randint(0,len(possibleoptions)-1)]
#         location1 = ABCD.pop(r.randint(0,len(ABCD)-1))
#         options[location1] = toadd

# else:
#     options = 'n/a'
#     answer = 'n/a'

# question = surveyresults.iloc[:,r.randint(4,5)]
# print(question)
# target = question[1]
# print(target)