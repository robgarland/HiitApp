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
                        'Current Index' : 'Number' (starting at -1)
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
    'Impostor',
    'Memory'
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

"""
Workout Structures
"""

impostor_structure = {
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
    'numinput' : {'index' : {4 : [exercise[2]], 
                             5 : [exercise[3]], 
                             8 : [exercise[6]], 
                             9 : [exercise[7]], 
                             14 :[exercise[12]], 
                             15 :[exercise[13]], 
                             18 : [exercise[13]], 
                             19 : [exercise[12]], 
                             24 : [exercise[7]], 
                             25 : [exercise[6]], 
                             28 : [exercise[3]], 
                             29 : exercise[2]
                             }
                  },
    'abinput' : {'index' : {2 : [exercise[0]], 
                            3 : [exercise[1]], 
                            12 : [exercise[10]], 
                            13 : [exercise[11]],
                            20 : [exercise[11]],
                            21 : [exercise[10]],
                            30 : [exercise[1]],
                            31 : [exercise[0]]
                            }
                 },
    'abcdinput' : {'index' :{6 : [exercise[4]], 
                             7 : [exercise[5]], 
                             10 : [exercise[8]], 
                             11 : [exercise[9]], 
                             22 : [exercise[9]], 
                             23 : [exercise[8]], 
                             26 : [exercise[5]], 
                             27 : [exercise[4]]
                             }
                   },
    'impostorinput' : {'index' : {16 : 'First Guess', 32 : 'Final Guess'}}
          }

memory_structure = {
    'inputs' : {'index' : {0 : 'Inputs'
                                            }
                                 },
    'warmup' : {'index' : {1 : 'Warmup',
                           14 : 'Halfway',
                           28 : 'Cooldown'
                                 }
                      },
    'leaderboard' : {'index' : {15 : 'Current Standings', 
                                29 : 'Final Standings'
                                }
                     },
    'abinput' : {'index' : {2 : [exercise[0]], 
                            3 : [exercise[1]],
                            4 : [exercise[2]],
                            5 : [exercise[3]],
                            24 : [exercise[3]],
                            25 : [exercise[2]],
                            26 : [exercise[1]],
                            27 : [exercise[0]] 
                            }
                 },
    'abcdinput' : {'index' :{8 : [exercise[6]], 
                             9 : [exercise[7]], 
                             10 : [exercise[8]], 
                             11 : [exercise[9]], 
                             18 : [exercise[9]], 
                             19 : [exercise[8]], 
                             20 : [exercise[7]], 
                             21 : [exercise[6]]
                             }
                   },
    'intenseburst': {'index' : {6 : [exercise[4]],
                                7 : [exercise[5]],
                                12 : [exercise[10]], 
                                13 : [exercise[11]],
                                16 : [exercise[11]],
                                17 : [exercise[10]],
                                22 : [exercise[5]],
                                23 : [exercise[4]]
                                }
                     }
          }

"""
All Elements/Creation of Elements Below
"""


def Navbar():
     navbar = dbc.Navbar([dbc.NavbarBrand("Hiit Me Up Workout"),
                          dbc.NavLink("Quit", href="/", className="ml-auto",style = {'color':'#5AC4D8'})
                          ], color = '#0A455A', dark = True)
    
    
    # navbar = dbc.Navbar(
    #        children=[
    #            dbc.Nav([dbc.NavbarBrand("Hiit Me Up Workout"),
    #            dbc.NavItem(dbc.NavLink("Quit", href="/")),
    #            fill = True
    #            justified = True
    #            ])
    #                 ],
    #       sticky="top"
    #     )
     return navbar

"""
Input Screen Components
"""


header1 = html.H4(children = ['Enter Code:'], style = {'textAlign' : "center",'margin-top':'30px'})

header2 = html.H4(children = ['Enter Name:'], style = {'textAlign' : "center",'margin-top':'30px'})

cemsg = html.H6(children = ['Code not recognised, please enter a valid workout code'], style = {'textAlign' : 'center','margin-top':'30px','color':'red'})

codeinput = dcc.Input(id = 'code-input', type = 'text', placeholder = "4-Digit Code", maxLength = '4', style = {'textAlign' : "center", 'display':'block','margin-left':'auto','margin-right':'auto', 'margin-top':'15px'})

nameinput = dcc.Dropdown(id = 'name-dropdown', options = [{'label': participants[i], 'value' : participants[i]} for i in range(len(participants))], style = {'textAlign':'center','display':'block','margin-left':'auto','margin-right':'auto','width':'80%','margin-top':'15px'})

