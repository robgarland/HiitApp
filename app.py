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
from sheets_integration import GetSurvey
"""
Data Structure Components
"""
"""
Session Info ideal layout
session info = {'CODE':{'Instructor':'Name',
                        'Workout Type':'Type',
                        'Current Index' : 'Number' (starting at 0)
                        'Current State' : 'Exercise/Rest'
                        'Structure' : 
                        'Participants':[{'Name':'Name',
                                         'Team':'Team',
                                         'Scores':{'Index':{'Entry':'Entry',
                                                    'Score':'Score'}
                                                    }
                                         'Total Score' : 'Score'
                                         }],
                        Teamscores:{'A': 'Score', 
                                    'B':'Score',C...
                                    }
                        }
    }
"""

surveyresults = GetSurvey()

sessioninfo = {}

survey_participants = surveyresults['First Name']

workouttypes = [
    'Impostor',
    'Icebreaker'
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
    'inputs' : {'index' : {0 : {'Exercise': 'Inputs'}
                                            }
                                 },
    'warmup' : {'index' : {1 : {'Exercise': 'Warmup'}, 
                           33 : {'Exercise': 'Cooldown'}
                                 }
                      },
    'leaderboard' : {'index' : {17 : {'Exercise': 'Current Standings'}, 
                                34 : {'Exercise': 'Final Standings'}
                                },
                     'participants' : {}
                     },
    'numinput' : {'index' : {4 : {'Exercise' : exercise[2]}, 
                             5 : {'Exercise' :exercise[3]}, 
                             8 : {'Exercise' :exercise[6]}, 
                             9 : {'Exercise' :exercise[7]}, 
                             14 : {'Exercise' :exercise[12]}, 
                             15 : {'Exercise' :exercise[13]}, 
                             18 : {'Exercise' :exercise[13]}, 
                             19 : {'Exercise' :exercise[12]}, 
                             24 : {'Exercise' :exercise[7]}, 
                             25 : {'Exercise' :exercise[6]}, 
                             28 : {'Exercise' :exercise[3]}, 
                             29 : {'Exercise' :exercise[2]}
                             }
                  },
    'abinput' : {'index' : {2 : {'Exercise' :exercise[0]}, 
                            3 : {'Exercise' :exercise[1]}, 
                            12 : {'Exercise' :exercise[10]}, 
                            13 : {'Exercise' :exercise[11]},
                            20 : {'Exercise' :exercise[11]},
                            21 : {'Exercise' :exercise[10]},
                            30 : {'Exercise' :exercise[1]},
                            31 : {'Exercise' :exercise[0]}
                            }
                 },
    'abcdinput' : {'index' :{6 : {'Exercise' :exercise[4]}, 
                             7 : {'Exercise' :exercise[5]}, 
                             10 : {'Exercise' :exercise[8]}, 
                             11 : {'Exercise' :exercise[9]}, 
                             22 : {'Exercise' :exercise[9]}, 
                             23 : {'Exercise' :exercise[8]}, 
                             26 : {'Exercise' :exercise[5]}, 
                             27 : {'Exercise' :exercise[4]}
                             }
                   },
    'impostorinput' : {'index' : {16 : 'First Guess', 32 : 'Final Guess'}}
          }

