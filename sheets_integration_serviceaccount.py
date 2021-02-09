# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 22:19:20 2021

@author: garla
"""

from __future__ import print_function
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
import gspread

# If modifying these scopes, delete the file token.pickle.
SCOPES = ["https://spreadsheets.google.com/feeds"]

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1AvJ4GP7O0Qw6q5WvzWsKxI0CztH8KAtEpF0iKk0WF3k'
SHEET = 'Form Responses'

def GetSurvey():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = ServiceAccountCredentials.from_json_keyfile_name("/home/hiitmeup/mysite/hiit-me-up-1612476279506-977bd3b5efc1.json", SCOPES)
    connection = gspread.authorize(creds)

    sht1 = connection.open_by_key(SAMPLE_SPREADSHEET_ID)

    worksheet = sht1.worksheet(SHEET)
    list_of_lists = worksheet.get_all_values()
    headers = list_of_lists.pop(0)

    df = pd.DataFrame(list_of_lists)
    df.columns = headers

    dff = pd.DataFrame(df.iloc[:,0:len(headers)-1])

    return dff