enterbutton = dbc.Button('Enter',id = 'enter-button', n_clicks = 0, color = 'info', style = {'textAlign' : "center", 'display':'block','margin-left':'auto','margin-right':'auto','margin-top':'20px'})

startbutton = dbc.Button('Start', id = 'start-button',n_clicks=0, color= 'info', style = {'textAlign' : "center", 'display':'block','margin-left':'auto','margin-right':'auto','margin-top':'20px'})

"""
Workout Screen Components
"""
def Warmcool(index,structure):
    warmcool = html.H4(children = [structure['warmup']['index'][index]], style = {'textAlign' : "center",'margin-top':'50px'})
    return warmcool

participanttable = html.Table( children = [
    html.Thead(
        html.Tr(
            html.Th('Current Participants')
            )
        ),
    html.Tbody(
        children = [html.Tr([
            html.Td(participants[i])
            ]) for i in range(len(participants))], id = 'current-participants'
        )
    ], style = {'textAlign' : "center",'margin-left':'auto','margin-right':'auto', 'margin-top':'15px'})

check_participant_interval = dcc.Interval(id = 'check-participants-interval', interval = 2000, n_intervals = 0)

update_time_interval = dcc.Interval(id = 'update-time-interval', interval = 1000, n_intervals = 0)

nextbutton = dbc.Button('Next',id = 'next-button', n_clicks = 0, style = {'textAlign' : "center", 'display':'block','margin-left':'auto','margin-right':'auto','margin-top':'20px'})

abutton = dbc.Button('A',id = 'a-button',n_clicks=0, style = {'textAlign' : "center", 'display':'block','margin-left':'auto','margin-right':'auto','margin-top':'20px'})

bbutton = dbc.Button('B',id = 'b-button',n_clicks=0, style = {'textAlign' : "center", 'display':'block','margin-left':'auto','margin-right':'auto','margin-top':'20px'})

abutton1 = dbc.Button('A',id = 'a-button-1',n_clicks=0, color = 'danger', style = {'textAlign' : "center", 'display':'block','margin-left':'auto','margin-right':'auto','margin-top':'20px'})

bbutton1 = dbc.Button('B',id = 'b-button-1',n_clicks=0, color = 'primary', style = {'textAlign' : "center", 'display':'block','margin-left':'auto','margin-right':'auto','margin-top':'20px'})

cbutton1 = dbc.Button('C',id = 'c-button-1',n_clicks=0, color = 'warning', style = {'textAlign' : "center", 'display':'block','margin-left':'auto','margin-right':'auto','margin-top':'20px'})

dbutton1 = dbc.Button('D',id = 'd-button-1',n_clicks=0, color = 'success', style = {'textAlign' : "center", 'display':'block','margin-left':'auto','margin-right':'auto','margin-top':'20px'})

numberinput = dcc.Input(id = 'number-input', type = 'number', placeholder = "X", max = '100', style = {'textAlign' : "center", 'display':'block','margin-left':'auto','margin-right':'auto', 'margin-top':'15px'})
                   
impostorguess = dcc.Dropdown(id = 'impostor-dropdown', options = [{'label': participants[i], 'value' : participants[i]} for i in range(len(participants))], style = {'textAlign':'center','display':'block','margin-left':'auto','margin-right':'auto','width':'80%','margin-top':'15px'})

quitbutton = dbc.Button('Quit',id = 'quit-button', href = "/", color = 'danger', style = {'textAlign' : "center", 'display':'block','margin-left':'auto','margin-right':'auto','margin-top':'20px'})

"""
Main body layout Components
"""

navbar = Navbar()
                   
headerdiv = html.Div(id = 'header-div',
                children = [header1]
                )
maindiv = html.Div(id = 'main-div',
                children = [codeinput,enterbutton]
                )

headerdiv1 = html.Div(id = 'header-div-1',
                children = []
                )
maindiv1 = html.Div(id = 'main-div-1',
                children = [participanttable,nextbutton]
                )

scorediv = html.Div(id = 'score-div',
                children = []
                )

"""
Instructor components
"""
header3 = html.H4(children = ['Hey Coach!'], style = {'textAlign' : "center",'margin-top':'30px'})

header4 = html.H6(children = ['Select Workout'], style = {'textAlign' : "center",'margin-top':'30px'})

