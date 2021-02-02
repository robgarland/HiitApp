# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 14:48:37 2021

@author: garla
"""
import pandas as pd 
import dash
import random as r
import string
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input

"""
Data Structure Components
"""
"""
Session Info ideal layout
session info = {'CODE':{'Instructor':'Name',
                        'Workout Type':'Type',
                        'Participants':[{'Name':'Name',
                                         'Team':'Team',
                                         'Scores':[{'Index':'Number',
                                                    'Entry':'Entry',
                                                    'Score':'Score'
                                                    }]
                                         }],
                        Teamscores:{'A': 'Score', 
                                    'B':'Score',C...
                                    }
                        }
    }
"""
sessioninfo = {}

participants = [
    'Rob',
    'Jordi',
    'Sana'
    ]

workouttypes = [
    'Impostor'
    ]

def generate_code(size=4, chars = string.ascii_uppercase):
    return ''.join(r.choice(chars) for _ in range(size))
    
code = 'DFAS'

# List of exercises avaliable

exercise = ['Jumping Jacks',
            'Arm Circles',
            'Lunges',
            'Shoulder Taps', 
            'Pulsing Squats',
            'Leg Raises',
            'Plank',
            'Sit Ups',
            'Half Burpees',
            'Mountain Climbers',
            'Squats',
            'Bicycle Crunches',
            'Push Ups',
            'Side Plank'
            ]

# Structure of Impostor Workout on Participant side (screen type is the main key, followed by the indexes at which the screen shows and the exercise)

regular_structure = {
    'inputs' : {'index' : {0 : 'Inputs'
                                            }
                                 },
    'warmup' : {'index' : {1 : 'Warmup', 
                           33 : 'Cooldown'
                                 }
                      },
    'leaderboard' : {'index' : {17 : 'Current Standings', 
                                34 : 'Final Standings'
                                }
                     },
    'numinput' : {'index' : {4 : exercise[2], 
                             5 : exercise[3], 
                             8 : exercise[6], 
                             9 : exercise[7], 
                             14 : exercise[12], 
                             15 : exercise[13], 
                             18 : exercise[13], 
                             19 : exercise[12], 
                             24 : exercise[7], 
                             25 : exercise[6], 
                             28 : exercise[3], 
                             29 : exercise[2]
                             }
                  },
    'abinput' : {'index' : {2 : exercise[0], 
                            3 : exercise[1], 
                            12 : exercise[10], 
                            13 : exercise[11],
                            20 : exercise[11],
                            21 : exercise[10],
                            30 : exercise[1],
                            31 : exercise[0]
                            }
                 },
    'abcdinput' : {'index' :{6 : exercise[4], 
                             7 : exercise[5], 
                             10 : exercise[8], 
                             11 : exercise[9], 
                             22 : exercise[9], 
                             23 : exercise[8], 
                             26 : exercise[5], 
                             27 : exercise[4]
                             }
                   },
    'impostorinput' : {'index' : {16 : 'Middle Guess', 32 : 'Final Guess'}}
          }

"""
All Elements/Creation of Elements Below
"""


def Navbar():
     navbar = dbc.NavbarSimple(
           children=[
              dbc.NavItem(dbc.NavLink("Quit", href="/")),
                    ],
          brand="Hiit Me Up Workout",
          sticky="top",
        )
     return navbar

"""
Input Screen Components
"""


header1 = html.H4(children = ['Enter Code:'], style = {'textAlign' : "center",'margin-top':'30px'})

header2 = html.H4(children = ['Enter Name:'], style = {'textAlign' : "center",'margin-top':'30px'})

cemsg = html.H6(children = ['Code not recognised, please enter a valid workout code'], style = {'textAlign' : 'center','margin-top':'30px','color':'red'})

codeinput = dcc.Input(id = 'code-input', type = 'text', placeholder = "4-Digit Code", maxLength = '4', style = {'textAlign' : "center", 'display':'block','margin-left':'auto','margin-right':'auto', 'margin-top':'15px'})

nameinput = dcc.Dropdown(id = 'name-dropdown', options = [{'label': participants[i], 'value' : participants[i]} for i in range(len(participants))], style = {'textAlign' : "center", 'display':'block','margin-left':'auto','margin-right':'auto', 'margin-top':'15px'})

enterbutton = dbc.Button('Enter', id = 'enter', href = "/workout", style = {'textAlign' : "center", 'display':'block','margin-left':'auto','margin-right':'auto','margin-top':'20px'})

"""
Workout Screen Components
"""
def Warmcool(index):
    warmcool = html.H4(children = [regular_structure['warmup']['index'][index]], style = {'textAlign' : "center",'margin-top':'50px'})
    return warmcool

participanttable = html.Table( children = [
    html.Thead(
        html.Tr(
            html.Th('Current Participants')
            )
        ),
    html.Tbody(
        [html.Tr([
            html.Td(participants[i])
            ]) for i in range(len(participants))]
        )
    ], style = {'textAlign' : "center"})

nextbutton = dbc.Button('Next',id = 'next-button', style = {'textAlign' : "center", 'display':'block','margin-left':'auto','margin-right':'auto','margin-top':'20px'})

abutton = dbc.Button('A',id = 'a-button',n_clicks=0, style = {'textAlign' : "center", 'display':'block','margin-left':'auto','margin-right':'auto','margin-top':'20px'})

bbutton = dbc.Button('B',id = 'b-button',n_clicks=0, style = {'textAlign' : "center", 'display':'block','margin-left':'auto','margin-right':'auto','margin-top':'20px'})

cbutton = dbc.Button('C',id = 'c-button',n_clicks=0, style = {'textAlign' : "center", 'display':'block','margin-left':'auto','margin-right':'auto','margin-top':'20px'})

dbutton = dbc.Button('D',id = 'd-button',n_clicks=0, style = {'textAlign' : "center", 'display':'block','margin-left':'auto','margin-right':'auto','margin-top':'20px'})

numberinput = dcc.Input(id = 'number-input', type = 'number', placeholder = "X", max = '100', style = {'textAlign' : "center", 'display':'block','margin-left':'auto','margin-right':'auto', 'margin-top':'15px'})
                   
impostorguess = dcc.Dropdown(id = 'impostor-dropdown', options = [{'label': participants[i], 'value' : participants[i]} for i in range(len(participants))], style = {'textAlign' : "center", 'display':'block','margin-left':'auto','margin-right':'auto', 'margin-top':'15px'})

quitbutton = dbc.Button('Quit',id = 'quit-button', href = "/", style = {'textAlign' : "center", 'display':'block','margin-left':'auto','margin-right':'auto','margin-top':'20px'})

"""
Main body layout Components
"""

navbar = Navbar()
                   
headerdiv = html.Div(id = 'header-div',
                children = [header1],
                )
maindiv = html.Div(id = 'main-div',
                children = [codeinput],
                )

headerdiv1 = html.Div(id = 'header-div-1',
                children = [],
                )
maindiv1 = html.Div(id = 'main-div-1',
                children = [participanttable,nextbutton],
                )

scorediv = html.Div(id = 'score-div',
                children = [],
                )
"""
Instructor components
"""
header3 = html.H4(children = ['Hey Coach!'], style = {'textAlign' : "center",'margin-top':'30px'})

header4 = html.H6(children = ['Select Workout'], style = {'textAlign' : "center",'margin-top':'30px'})

instructorname = dcc.Input(id = 'instructor-name-input', type = 'text', placeholder = "Enter Name", maxLength = '10', style = {'textAlign' : "center", 'display':'block','margin-left':'auto','margin-right':'auto', 'margin-top':'15px'})

impostorselect = dbc.Button('Impostor', id = 'impostor-select',n_clicks=0, style = {'textAlign' : "center", 'display':'block','margin-left':'auto','margin-right':'auto','margin-top':'20px'})

"""
Main body layout components - instructor
"""

headerdiv2 = html.Div(id = 'header-div-2',
                children = [header3],
                )
maindiv2 = html.Div(id = 'main-div-2',
                children = [instructorname,header4,impostorselect],
                )

scorediv1 = html.Div(id = 'score-div-1',
                children = [],
                )

"""
Default Page Layouts
"""

def Homepage():
    layout = [navbar, 
              dbc.Container([
                dbc.Row([
                    dbc.Col([headerdiv,
                             maindiv,
                             scorediv
                             ])
                    ])
        ])
              ]
    return layout

                        
def Instructor():
    layout = html.Div([navbar,
                       dbc.Row([
                    dbc.Col([headerdiv2,
                             maindiv2,
                             scorediv1
                             ])
                    ])
    ])
    return layout
    
def Workout():
    layout = [navbar, 
              dbc.Container([
                dbc.Row([
                    dbc.Col([headerdiv1,
                             maindiv1,
                             scorediv
                             ])
                    ])
        ])
              ]
    return layout

"""
Update functions for default layouts based on current state
"""

def update_inputs(codein):
    if codein == code:
        headerlayout = [header2]
        mainlayout = [nameinput, enterbutton]
    elif codein:
        if len(codein) > 3:
            headerlayout = [header1]
            mainlayout = [codeinput,cemsg]
        else:
            headerlayout = [header1]
            mainlayout = [codeinput]
    else:
        headerlayout = [header1]
        mainlayout = [codeinput]
        
    return headerlayout, mainlayout
    
#def update_instructor_inputs():
    

def update_workout(index):
    for i in regular_structure.keys():
        print(i)
        for j in regular_structure[i]['index'].keys():
            print(j)
            if j == index:
                print('found')
                screentype = i
                exercisetype = regular_structure[i]['index'][j]
                break
            else:
                screentype = 'initial'
                exercisetype = None
        if j == index:
            break
        
    if screentype == 'inputs':
        headerlayout = []
        mainlayout = [participanttable,nextbutton]
        scorelayout = []
    elif screentype == 'warmup':
        headerlayout = Warmcool(index)
        if regular_structure['warmup']['index'][index] == 'Warmup':
            mainlayout = [nextbutton]
        elif regular_structure['warmup']['index'][index] == 'Cooldown':
            mainlayout = [quitbutton]
        scorelayout = []
    elif screentype == 'leaderboard':
        headerlayout = []
        mainlayout = [participanttable,nextbutton]
        scorelayout = []
    elif screentype == 'numinput':
        headerlayout = [html.H4(children = [exercisetype], style = {'textAlign' : "center",'margin-top':'30px'})]
        mainlayout = [numberinput,nextbutton]
        scorelayout = []
    elif screentype == 'abinput':
        headerlayout = [html.H4(children = [exercisetype], style = {'textAlign' : "center",'margin-top':'30px'})]
        mainlayout = [abutton,bbutton,nextbutton]
        scorelayout = []
    elif screentype == 'abcdinput':
        headerlayout = [html.H4(children = [exercisetype], style = {'textAlign' : "center",'margin-top':'30px'})]
        mainlayout = [abutton,bbutton,cbutton,dbutton,nextbutton]
        scorelayout = []
    elif screentype == 'impostorinput':
        headerlayout = [html.H4(children = [exercisetype], style = {'textAlign' : "center",'margin-top':'30px'})]
        mainlayout = [impostorguess,nextbutton]
        scorelayout = []
    else:
        headerlayout = []
        mainlayout = [participanttable,nextbutton]
        scorelayout = []
    return headerlayout, mainlayout, scorelayout


    
    

    