icebreaker_structure = {
    'inputs' : {'index' : {0 : {'Exercise': 'Inputs'}
                                            }
                                 },
    'warmup' : {'index' : {1 : {'Exercise': 'Warmup'},
                           14 : {'Exercise': 'Halfway'},
                           28 : {'Exercise': 'Cooldown'}
                                 }
                      },
    'leaderboard' : {'index' : {15 : {'Exercise':'Current Standings'}, 
                                29 : {'Exercise':'Final Standings'}
                                },
                     'participants' : {}
                     },
    'abinput' : {'index' : {2 : {'Exercise' :exercise[0]}, 
                            3 : {'Exercise' :exercise[1]},
                            4 : {'Exercise' :exercise[2]},
                            5 : {'Exercise' :exercise[3]},
                            24 : {'Exercise' :exercise[3]},
                            25 : {'Exercise' :exercise[2]},
                            26 : {'Exercise' :exercise[1]},
                            27 : {'Exercise' :exercise[0]} 
                            }
                 },
    'abcdinput' : {'index' :{8 : {'Exercise' :exercise[6]}, 
                             9 : {'Exercise' :exercise[7]}, 
                             10 : {'Exercise' :exercise[8]}, 
                             11 : {'Exercise' :exercise[9]}, 
                             18 : {'Exercise' :exercise[9]}, 
                             19 : {'Exercise' :exercise[8]}, 
                             20 : {'Exercise' :exercise[7]}, 
                             21 : {'Exercise' :exercise[6]}
                             }
                   },
    'intenseburst': {'index' : {6 : {'Exercise' :exercise[4]},
                                7 : {'Exercise' :exercise[5]},
                                12 : {'Exercise' :exercise[10]}, 
                                13 : {'Exercise' :exercise[11]},
                                16 : {'Exercise' :exercise[11]},
                                17 : {'Exercise' :exercise[10]},
                                22 : {'Exercise' :exercise[5]},
                                23 : {'Exercise' :exercise[4]}
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

nameinput = dcc.Dropdown(id = 'name-dropdown', options = [{'label': survey_participants.iloc[i], 'value' : survey_participants.iloc[i]} for i in range(len(survey_participants))], style = {'textAlign':'center','display':'block','margin-left':'auto','margin-right':'auto','width':'80%','margin-top':'15px'})

enterbutton = dbc.Button('Enter',id = 'enter-button', n_clicks = 0, color = 'info', style = {'textAlign' : "center", 'display':'block','margin-left':'auto','margin-right':'auto','margin-top':'20px'})

startbutton = dbc.Button('Start', id = 'start-button',n_clicks=0, color= 'info', style = {'textAlign' : "center", 'display':'block','margin-left':'auto','margin-right':'auto','margin-top':'20px'})

"""
Workout Screen Components
"""
def Warmcool(index,structure):
    warmcool = html.H4(children = [structure['warmup']['index'][index]['Exercise']], style = {'textAlign' : "center",'margin-top':'50px'})
    return warmcool

def participant_table(code):
    totalpeople = len(sessioninfo[code]['Participants'])
    if totalpeople > 0:
        participanttable = html.Table(children = [
            html.Thead(
                html.Tr(
                    html.Th('Current Participants')
                    )
                ),
            html.Tbody(
                children = [html.Tr([
                    html.Td(sessioninfo[code]['Participants'][i]['Name'])
                    ]) for i in range(totalpeople)], id = 'current-participants'
                )
            ], style = {'textAlign' : "center",'margin-left':'auto','margin-right':'auto', 'margin-top':'30px'})
        return participanttable
    else:
        participanttable = html.Table(children = [
        html.Thead(
            html.Tr(
                html.Th('Current Participants')
                )
            ),
        html.Tbody(
            children = [html.Tr([
                html.Td('Waiting for Participants')
                ])], id = 'current-participants'
            )
        ], style = {'textAlign' : "center",'margin-left':'auto','margin-right':'auto', 'margin-top':'30px'})
        return participanttable
            

check_participant_interval = dcc.Interval(id = 'check-participants-interval', interval = 2000, n_intervals = 0)

update_exercise_interval = dcc.Interval(id = 'update-exercise-interval', interval = 1000, n_intervals = 0)

submitbutton = dbc.Button('Submit',id = 'submit-button', n_clicks = 0, style = {'textAlign' : "center", 'display':'block','margin-left':'auto','margin-right':'auto','margin-top':'20px'})

abutton = dbc.Button('A',id = 'a-button',n_clicks=0, color = 'info', style = {'textAlign' : "center", 'display':'block','margin-left':'auto','margin-right':'auto', 'margin-top':'20px', 'width':'75vw', 'height':'20vh', 'font-size':'xx-large'})

bbutton = dbc.Button('B',id = 'b-button',n_clicks=0, color = 'info',style = {'textAlign' : "center", 'display':'block','margin-left':'auto','margin-right':'auto','margin-top':'20px','width':'75vw', 'height':'20vh','font-size':'xx-large'})

abutton1 = dbc.Button('A',id = 'a-button-1',n_clicks=0, color = 'danger', style = {'textAlign' : "center", 'display':'block','margin-left':'auto','margin-right':'auto','margin-top':'20px'})

bbutton1 = dbc.Button('B',id = 'b-button-1',n_clicks=0, color = 'primary', style = {'textAlign' : "center", 'display':'block','margin-left':'auto','margin-right':'auto','margin-top':'20px'})

cbutton1 = dbc.Button('C',id = 'c-button-1',n_clicks=0, color = 'warning', style = {'textAlign' : "center", 'display':'block','margin-left':'auto','margin-right':'auto','margin-top':'20px'})

dbutton1 = dbc.Button('D',id = 'd-button-1',n_clicks=0, color = 'success', style = {'textAlign' : "center", 'display':'block','margin-left':'auto','margin-right':'auto','margin-top':'20px'})

numberinput = dcc.Input(id = 'number-input', type = 'number', placeholder = "X", max = '100', style = {'textAlign' : "center", 'display':'block','margin-left':'auto','margin-right':'auto', 'margin-top':'15px'})
                   
impostorguess = dcc.Dropdown(id = 'impostor-dropdown', options = [{'label': survey_participants.iloc[i], 'value' : survey_participants.iloc[i]} for i in range(len(survey_participants))], style = {'textAlign':'center','display':'block','margin-left':'auto','margin-right':'auto','width':'80%','margin-top':'15px'})

quitbutton = dbc.Button('Quit',id = 'quit-button', href = "/", color = 'danger', style = {'textAlign' : "center", 'display':'block','margin-left':'auto','margin-right':'auto','margin-top':'20px','width':'75vw', 'height':'10vh'})

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
                children = [update_exercise_interval]
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

icebreakerselect = dbc.Button('Icebreaker', id = 'icebreaker-select',n_clicks=0, color = 'info', style = {'textAlign' : "center", 'display':'block','margin-left':'auto','width':'66%','margin-right':'auto','margin-top':'20px'})

tugofwarselect = dbc.Button('Tug of War', id = 'tugofwar-select',n_clicks=0, color = 'secondary', style = {'textAlign' : "center", 'display':'block','margin-left':'auto','width':'66%','margin-right':'auto','margin-top':'20px'})

bullseyeselect = dbc.Button('Bullseye', id = 'bullseye-select',n_clicks=0, color = 'warning', style = {'textAlign' : "center", 'display':'block','margin-left':'auto','width':'66%','margin-right':'auto','margin-top':'20px'})

nemsg = html.H6(children = ['Please enter your name'], style = {'textAlign' : 'center','margin-top':'30px','color':'red'})

moveonbutton_re = dbc.Button('Move On -->', id = 'moveon-button-to-rest',n_clicks=0, color= 'info', style = {'textAlign' : "center", 'display':'block','margin-left':'auto','margin-right':'auto','margin-top':'20px'})

moveonbutton_ex = dbc.Button('Move On -->', id = 'moveon-button-to-exercise',n_clicks=0, color= 'info', style = {'textAlign' : "center", 'display':'block','margin-left':'auto','margin-right':'auto','margin-top':'20px'})

hidden_moveonbutton_ex = dbc.Button(id = 'moveon-button-to-exercise', style = {'display':'none'})

hidden_moveonbutton_re = dbc.Button(id = 'moveon-button-to-rest', style = {'display':'none'})

"""
Main body layout components - instructor
"""

headerdiv2 = html.Div(id = 'header-div-2',
                children = [header3]
                )
maindiv2 = html.Div(id = 'main-div-2',
                children = [instructorname,header4,impostorselect,icebreakerselect,tugofwarselect,bullseyeselect]
                )

scorediv2 = html.Div(id = 'score-div-2',
                children = []
                )

headerdiv3 = html.Div(id = 'header-div-3',
                children = []
                )
maindiv3 = html.Div(id = 'main-div-3',
                children = [moveonbutton_ex,hidden_moveonbutton_re]
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
def update_survey_results():
    global surveyresults
    surveyresults = GetSurvey() 
    
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
                    
            sessioninfo[code] = {'Instructor':name,'Workout Type':sessiontype,'Structure': {'inputs' : {'index' : {0 : {'Exercise': 'Inputs'}}}}, 'Current Index':0, 'Current State': 'Exercise', 'Participants':[],'Teamscores':{'A':0,'B':0}} #note the a/b thing can change based on the survey we create, and the inputs will affect the team types (user can chooose what to split by somehow, needs development)
            header = [html.H6(children = ['Instructor Name:'], style = {'textAlign' : "center",'margin-top':'30px'}),
                      html.H4(children = [name], style = {'textAlign' : "center",'margin-top':'30px'}),
                      html.H6(children = ['Selected Workout:'], style = {'textAlign' : "center",'margin-top':'30px'}),
                      html.H4(children = [sessiontype], style = {'textAlign' : "center",'margin-top':'30px'})]
            participanttable = participant_table(code)
            main = [html.H6(['Code:'], style = {'textAlign' : "center",'margin-top':'30px'}),
                    html.H4(children = ['{}'.format(code)], style = {'textAlign' : "center",'margin-top':'30px'}),
                    participanttable,startbutton,dcc.Dropdown(id = 'name-dropdown',style = {'display':'none'}),check_participant_interval]
            score = []
            hidden = [code]
            update_survey_results()
            return header, main, score, hidden
        else:
            header = [header3]
            main = [instructorname,nemsg,header4,impostorselect,icebreakerselect,tugofwarselect,bullseyeselect]
            score = []
            hidden = []
            return header, main, score, hidden
    else:
        header = [header3]
        main = [instructorname,header4,impostorselect,icebreakerselect,tugofwarselect,bullseyeselect]
        score = []
        return header, main, score, hidden

def workout_structure(code):
    if code:
        if sessioninfo[code]['Workout Type'] == 'Impostor':
            structure = impostor_structure
            session_users = finalize_participants(code,structure)
            generate_ab_patterns(structure)
            generate_questions(structure,session_users)
            sessioninfo[code]['Structure'] = structure

        elif sessioninfo[code]['Workout Type'] == 'Icebreaker':
            structure = icebreaker_structure
            session_users = finalize_participants(code,structure)
            generate_ab_patterns(structure)
            generate_questions(structure,session_users)
            sessioninfo[code]['Structure'] = structure
            
def finalize_participants(code,structure):
    if code:
        sessionparticipants = []
        for i in range(len(sessioninfo[code]['Participants'])):

            structure['leaderboard']['participants'][i] = sessioninfo[code]['Participants'][i]['Name']
            sessionparticipants.append(sessioninfo[code]['Participants'][i]['Name'])
            
        return sessionparticipants
        
def generate_ab_patterns(structure, size = 5, chars = 'AB'):
    for i in structure['abinput']['index'].keys():
        target = 'Pattern'
        answer = ''.join(r.choice(chars) for _ in range(size))
        structure['abinput']['index'][i]['Target'] = target
        structure['abinput']['index'][i]['Answer'] = answer

def generate_questions(structure,session_users):
    headers = surveyresults.columns.tolist()
    for i in structure['abcdinput']['index'].keys():
        target = headers[r.randint(4,len(headers)-1)]
        possibleoptions = surveyresults[target].unique()
        
        targetindex = r.randint(0,len(surveyresults)-1)
        targetplayer = surveyresults.loc[targetindex,'First Name']
        
        while targetplayer not in session_users:
             targetindex = r.randint(0,len(surveyresults)-1)
             targetplayer = surveyresults.loc[targetindex,'First Name']
            
        correct = surveyresults.loc[targetindex,target]
        
        while len(possibleoptions) == 1:
            target = headers[r.randint(4,len(headers)-1)]
            possibleoptions = surveyresults[target].unique()
            correct = surveyresults.loc[targetindex,target]
        
        if len(possibleoptions) == 2:
            ABCD = ['A','B']
            location = ABCD.pop(r.randint(0,len(ABCD)-1))
            answer = {location : correct}
            options = {}
            options[location] = correct
            while len(options) < 2:
                toadd = possibleoptions[r.randint(0,len(possibleoptions)-1)]
                while toadd in options.values():
                    toadd = possibleoptions[r.randint(0,len(possibleoptions)-1)]
                location1 = ABCD.pop(r.randint(0,len(ABCD)-1))
                options[location1] = toadd
        
        elif len(possibleoptions) == 3:
            ABCD = ['A','B','C']
            location = ABCD.pop(r.randint(0,len(ABCD)-1))
            answer = {location : correct}
            options = {}
            options[location] = correct
            while len(options) < 3:
                toadd = possibleoptions[r.randint(0,len(possibleoptions)-1)]
                while toadd in options.values():
                    toadd = possibleoptions[r.randint(0,len(possibleoptions)-1)]
                location1 = ABCD.pop(r.randint(0,len(ABCD)-1))
                options[location1] = toadd
                
        elif len(possibleoptions) >= 4:
            ABCD = ['A','B','C','D']
            location = ABCD.pop(r.randint(0,len(ABCD)-1))
            answer = {location : correct}
            options = {}
            options[location] = correct
            while len(options) < 4:
                toadd = possibleoptions[r.randint(0,len(possibleoptions)-1)]
                while toadd in options.values():
                    toadd = possibleoptions[r.randint(0,len(possibleoptions)-1)]
                location1 = ABCD.pop(r.randint(0,len(ABCD)-1))
                options[location1] = toadd       
                
        structure['abcdinput']['index'][i]['Target'] = target
        structure['abcdinput']['index'][i]['Target Player'] = targetplayer
        structure['abcdinput']['index'][i]['Answer'] = answer
        structure['abcdinput']['index'][i]['Options'] = options
       
def enter_session(code,name):
    if code:
        sessioninfo[code]['Participants'].append({'Name':name,'Team':'','Scores':{},'Total Score':0})

def update_participants_body(code):
    if len(sessioninfo[code]['Participants']) > 0:
        body =  [[html.Tr([
                html.Td(sessioninfo[code]['Participants'][i]['Name'])
                ]) for i in range(len(sessioninfo[code]['Participants']))]]    
    else:
        body = [[html.Tr([html.Td('Waiting For Participants')])]]   
    return body

def get_index(code):
    if code:
        index = sessioninfo[code]['Current Index']
        return index
    else:
        return 0
    
def update_index(code):
    if code:
        sessioninfo[code]['Current Index'] += 1
        return sessioninfo[code]['Current Index']
    else:
        return sessioninfo[code]['Current Index']

def state_to_rest(code):
    if code:
        sessioninfo[code]['Current State'] = 'Rest'
        return sessioninfo[code]['Current State']
    else:
        return sessioninfo[code]['Current State']

def state_to_exercise(code):
    if code:
        sessioninfo[code]['Current State'] = 'Exercise'
        return sessioninfo[code]['Current State']
    else:
        return sessioninfo[code]['Current State']
    
def update_instructor_workout(index, newstate, code):
    structure = sessioninfo[code]['Structure']
    for i in structure.keys():
        for j in structure[i]['index'].keys():
            if int(j) == int(index):
                screentype = i
                exercisetype = structure[i]['index'][j]['Exercise']
                break
            else:
                screentype = 'initial'
                exercisetype = None
        if int(j) == int(index):
            break
    participanttable = participant_table(code) 
    
    if screentype == 'inputs':
        headerlayout = [html.H6(children = ['Instructor Name:'], style = {'textAlign' : "center",'margin-top':'30px'}),
                      html.H4(children = [sessioninfo[code]['Instructor']], style = {'textAlign' : "center",'margin-top':'30px'}),
                      html.H6(children = ['Selected Workout:'], style = {'textAlign' : "center",'margin-top':'30px'}),
                      html.H4(children = [sessioninfo[code]['Workout Type']], style = {'textAlign' : "center",'margin-top':'30px'})]
        mainlayout = [participanttable,moveonbutton_ex,check_participant_interval,hidden_moveonbutton_re]
        scorelayout = []
        
    elif screentype == 'warmup':
        headerlayout = Warmcool(index,structure)
        if structure['warmup']['index'][index]['Exercise'] in ['Warmup','Halfway']:
            mainlayout = [moveonbutton_ex,hidden_moveonbutton_re]
        elif structure['warmup']['index'][index]['Exercise'] == 'Cooldown':
            mainlayout = [quitbutton]
        scorelayout =[]
        
    elif screentype == 'leaderboard':
        headerlayout = [html.H6(children = [structure['leaderboard']['index'][index]['Exercise']], style = {'textAlign' : "center",'margin-top':'30px'})]
        mainlayout = [participanttable,moveonbutton_ex,hidden_moveonbutton_re]
        scorelayout = []
        
    elif screentype == 'numinput':
        if newstate == 'Exercise':
            headerlayout = [html.H4(children = [exercisetype], style = {'textAlign' : "center",'margin-top':'30px'})]
            mainlayout = [numberinput,moveonbutton_re,hidden_moveonbutton_ex]
            scorelayout = []
        elif newstate == 'Rest':
            headerlayout = [html.H4(children = [exercisetype], style = {'textAlign' : "center",'margin-top':'30px'})]
            mainlayout = [numberinput,moveonbutton_ex,hidden_moveonbutton_re]
            scorelayout = []
            
    elif screentype == 'abinput':
        target = structure['abinput']['index'][index]['Target']
        answer = structure['abinput']['index'][index]['Answer']
        if newstate == 'Exercise':
            headerlayout = [html.H6(children = ['Master your Memory'], style = {'textAlign' : "center",'margin-top':'30px'}),
                        html.H4(children = [exercisetype], style = {'textAlign' : "center",'margin-top':'30px'}),
                        ]
            mainlayout = [html.H6(children = [target], style = {'textAlign' : "center",'margin-top':'30px'}),
                      html.H4(children = [answer], style = {'textAlign' : "center",'margin-top':'30px'}),
                      moveonbutton_re,hidden_moveonbutton_ex]
            scorelayout = []
        elif newstate == 'Rest':
            headerlayout = [html.H6(children = ['Master your Memory'], style = {'textAlign' : "center",'margin-top':'30px'}),
                        html.H4(children = ['Rest'], style = {'textAlign' : "center",'margin-top':'30px'}),
                        ]
            mainlayout = [html.H6(children = [target], style = {'textAlign' : "center",'margin-top':'30px'}),
                      html.H4(children = [answer], style = {'textAlign' : "center",'margin-top':'30px'}),
                      html.H6(children = ['Total Answered:'], style = {'textAlign' : "center",'margin-top':'30px'}),
                      moveonbutton_ex, hidden_moveonbutton_re]
            scorelayout = []
        
    elif screentype == 'abcdinput':
        target = structure['abcdinput']['index'][index]['Target']
        targetplayer = structure['abcdinput']['index'][index]['Target Player']
        answer = structure['abcdinput']['index'][index]['Answer']
        options = structure['abcdinput']['index'][index]['Options']
        a = list(answer.values())
        if newstate == 'Exercise':
            headerlayout = [html.H6(children = ['Workout Buddies'], style = {'textAlign' : "center",'margin-top':'30px'}),
                            html.H4(children = [exercisetype], style = {'textAlign' : "center",'margin-top':'30px'}),
                            html.H6(children = [target], style = {'textAlign' : "center",'margin-top':'30px'}),
                            html.H4(children = [targetplayer], style = {'textAlign' : "center",'margin-top':'30px'}),
                            html.H6(children = ['Answer: ',a[0]], style = {'textAlign' : "center",'margin-top':'30px'})]
            mainlayout = [moveonbutton_re, hidden_moveonbutton_ex]
            scorelayout = []
        elif newstate == 'Rest':
            headerlayout = [html.H6(children = ['Workout Buddies'], style = {'textAlign' : "center",'margin-top':'30px'}),
                            html.H4(children = ['Rest'], style = {'textAlign' : "center",'margin-top':'30px'}),
                            html.H6(children = [target], style = {'textAlign' : "center",'margin-top':'30px'}),
                            html.H4(children = [targetplayer], style = {'textAlign' : "center",'margin-top':'30px'}),
                            html.H6(children = ['Answer: ',a[0]], style = {'textAlign' : "center",'margin-top':'30px'}),
                            html.H6(children = ['Total Answered:'], style = {'textAlign' : "center",'margin-top':'30px'})]
            mainlayout = [moveonbutton_ex, hidden_moveonbutton_re]
            scorelayout = []
            
    elif screentype == 'impostorinput':
        headerlayout = [html.H4(children = [exercisetype], style = {'textAlign' : "center",'margin-top':'30px'}),
                        html.H6(children = ['Total Answered:'], style = {'textAlign' : "center",'margin-top':'30px'})]
        mainlayout = [impostorguess,moveonbutton_ex,hidden_moveonbutton_re]
        scorelayout = []
            
    elif screentype == 'intenseburst':
        if newstate == 'Exercise':
            headerlayout = [html.H6(children = ['Intense Burst'], style = {'textAlign' : "center",'margin-top':'30px'}),
                            html.H4(children = [exercisetype], style = {'textAlign' : "center",'margin-top':'30px'}),]
            mainlayout = [moveonbutton_re,hidden_moveonbutton_ex]
            scorelayout = []
        if newstate == 'Rest':
            headerlayout = [html.H6(children = ['Intense Burst'], style = {'textAlign' : "center",'margin-top':'30px'}),
                            html.H4(children = ['Rest'], style = {'textAlign' : "center",'margin-top':'30px'})]
            mainlayout = [moveonbutton_ex,hidden_moveonbutton_re]
            scorelayout = []
        
    else:
        headerlayout = []
        mainlayout = [participanttable,moveonbutton_ex,hidden_moveonbutton_re]
        scorelayout = []
    return headerlayout, mainlayout, scorelayout

def update_workout(code,name):
    index = sessioninfo[code]['Current Index']
    state = sessioninfo[code]['Current State']
    structure = sessioninfo[code]['Structure']
    for i in structure.keys():
        for j in structure[i]['index'].keys():
            if int(j) == int(index):
                screentype = i
                exercisetype = structure[i]['index'][j]['Exercise']
                break
            else:
                screentype = 'initial'
                exercisetype = None
        if int(j) == int(index):
            break
    participanttable = participant_table(code)  
    
    if screentype == 'inputs':
        headerlayout = [html.H6(children = ['Instructor Name:'], style = {'textAlign' : "center",'margin-top':'30px'}),
                      html.H4(children = [sessioninfo[code]['Instructor']], style = {'textAlign' : "center",'margin-top':'30px'}),
                      html.H6(children = ['Selected Workout:'], style = {'textAlign' : "center",'margin-top':'30px'}),
                      html.H4(children = [sessioninfo[code]['Workout Type']], style = {'textAlign' : "center",'margin-top':'30px'})]
        mainlayout = [participanttable,update_exercise_interval]
        scorelayout = []
        
    elif screentype == 'warmup':
        headerlayout = Warmcool(index,structure)
        if structure['warmup']['index'][index]['Exercise'] in ['Warmup','Halfway']:
            mainlayout = [update_exercise_interval]
        elif structure['warmup']['index'][index]['Exercise'] == 'Cooldown':
            mainlayout = [quitbutton]
        scorelayout =[]
        
    elif screentype == 'leaderboard':
        headerlayout = [html.H6(children = [structure['leaderboard']['index'][index]['Exercise']], style = {'textAlign' : "center",'margin-top':'30px'})]
        mainlayout = [update_exercise_interval, participanttable]
        scorelayout = []
        
    elif screentype == 'numinput':
        create_score_entry(code,name)
        if state == 'Exercise':
            headerlayout = [html.H4(children = [exercisetype], style = {'textAlign' : "center",'margin-top':'30px'})]
            mainlayout = [update_exercise_interval, numberinput]
            scorelayout = []
        elif state == 'Rest':
            headerlayout = [html.H4(children = ['Rest'], style = {'textAlign' : "center",'margin-top':'30px'}),
                            html.H4(children = ['Enter your number below:'], style = {'textAlign' : "center",'margin-top':'30px'})]
            mainlayout = [update_exercise_interval, numberinput]
            scorelayout = []
            
    elif screentype == 'abinput':
        create_score_entry(code,name)
        target = structure['abinput']['index'][index]['Target']
        answer = structure['abinput']['index'][index]['Answer']
        if state == 'Exercise':
            headerlayout = [html.H6(children = ['Master your Memory'], style = {'textAlign' : "center",'margin-top':'30px'}),
                            html.H4(children = [exercisetype], style = {'textAlign' : "center",'margin-top':'30px'})
                            ]
            mainlayout = [update_exercise_interval]
            scorelayout = []
        elif state == 'Rest':
            headerlayout = [html.H6(children = ['Master your Memory'], style = {'textAlign' : "center",'margin-top':'30px'}),
                            html.H4(children = ['Rest'], style = {'textAlign' : "center",'margin-top':'30px'}),
                            ]
            mainlayout = [html.H6(children = [target], style = {'textAlign' : "center",'margin-top':'30px'}),
                          html.H4(id = 'show-user-pattern', children = [update_ab_pattern(0,code,name)], style = {'textAlign' : "center",'margin-top':'30px'}),
                          abutton,bbutton,update_exercise_interval]
            print(update_ab_pattern(0,code,name))
            scorelayout = []
            
    elif screentype == 'abcdinput':
        create_score_entry(code,name)
        target = structure['abcdinput']['index'][index]['Target']
        targetplayer = structure['abcdinput']['index'][index]['Target Player']
        answer = structure['abcdinput']['index'][index]['Answer']
        options = structure['abcdinput']['index'][index]['Options']
        if state == 'Exercise':
            headerlayout = [html.H6(children = ['Workout Buddies'], style = {'textAlign' : "center",'margin-top':'30px'}),
                            html.H4(children = [exercisetype], style = {'textAlign' : "center",'margin-top':'30px'}),
                            html.H6(children = [target], style = {'textAlign' : "center",'margin-top':'30px'}),
                            html.H6(children = ['What did ', targetplayer, ' answer?'], style = {'textAlign' : "center",'margin-top':'30px'})]
            mainlayout = [update_exercise_interval]
            scorelayout = []
            
        elif state == 'Rest':
            headerlayout = [html.H6(children = ['Workout Buddies'], style = {'textAlign' : "center",'margin-top':'30px'}),
                            html.H4(children = ['Rest'], style = {'textAlign' : "center",'margin-top':'30px'}),
                            html.H6(children = [target], style = {'textAlign' : "center",'margin-top':'30px'}),
                            html.H6(children = ['What did ', targetplayer, ' answer?'], style = {'textAlign' : "center",'margin-top':'30px'})]
            if len(options) == 2: 
                mainlayout = [dbc.Button(options['A'],id = 'a-button-1',n_clicks=0, color = 'danger', style = {'textAlign' : "center", 'display':'block','margin-left':'auto','margin-right':'auto', 'margin-top':'20px', 'width':'45vw', 'height':'10vh'}),
                              dbc.Button(options['B'],id = 'b-button-1',n_clicks=0, color = 'primary', style = {'textAlign' : "center", 'display':'block','margin-left':'auto','margin-right':'auto', 'margin-top':'20px', 'width':'45vw', 'height':'10vh'}),
                              update_exercise_interval]
            elif len(options) == 3:
                mainlayout = [dbc.Button(options['A'],id = 'a-button-1',n_clicks=0, color = 'danger', style = {'textAlign' : "center", 'display':'block','margin-left':'auto','margin-right':'auto', 'margin-top':'20px', 'width':'45vw', 'height':'10vh'}),
                              dbc.Button(options['B'],id = 'b-button-1',n_clicks=0, color = 'primary', style = {'textAlign' : "center", 'display':'block','margin-left':'auto','margin-right':'auto', 'margin-top':'20px', 'width':'45vw', 'height':'10vh'}),
                              dbc.Button(options['C'],id = 'c-button-1',n_clicks=0, color = 'warning', style = {'textAlign' : "center", 'display':'block','margin-left':'auto','margin-right':'auto', 'margin-top':'20px', 'width':'45vw', 'height':'10vh'}),
                              update_exercise_interval]
            elif len(options) == 4:
                mainlayout = [dbc.Button(options['A'],id = 'a-button-1',n_clicks=0, color = 'danger', style = {'textAlign' : "center", 'display':'block','margin-left':'auto','margin-right':'auto', 'margin-top':'20px', 'width':'45vw', 'height':'10vh'}),
                              dbc.Button(options['B'],id = 'b-button-1',n_clicks=0, color = 'primary', style = {'textAlign' : "center", 'display':'block','margin-left':'auto','margin-right':'auto', 'margin-top':'20px', 'width':'45vw', 'height':'10vh'}),
                              dbc.Button(options['C'],id = 'c-button-1',n_clicks=0, color = 'warning', style = {'textAlign' : "center", 'display':'block','margin-left':'auto','margin-right':'auto', 'margin-top':'20px', 'width':'45vw', 'height':'10vh'}),
                              dbc.Button(options['D'],id = 'd-button-1',n_clicks=0, color = 'success', style = {'textAlign' : "center", 'display':'block','margin-left':'auto','margin-right':'auto', 'margin-top':'20px', 'width':'45vw', 'height':'10vh'}),
                              update_exercise_interval] 
            else:
                mainlayout = [update_exercise_interval]
            scorelayout = []
        
    elif screentype == 'impostorinput':
        create_score_entry(code,name)
        headerlayout = [html.H4(children = [exercisetype], style = {'textAlign' : "center",'margin-top':'30px'})]
        mainlayout = [impostorguess,update_exercise_interval]
        scorelayout = []
        
    elif screentype == 'intenseburst':
        if state == 'Exercise':
            headerlayout = [html.H6(children = ['Intense Burst'], style = {'textAlign' : "center",'margin-top':'30px'}),
                            html.H4(children = [exercisetype], style = {'textAlign' : "center",'margin-top':'30px'})]
            mainlayout = [update_exercise_interval]
            scorelayout = []
        elif state == 'Rest':
            headerlayout = [html.H6(children = ['Intense Burst'], style = {'textAlign' : "center",'margin-top':'30px'}),
                            html.H4(children = ['Rest'], style = {'textAlign' : "center",'margin-top':'30px'})]
            mainlayout = [update_exercise_interval]
            scorelayout = []
        
    else:
        headerlayout = []
        mainlayout = [participanttable,update_exercise_interval]
        scorelayout = []
    return headerlayout, mainlayout, scorelayout

def create_score_entry(code,name):
    index = sessioninfo[code]['Current Index']
    print(name)
    for i in range(len(sessioninfo[code]['Participants'])):
        if sessioninfo[code]['Participants'][i]['Name'] == name[0]:
            partindex = i
            break
    try:
        if sessioninfo[code]['Participants'][partindex]['Scores'][index]:
            pass
    except KeyError:
        sessioninfo[code]['Participants'][partindex]['Scores'][index] =  {'Entry':'','Score':0}
        

    
def update_ab_pattern(button,code,name):
    index = sessioninfo[code]['Current Index']
    if code:
        for i in range(len(sessioninfo[code]['Participants'])):
            if sessioninfo[code]['Participants'][i]['Name'] == name[0]:
                partindex = i
                break
        pattern = sessioninfo[code]['Participants'][partindex]['Scores'][index]['Entry']
    print(pattern)  
    if button == 'A' and len(pattern) < 5:
        pattern+='A'
        print(pattern)  
        sessioninfo[code]['Participants'][partindex]['Scores'][index]['Entry'] = pattern
        print(sessioninfo[code]['Participants'][partindex]['Scores'][index]['Entry'])  
        return pattern
    elif button == 'B' and len(pattern) < 5:
        pattern+='B'
        print(pattern)  
        sessioninfo[code]['Participants'][partindex]['Scores'][index]['Entry'] = pattern
        print(sessioninfo[code]['Participants'][partindex]['Scores'][index]['Entry'])
        return pattern
    else:
        if sessioninfo[code]['Participants'][partindex]['Scores'][index]['Entry'] == '':
            return 'Tap A/B!'
        else:
            return pattern
               
    


    