instructorname = dcc.Input(id = 'instructor-name-input', type = 'text', placeholder = "Enter Name", maxLength = '10', style = {'textAlign' : "center", 'display':'block','margin-left':'auto','margin-right':'auto', 'margin-top':'15px'})

impostorselect = dbc.Button('Impostor', id = 'impostor-select',n_clicks=0, color = 'dark', style = {'textAlign' : "center", 'display':'block','margin-left':'auto','width':'66%','margin-right':'auto','margin-top':'20px'})

memoryselect = dbc.Button('Memory', id = 'memory-select',n_clicks=0, color = 'info', style = {'textAlign' : "center", 'display':'block','margin-left':'auto','width':'66%','margin-right':'auto','margin-top':'20px'})

tugofwarselect = dbc.Button('Tug of War', id = 'tugofwar-select',n_clicks=0, color = 'secondary', style = {'textAlign' : "center", 'display':'block','margin-left':'auto','width':'66%','margin-right':'auto','margin-top':'20px'})

bullseyeselect = dbc.Button('Bullseye', id = 'bullseye-select',n_clicks=0, color = 'warning', style = {'textAlign' : "center", 'display':'block','margin-left':'auto','width':'66%','margin-right':'auto','margin-top':'20px'})

nemsg = html.H6(children = ['Please enter your name'], style = {'textAlign' : 'center','margin-top':'30px','color':'red'})

moveonbutton = dbc.Button('Move On -->', id = 'moveon-button',n_clicks=0, color= 'info', style = {'textAlign' : "center", 'display':'block','margin-left':'auto','margin-right':'auto','margin-top':'20px'})

"""
Main body layout components - instructor
"""

headerdiv2 = html.Div(id = 'header-div-2',
                children = [header3]
                )
maindiv2 = html.Div(id = 'main-div-2',
                children = [instructorname,header4,impostorselect,memoryselect,tugofwarselect,bullseyeselect]
                )

scorediv2 = html.Div(id = 'score-div-2',
                children = []
                )

headerdiv3 = html.Div(id = 'header-div-3',
                children = []
                )
maindiv3 = html.Div(id = 'main-div-3',
                children = []
                )

scorediv3 = html.Div(id = 'score-div-3',
                children = []
                )

"""
Default Page Layouts
"""

def Homepage():
    layout = [navbar, 
                dbc.Row([
                    dbc.Col([headerdiv,
                             maindiv,
                             scorediv
                             ])
        ])
              ]
    return layout

                        
def Instructor():
    layout = html.Div([navbar,
                       dbc.Row([
                    dbc.Col([headerdiv2,
                             maindiv2,
                             scorediv2
                             ])
                    ])
    ])
    return layout
    
def Workout():
    layout = [navbar, 
                dbc.Row([
                    dbc.Col([headerdiv1,
                             maindiv1,
                             scorediv
                             ])
                    ])
              ]
    return layout

def InstructorWorkout():
    layout = [navbar, 
                dbc.Row([
                    dbc.Col([headerdiv3,
                             maindiv3,
                             scorediv3
                             ])
                    ])
              ]
    return layout

"""
Update functions for default layouts based on current state
"""

def update_inputs(codein):
    if codein in sessioninfo.keys():
        headerlayout = [header2]
        mainlayout = [nameinput, startbutton]
        hidden = [codein]
    elif codein:
        headerlayout = [header1]
        mainlayout = [codeinput,cemsg,enterbutton]
        hidden = [codein]
    else:
        headerlayout = [header1]
        mainlayout = [codeinput,enterbutton]
        hidden = []
        
    return headerlayout, mainlayout, hidden

def instructor_setup(sessiontype,name):
    if sessiontype in workouttypes:
        if name:
            code = generate_code()
            while code in sessioninfo.keys():
                code = generate_code()              #ensuring no duplicate code is produced
                    
            sessioninfo[code] = {'Instructor':name,'Workout Type':sessiontype,'Current Index':-1,'Participants':[],'Teamscores':{'A':0,'B':0}} #note the a/b thing can change based on the survey we create, and the inputs will affect the team types (user can chooose what to split by somehow, needs development)
            header = [html.H6(children = ['Instructor Name:'], style = {'textAlign' : "center",'margin-top':'30px'}),
                      html.H4(children = [name], style = {'textAlign' : "center",'margin-top':'30px'}),
                      html.H6(children = ['Selected Workout:'], style = {'textAlign' : "center",'margin-top':'30px'}),
                      html.H4(children = [sessiontype], style = {'textAlign' : "center",'margin-top':'30px'})]
            main = [html.H6(['Code:'], style = {'textAlign' : "center",'margin-top':'30px'}),
                    html.H4(children = ['{}'.format(code)], style = {'textAlign' : "center",'margin-top':'30px'}),
                    participanttable,startbutton,dcc.Dropdown(id = 'name-dropdown',style = {'display':'none'}),check_participant_interval]
            score = []
            hidden = [code]
            return header, main, score, hidden
        else:
            header = [header3]
            main = [instructorname,nemsg,header4,impostorselect,memoryselect,tugofwarselect,bullseyeselect]
            score = []
            hidden = []
            return header, main, score, hidden
    else:
        header = [header3]
        main = [instructorname,header4,impostorselect,memoryselect,tugofwarselect,bullseyeselect]
        score = []
        return header, main, score, hidden

def workout_structure(code):
    if code:
        if sessioninfo[code]['Workout Type'] == 'Impostor':
            structure = impostor_structure
        elif sessioninfo[code]['Workout Type'] == 'Memory':
            structure = memory_structure
    else:
        structure = {}
    return structure

def enter_session(code,name):
    if code:
        sessioninfo[code]['Participants'].append({'Name':name,'Team':'','Scores':[]})

def update_participants_body(code):
    if len(sessioninfo[code]['Participants']) > 0:
        body =  [[html.Tr([
                html.Td(sessioninfo[code]['Participants'][i]['Name'])
                ]) for i in range(len(sessioninfo[code]['Participants']))]]    
    else:
        body = [[html.Tr([html.Td('Waiting For Participants')])]]   
    return body

# def update_workout(index):
#     for i in regular_structure.keys():
#         for j in regular_structure[i]['index'].keys():
#             if j == index:
#                 screentype = i
#                 exercisetype = regular_structure[i]['index'][j]
#                 break
#             else:
#                 screentype = 'initial'
#                 exercisetype = None
#         if j == index:
#             break       
#     if screentype == 'inputs':
#         headerlayout = [html.H6(children = ['Instructor Name:'], style = {'textAlign' : "center",'margin-top':'30px'}),
#                       html.H4(children = [name], style = {'textAlign' : "center",'margin-top':'30px'}),
#                       html.H6(children = ['Selected Workout:'], style = {'textAlign' : "center",'margin-top':'30px'}),
#                       html.H4(children = [sessiontype], style = {'textAlign' : "center",'margin-top':'30px'})]
#         mainlayout = [participanttable,nextbutton]
#         scorelayout = []
#     elif screentype == 'warmup':
#         headerlayout = Warmcool(index)
#         if regular_structure['warmup']['index'][index] == 'Warmup':
#             mainlayout = [nextbutton]
#         elif regular_structure['warmup']['index'][index] == 'Cooldown':
#             mainlayout = [quitbutton]
#         scorelayout = []
#     elif screentype == 'leaderboard':
#         headerlayout = []
#         mainlayout = [participanttable,nextbutton]
#         scorelayout = []
#     elif screentype == 'numinput':
#         headerlayout = [html.H4(children = [exercisetype], style = {'textAlign' : "center",'margin-top':'30px'})]
#         mainlayout = [numberinput,nextbutton]
#         scorelayout = []
#     elif screentype == 'abinput':
#         headerlayout = [html.H4(children = [exercisetype], style = {'textAlign' : "center",'margin-top':'30px'})]
#         mainlayout = [abutton,bbutton,nextbutton]
#         scorelayout = []
#     elif screentype == 'abcdinput':
#         headerlayout = [html.H4(children = [exercisetype], style = {'textAlign' : "center",'margin-top':'30px'})]
#         mainlayout = [abutton,bbutton,cbutton,dbutton,nextbutton]
#         scorelayout = []
#     elif screentype == 'impostorinput':
#         headerlayout = [html.H4(children = [exercisetype], style = {'textAlign' : "center",'margin-top':'30px'})]
#         mainlayout = [impostorguess,nextbutton]
#         scorelayout = []
#     elif screentype == 'intenseburst':
#         headerlayout = [html.H4(children = [exercisetype], style = {'textAlign' : "center",'margin-top':'30px'})]
#         mainlayout = [impostorguess,nextbutton]
#         scorelayout = []
#     else:
#         headerlayout = []
#         mainlayout = [participanttable,nextbutton]
#         scorelayout = []
#     return headerlayout, mainlayout, scorelayout


    
    

    

