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

quizupsquestions = pd.read_csv('data/Quiz Ups Questions.csv')

sessioninfo = {}

survey_participants = surveyresults['First Name']


workouttypes = [
    'Impostor',
    'Icebreaker',
    'Tug of War',
    'Quiz Ups',
    'Memory Master',
    'Wheel of Fortune'
    ]


def generate_code(size=4, chars = string.ascii_uppercase):
    return ''.join(r.choice(chars) for _ in range(size))

# List of exercises avaliable

exercise = ['Jumping Jacks',
            'Spider Legs',
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
            'Side Plank',
            'High Knees',
            'Jack Knives',
            'Burpees',
            'Flutter Kicks',
            'Press Up into 5 Mountain Climbers',
            'Tricep Extensions',
            'Squat Jump Touches',
            'Alternative Lunges',
            '2 Thrusters into 1 Burpee',
            'Fast Feet - Jump',
            'Left Leg Lower Crunch',
            'Right Leg Lower Crunch',
            '3 Pulsing Squats to Full Squat',
            'Left V-Sit',
            'Right V-Sit',
            'Side Lunge Low Hold',
            'Fast Feet - Chest Down',
            'Half Sit-Up into Full Sit-Up',
            'Sit-Up Glute Raise'
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
    'leaderboard' : {'index' : {17 : {'Exercise': 'Current Leaderboard'},
                                34 : {'Exercise': 'Final Leaderboard'}
                                },
                      'participants' : {}
                      },
    'numinput' : {'index' : {4 : {'Exercise' :exercise[2]},
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
                           7 : {'Exercise': 'Round 1 Done!'},
                           14 : {'Exercise': 'Round 2 Done!'},
                           21 : {'Exercise': 'Round 3 Done!'},
                           23 : {'Exercise': 'Cooldown'}
                                 }
                      },
    'leaderboard' : {'index' : {8 : {'Exercise':'Current Leaderboard'},
                                15 : {'Exercise':'Current Leaderboard'},
                                22 : {'Exercise':'Final Leaderboard'},
                                },
                     'participants' : {}
                     },
    'abcdinput' : {'index' :{4 : {'Exercise' :exercise[9]},
                             5 : {'Exercise' :exercise[16]},
                             6 : {'Exercise' :exercise[17]},
                             11 : {'Exercise' :exercise[9]},
                             12 : {'Exercise' :exercise[16]},
                             13 : {'Exercise' :exercise[17]},
                             18 : {'Exercise' :exercise[9]},
                             19 : {'Exercise' :exercise[16]},
                             20 : {'Exercise' :exercise[17]}
                             }
                   },
    'intenseburst': {'index' : {2 : {'Exercise' :exercise[14]},
                                3 : {'Exercise' :exercise[15]},
                                9 : {'Exercise' :exercise[14]},
                                10 : {'Exercise' :exercise[15]},
                                16 : {'Exercise' :exercise[14]},
                                17 : {'Exercise' :exercise[15]}
                                }
                     }
          }

quizup_structure = {
    'inputs' : {'index' : {0 : {'Exercise': 'Inputs'}
                                            }
                                 },
    'warmup' : {'index' : {1 : {'Exercise': 'Warmup'},
                           6 : {'Exercise': 'Round 1 Done!'},
                           12 : {'Exercise': 'Round 2 Done!'},
                           18 : {'Exercise': 'Round 3 Done!'},
                           20 : {'Exercise': 'Cooldown'}
                                 }
                      },
    'leaderboard' : {'index' : {7 : {'Exercise':'Current Leaderboard'},
                                13 : {'Exercise':'Current Leaderboard'},
                                19 : {'Exercise':'Final Leaderboard'},
                                },
                     'participants' : {}
                     },
    'abcdinput' : {'index' :{2 : {'Exercise' : [exercise[18],exercise[19]]},
                             3 : {'Exercise' : [exercise[20],exercise[21]]},
                             4 : {'Exercise' : [exercise[22],exercise[23]]},
                             5 : {'Exercise' : [exercise[24],exercise[25]]},
                             8 : {'Exercise' : [exercise[18],exercise[3]]},
                             9 : {'Exercise' : [exercise[20],exercise[26]]},
                             10 : {'Exercise' : [exercise[22],exercise[9]]},
                             11 : {'Exercise' : [exercise[27],exercise[28]]},
                             14 : {'Exercise' : [exercise[19],exercise[3]]},
                             15 : {'Exercise' : [exercise[29],exercise[26]]},
                             16 : {'Exercise' : [exercise[30],exercise[9]]},
                             17 : {'Exercise' : [exercise[31],exercise[32]]}
                             }
                   }
    }
                                                 


"""
All Elements/Creation of Elements Below
"""
image = '/assets/newlogowhite.png'

def Navbar():
     navbar = dbc.Navbar([dbc.Col(html.Img(src=image, height="20eh", style ={'margin-top':'5px','margin-bottom':'5px'})),
                          dbc.Button("Quit", href = "https://www.hiitmeupworkout.co.uk/icebreaker",external_link=True, color = 'danger', className="ml-auto",style = {'color':'#FFFFFF','border-radius':'30px','padding':'5px 20px 5px 20px'})
                          ], color = '#0A455A', sticky = 'top',dark = True)

     return navbar

def Navbar2():
     navbar2 = dbc.Navbar([dbc.Col(html.Img(src=image, height="20eh", style ={'margin-top':'5px','margin-bottom':'5px'}))
                          ], color = '#0A455A', sticky = 'top',dark = True)
     return navbar2

"""
Input Screen Components
"""
header0 = html.H4(children = ["Let's do this!"], style = {'textAlign' : "center",'margin-top':'30px','color':'white'})
header00 = html.H6(children = ['Enter the session code and select your name below to join a session:'], style = {'textAlign' : "center",'margin-top':'30px','color':'white'})

header1 = html.H6(children = ['ENTER SESSION CODE:'], style = {'textAlign' : "center",'margin-top':'30px','color':'rgb(10, 79, 105)'})

header2 = html.H4(children = ['Enter Name:'], style = {'textAlign' : "center",'margin-top':'30px'})

cemsg = html.H6(children = ['Code not recognised, please enter a valid workout code'], style = {'textAlign' : 'center','margin-top':'30px','color':'red','padding' : '0px 30px 0px 30px'})

codeinput = dcc.Input(id = 'code-input', type = 'text', placeholder = "ABCD", maxLength = '4', style = {'textAlign' : "center",'font-size': '20px','background-color':'rgb(239, 239, 239)','display':'block','border-radius' : '20px','margin-left':'auto','margin-right':'auto','width':'80%','margin-top':'30px','padding':'15px'})

nameinput = dcc.Dropdown(id = 'name-dropdown', options = [{'label': survey_participants.iloc[i], 'value' : survey_participants.iloc[i]} for i in range(len(survey_participants))], style = {'textAlign':'center','display':'block','font-size': '20px','margin-left':'auto','margin-right':'auto','width':'80%','margin-top':'15px'})

enterbutton = dbc.Button('Join',id = 'enter-button', n_clicks = 0, color = 'info', style = {'textAlign' : "center",'background-color' : 'rgb(10, 79, 105)','border-radius' : '20px', 'display':'block','margin-left':'auto','margin-right':'auto','margin-top':'50px','width':'80%','font-size': '25px', 'touch-action': 'manipulation'})

startbutton = dbc.Button('Start', id = 'start-button',n_clicks=0, color= 'info', style = {'textAlign' : "center", 'display':'block','border-radius' : '20px','background-color' : 'rgb(10, 79, 105)','margin-left':'auto','margin-right':'auto','margin-top':'50px', 'width':'80%','font-size': '25px','touch-action': 'manipulation'})

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
                html.Td('Waiting for Participants',  style={'padding' : '10px'})
                ])], id = 'current-participants'
            )
        ], style = {'textAlign' : "center",'margin-left':'auto','margin-right':'auto', 'margin-top':'30px'})
        return participanttable

def people_joined(code):
    totalpeople = len(sessioninfo[code]['Participants'])
    people_number = html.H6('Current Participants: {}'.format(totalpeople),style = {'textAlign' : "center",'margin-top':'30px'}) 
    return people_number

def TakeSecond(elem):
    return elem[1]

def CreatePosition(scores):
    cur_score = None # Score we're examining
    cur_count = 0 # Number of others that we've seen with this score

    for ix, (name, score) in enumerate(scores):
        if score == cur_score: # Same score for this player as previous
            cur_count += 1
        else: # Different score from before
            cur_score = score
            cur_count = 0
        if ix - cur_count + 1 == 1:
            suf = 'st'
        elif ix - cur_count + 1 == 2:
            suf = 'nd'
        elif ix - cur_count + 1 == 3:
            suf = 'rd'
        else:
            suf = 'th'
        if cur_count > 0:
            scores[ix].append('={}{}'.format(ix - cur_count + 1,suf)) # Add 1 because ix is 0-based
            scores[ix-1].pop(2)
            scores[ix-1].append('={}{}'.format(ix - cur_count + 1,suf))
        else:
            scores[ix].append('{}{}'.format(ix - cur_count + 1,suf))
    return scores

def leader_board(code, name = 'instructor'):
    totalpeople = len(sessioninfo[code]['Participants'])
    
    if totalpeople > 0:
        participants_scores = [[sessioninfo[code]['Participants'][i]['Name'],sessioninfo[code]['Participants'][i]['Total Score']] for i in range(totalpeople)]
        participants_scores.sort(key = TakeSecond,reverse = True)
        participants_scores = CreatePosition(participants_scores)
        if name == 'instructor':
            if totalpeople < 10:
                mainbody = [html.Tr([html.Td(participants_scores[i+1][2],style={'padding-left': '15px', 'padding-right': '15px'}),
                                 html.Td(participants_scores[i+1][0],style={'padding-left': '15px', 'padding-right': '15px'}),
                                 html.Td(participants_scores[i+1][1],style={'padding-left': '15px', 'padding-right': '15px'})
                                 ]) for i in range(totalpeople-1)]
                leader = html.Tr([html.Td('🏆',style={'padding-left': '15px', 'padding-right': '15px','color':'#FFD700'}),
                                 html.Td(participants_scores[0][0],style={'padding-left': '15px', 'padding-right': '15px','color':'#FFD700'}),
                                 html.Td(participants_scores[0][1],style={'padding-left': '15px', 'padding-right': '15px','color':'#FFD700'})
                                 ])
                mainbody.insert(0,leader)
                leaderboard = html.Table(children = [
                    html.Thead(
                        html.Tr([html.Th('Pos', style={'padding-left': '15px', 'padding-right': '15px'}),
                                 html.Th('Name', style={'padding-left': '15px', 'padding-right': '15px'}),
                                 html.Th('Score', style={'padding-left': '15px', 'padding-right': '15px'})
                                 ])
                        ),
                    html.Tbody(children = mainbody, id = 'leaderboard-participants')
                    ], style = {'textAlign' : "center",'margin-left':'auto','margin-right':'auto', 'margin-top':'30px'})
                return leaderboard

            else:
                mainbody = [html.Tr([html.Td(participants_scores[i+1][2],style={'padding-left': '15px', 'padding-right': '15px'}),
                                 html.Td(participants_scores[i+1][0],style={'padding-left': '15px', 'padding-right': '15px'}),
                                 html.Td(participants_scores[i+1][1],style={'padding-left': '15px', 'padding-right': '15px'})
                                 ]) for i in range(9)]
                leader = html.Tr([html.Td('🏆',style={'padding-left': '15px', 'padding-right': '15px','color':'#FFD700'}),
                                 html.Td(participants_scores[0][0],style={'padding-left': '15px', 'padding-right': '15px','color':'#FFD700'}),
                                 html.Td(participants_scores[0][1],style={'padding-left': '15px', 'padding-right': '15px','color':'#FFD700'})
                                 ])
                mainbody.insert(0,leader)
                leaderboard = html.Table(children = [
                    html.Thead(
                        html.Tr([html.Th('Pos', style={'padding-left': '15px', 'padding-right': '15px'}),
                                 html.Th('Name', style={'padding-left': '15px', 'padding-right': '15px'}),
                                 html.Th('Score', style={'padding-left': '15px', 'padding-right': '15px'})
                                 ])
                        ),
                    html.Tbody(children = mainbody, id = 'leaderboard-participants')
                    ], style = {'textAlign' : "center",'margin-left':'auto','margin-right':'auto', 'margin-top':'30px'})
                return leaderboard
        else:
            for i in range(totalpeople):
                if participants_scores[i][0] == name:
                    player = participants_scores[i]
                    break

            if totalpeople < 10:
                mainbody = [html.Tr([html.Td(participants_scores[i+1][2],style={'padding-left': '15px', 'padding-right': '15px'}),
                                 html.Td(participants_scores[i+1][0],style={'padding-left': '15px', 'padding-right': '15px'}),
                                 html.Td(participants_scores[i+1][1],style={'padding-left': '15px', 'padding-right': '15px'})
                                 ]) for i in range(totalpeople-1)]
                leader = html.Tr([html.Td('🏆',style={'padding-left': '15px', 'padding-right': '15px','color':'#FFD700'}),
                                 html.Td(participants_scores[0][0],style={'padding-left': '15px', 'padding-right': '15px','color':'#FFD700'}),
                                 html.Td(participants_scores[0][1],style={'padding-left': '15px', 'padding-right': '15px','color':'#FFD700'})
                                 ])
                playerbody = html.Tr([html.Td(player[2],style={'padding-left': '15px', 'padding-right': '15px'}),
                                 html.Td('You',style={'padding-left': '15px', 'padding-right': '15px'}),
                                 html.Td(player[1],style={'padding-left': '15px', 'padding-right': '15px'})
                                 ])
                mainbody.insert(0,leader)
                mainbody.append(playerbody)
                leaderboard = html.Table(children = [
                    html.Thead(
                        html.Tr([html.Th('Pos', style={'padding-left': '15px', 'padding-right': '15px'}),
                                 html.Th('Name', style={'padding-left': '15px', 'padding-right': '15px'}),
                                 html.Th('Score', style={'padding-left': '15px', 'padding-right': '15px'})
                                 ])
                        ),
                    html.Tbody(children = mainbody, id = 'leaderboard-participants')
                    ], style = {'textAlign' : "center",'margin-left':'auto','margin-right':'auto', 'margin-top':'30px'})
                return leaderboard
            else:
                mainbody = [html.Tr([html.Td(participants_scores[i+1][2],style={'padding-left': '15px', 'padding-right': '15px'}),
                                 html.Td(participants_scores[i+1][0],style={'padding-left': '15px', 'padding-right': '15px'}),
                                 html.Td(participants_scores[i+1][1],style={'padding-left': '15px', 'padding-right': '15px'})
                                 ]) for i in range(9)]
                leader = html.Tr([html.Td('🏆',style={'padding-left': '15px', 'padding-right': '15px','color':'#FFD700'}),
                                 html.Td(participants_scores[0][0],style={'padding-left': '15px', 'padding-right': '15px','color':'#FFD700'}),
                                 html.Td(participants_scores[0][1],style={'padding-left': '15px', 'padding-right': '15px','color':'#FFD700'})
                                 ])
                playerbody = html.Tr([html.Td(player[2],style={'padding-left': '15px', 'padding-right': '15px'}),
                                 html.Td('You',style={'padding-left': '15px', 'padding-right': '15px'}),
                                 html.Td(player[1],style={'padding-left': '15px', 'padding-right': '15px'})
                                 ])
                mainbody.insert(0,leader)
                mainbody.append(playerbody)
                leaderboard = html.Table(children = [
                    html.Thead(
                        html.Tr([html.Th('Pos', style={'padding-left': '15px', 'padding-right': '15px'}),
                                 html.Th('Name', style={'padding-left': '15px', 'padding-right': '15px'}),
                                 html.Th('Score', style={'padding-left': '15px', 'padding-right': '15px'})
                                 ])
                        ),
                    html.Tbody(children = mainbody, id = 'leaderboard-participants')
                    ], style = {'textAlign' : "center",'margin-left':'auto','margin-right':'auto', 'margin-top':'30px'})
                return leaderboard
    else:
        leaderboard = html.Table(children = [
        html.Thead(
            html.Tr(
                html.Th('Leaderboard')
                )
            ),
        html.Tbody(
            children = [html.Tr([
                html.Td('No Participants in Sessions')
                ])], id = 'leaderboard-participants'
            )
        ], style = {'textAlign' : "center",'margin-left':'auto','margin-right':'auto', 'margin-top':'30px'})
        return leaderboard

def initial_live_leaderboard():
    leaderboard = html.Div([
                        html.H6('Leaderboard', style = {'textAlign' : 'center', 'display':'block','margin-top':'0px','margin-left' : 'auto', 'margin-right':'auto'}),
                        html.Table(children = [
                            html.Tbody(children = [
                                html.Tr([
                                    html.Td('Updating...'),
                                    ])
                                ], id = 'live-leaderboard-usr')], style = {'textAlign' : 'center', 'margin-left' : 'auto', 'margin-right':'auto'})]
                            , style = {'position' : 'absolute','bottom' : 0, 'left' : 0, 'right' : 0, 'display':'block', 'padding-bottom' : '10px','padding-top' : '5px' ,'background-color':'#5AC4D8'})
    return leaderboard

def initial_live_instructor_leaderboard():
    leaderboard = html.Div([
                        html.H6('Leaderboard', style = {'textAlign' : 'center', 'display':'block', 'margin-left' : 'auto', 'margin-right':'auto'}),
                        html.Table(children = [
                            html.Tbody(children = [
                                html.Tr([
                                    html.Td('Updating...'),
                                    ])
                                ], id = 'live-leaderboard-ins')], style = {'textAlign' : 'center', 'margin-left' : 'auto', 'margin-right':'auto'})]
                            , style = {'position' : 'absolute','bottom' : 0, 'left' : 0, 'right' : 0, 'display':'block', 'padding-bottom' : '10px','padding-top' : '5px' ,'background-color':'#5AC4D8'})
    return leaderboard

check_participant_interval = dcc.Interval(id = 'check-participants-interval', interval = 2000, n_intervals = 0)

update_exercise_interval = dcc.Interval(id = 'update-exercise-interval', interval = 1000, n_intervals = 0)

submitbutton = dbc.Button('Submit',id = 'submit-button', n_clicks = 0, className="m-auto", style = {'textAlign' : "center", 'display':'block','margin-top':'30px', 'width':'36vw','touch-action': 'manipulation','background-color':'#71CC97','border-color':'#71CC97'})

abutton = dbc.Button('A',id = 'a-button',n_clicks=0, color = 'info', className="ml-auto", style = {'textAlign' : "center", 'display':'block', 'margin-top':'30px', 'width':'36vw', 'height':'16vh', 'font-size':'40px','touch-action': 'manipulation','background-color':'#0A4F69','border-color':'#0A4F69','border-radius':'10%'})

bbutton = dbc.Button('B',id = 'b-button',n_clicks=0, color = 'info', className="mr-auto", style = {'textAlign' : "center", 'display':'block','margin-top':'30px','width':'36vw','height':'16vh','font-size':'40px','touch-action': 'manipulation','background-color':'#0A4F69','border-color':'#0A4F69','border-radius':'10%'})

clearbutton = dbc.Button('Clear',id = 'clear-button',n_clicks=0, className="ml-auto", color = 'danger',style = {'textAlign' : "center", 'display':'block','margin-top':'30px','width':'36vw','touch-action': 'manipulation'})

abutton1 = dbc.Button('A',id = 'a-button-1',n_clicks=0, color = 'danger', style = {'textAlign' : "center", 'display':'block','margin-left':'auto','margin-right':'auto','margin-top':'20px'})

bbutton1 = dbc.Button('B',id = 'b-button-1',n_clicks=0, color = 'primary', style = {'textAlign' : "center", 'display':'block','margin-left':'auto','margin-right':'auto','margin-top':'20px'})

cbutton1 = dbc.Button('C',id = 'c-button-1',n_clicks=0, color = 'warning', style = {'textAlign' : "center", 'display':'block','margin-left':'auto','margin-right':'auto','margin-top':'20px'})

dbutton1 = dbc.Button('D',id = 'd-button-1',n_clicks=0, color = 'success', style = {'textAlign' : "center", 'display':'block','margin-left':'auto','margin-right':'auto','margin-top':'20px'})

numberinput = dcc.Input(id = 'number-input', type = 'number', placeholder = "X", max = '10000', style = {'textAlign' : "center", 'display':'block','margin-left':'auto','margin-right':'auto', 'margin-top':'15px', 'margin-bottom':'30px'})

impostorguess = dcc.Dropdown(id = 'impostor-dropdown', options = [{'label': survey_participants.iloc[i], 'value' : survey_participants.iloc[i]} for i in range(len(survey_participants))], style = {'textAlign':'center','display':'block','margin-left':'auto','margin-right':'auto','width':'80%','margin-top':'15px'})

quitbutton = dbc.Button('Quit',id = 'quit-button', href = "https://www.hiitmeupworkout.co.uk/icebreaker",external_link=True, color = 'danger', style = {'textAlign' : "center",'border-radius' : '20px', 'display':'block','margin-left':'auto','margin-right':'auto','margin-top':'50px','width':'80%','font-size': '25px','touch-action': 'manipulation'})

easybutton = dbc.Button('Easy',id = 'easy-button',n_clicks=0, color = 'success', style = {'textAlign' : "center", 'display':'block','margin-left':'auto','margin-right':'auto','margin-top':'20px','width':'36vw', 'height':'16vh'})

hardbutton = dbc.Button('Hard',id = 'hard-button',n_clicks=0, color = 'danger', style = {'textAlign' : "center", 'display':'block','margin-left':'auto','margin-right':'auto','margin-top':'20px','width':'36vw', 'height':'16vh'})

"""
Main body layout Components
"""

navbar = Navbar()
navbar2 = Navbar2()

leaderboard = initial_live_leaderboard()

insleaderboard = initial_live_instructor_leaderboard()

welcomediv = html.Div(id = 'welcomediv',
                children = [header0,header00],
                style = {'padding':'30px','backgroundColor': 'rgb(43, 169, 193)'})


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

check_submissions_interval = dcc.Interval(id = 'check-submissions-interval', interval = 1000, n_intervals = 0)

update_leaderboard_interval = dcc.Interval(id = 'update-leaderboard-interval', interval = 5000, n_intervals = 0)

instructorname = dcc.Input(id = 'instructor-name-input', type = 'text', placeholder = "Enter Name", maxLength = '10', style = {'textAlign' : "center",'font-size': '20px','background-color':'rgb(239, 239, 239)','display':'block','border-radius' : '20px','margin-left':'auto','margin-right':'auto','width':'80%','margin-top':'30px','padding':'15px','touch-action': 'manipulation'})

impostorselect = dbc.Button('Impostor', id = 'impostor-select',n_clicks=0, color = 'secondary',style = {'textAlign' : "center", 'display':'block','margin-left':'auto','width':'66%','margin-right':'auto','margin-top':'20px','touch-action': 'manipulation'})

icebreakerselect = dbc.Button('Icebreaker', id = 'icebreaker-select',n_clicks=0, color = 'secondary', style = {'textAlign' : "center", 'display':'block','margin-left':'auto','width':'66%','margin-right':'auto','margin-top':'20px','touch-action': 'manipulation'})

tugofwarselect = dbc.Button('Tug of War', id = 'tugofwar-select',n_clicks=0, color = 'secondary', style = {'textAlign' : "center", 'display':'block','margin-left':'auto','width':'66%','margin-right':'auto','margin-top':'20px','touch-action': 'manipulation'})

quizupselect = dbc.Button('Quiz Ups', id = 'quizup-select',n_clicks=0, color = 'success', style = {'textAlign' : "center", 'display':'block','margin-left':'auto','width':'66%','margin-right':'auto','margin-top':'20px','touch-action': 'manipulation'})

memoryselect = dbc.Button('Memory Master', id = 'memory-select',n_clicks=0, color = 'secondary', style = {'textAlign' : "center", 'display':'block','margin-left':'auto','width':'66%','margin-right':'auto','margin-top':'20px','touch-action': 'manipulation'})

fortuneselect = dbc.Button('Wheel of Fortune', id = 'fortune-select',n_clicks=0, color = 'secondary', style = {'textAlign' : "center", 'display':'block','margin-left':'auto','width':'66%','margin-right':'auto','margin-top':'20px','touch-action': 'manipulation'})

nemsg = html.H6(children = ['Please enter your name'], style = {'textAlign' : 'center','margin-top':'30px','color':'red'})

moveonbutton_re = dbc.Button('Rest 😎', id = 'moveon-button-to-rest',n_clicks=0, color= 'info', style = {'textAlign' : "center",'background-color' : 'rgb(10, 79, 105)','border-radius' : '20px', 'display':'block','margin-left':'auto','margin-right':'auto','margin-top':'50px','width':'80%','font-size': '25px','touch-action': 'manipulation'})

moveonbutton_ex = dbc.Button('Next Exercise', id = 'moveon-button-to-exercise',n_clicks=0, color= 'info', style = {'textAlign' : "center",'background-color' : 'rgb(10, 79, 105)','border-radius' : '20px', 'display':'block','margin-left':'auto','margin-right':'auto','margin-top':'50px','width':'80%','font-size': '25px','touch-action': 'manipulation'})

hidden_moveonbutton_ex = dbc.Button(id = 'moveon-button-to-exercise', style = {'display':'none'})

hidden_moveonbutton_re = dbc.Button(id = 'moveon-button-to-rest', style = {'display':'none'})

"""
Main body layout components - instructor
"""

headerdiv2 = html.Div(id = 'header-div-2',
                children = [header3]
                )
maindiv2 = html.Div(id = 'main-div-2',
                children = [instructorname,header4,impostorselect,icebreakerselect,tugofwarselect,quizupselect,memoryselect,fortuneselect]
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
                    dbc.Col([welcomediv,
                             headerdiv,
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
    layout = [navbar2,
                dbc.Row([
                    dbc.Col([headerdiv1,
                             maindiv1,
                             scorediv
                             ])
                    ]),
                leaderboard
              ]
    return layout

def InstructorWorkout():
    layout = [navbar2,
                dbc.Row([
                    dbc.Col([headerdiv3,
                             maindiv3,
                             scorediv3
                             ])
                    ]),
                insleaderboard
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
            main = [instructorname,nemsg,header4,impostorselect,icebreakerselect,tugofwarselect,quizupselect,memoryselect,fortuneselect]
            score = []
            hidden = []
            return header, main, score, hidden
    else:
        header = [header3]
        main = [instructorname,header4,impostorselect,icebreakerselect,tugofwarselect,quizupselect,memoryselect,fortuneselect]
        score = []
        hidden = []
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
        
        elif sessioninfo[code]['Workout Type'] == 'Quiz Ups':
            structure = quizup_structure
            session_users = finalize_participants(code,structure)
            generate_quizups(structure)
            sessioninfo[code]['Structure'] = structure
        
def finalize_participants(code,structure):
    if code:
        sessionparticipants = []
        for i in range(len(sessioninfo[code]['Participants'])):

            structure['leaderboard']['participants'][i] = sessioninfo[code]['Participants'][i]['Name']
            sessionparticipants.append(sessioninfo[code]['Participants'][i]['Name'])

        return sessionparticipants

def generate_ab_patterns(structure, size = 7, chars = 'AB'):
    try:
        for i in structure['abinput']['index'].keys():
            target = 'Pattern'
            answer = ''.join(r.choice(chars) for _ in range(size))
            structure['abinput']['index'][i]['Target'] = target
            structure['abinput']['index'][i]['Answer'] = answer
    except:
        pass

def generate_questions(structure,session_users):
    headers = surveyresults.columns.tolist()
    for i in structure['abcdinput']['index'].keys():
        targetqs = [8,9,11]
        target = headers[r.choice(targetqs)]
        possibleoptions = surveyresults[target].unique()

        targetindex = r.randint(0,len(surveyresults)-1)
        targetplayer = surveyresults.loc[targetindex,'First Name']

        while targetplayer not in session_users:
             targetindex = r.randint(0,len(surveyresults)-1)
             targetplayer = surveyresults.loc[targetindex,'First Name']

        correct = surveyresults.loc[targetindex,target]

        while len(possibleoptions) == 1:
            target = headers[r.choice(targetqs)]
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

def generate_quizups(structure):
    questions = []
    trivia = pd.DataFrame(quizupsquestions.loc[quizupsquestions['Type'] == 'Trivia',:]).reset_index(drop=True)
    nearest = pd.DataFrame(quizupsquestions.loc[quizupsquestions['Type'] == 'NearestTo',:]).reset_index(drop=True)
    easy = pd.DataFrame(trivia.loc[trivia['Difficulty'] == 'Easy',:]).reset_index(drop=True)
    hard = pd.DataFrame(trivia.loc[trivia['Difficulty'] == 'Hard',:]).reset_index(drop=True)
    count = 0
    
    for i in structure['abcdinput']['index'].keys():
        if count < 3:
            e = easy.loc[r.randint(0,len(easy)-1)]
            eq = e['Question']
            while eq in questions:
                e = easy.loc[r.randint(0,len(easy)-1)]
                eq = e['Question']
            h = hard.loc[r.randint(0,len(hard)-1)]
            hq = h['Question']
            while hq in questions:
                h = hard.loc[r.randint(0,len(hard)-1)]
                hq = h['Question']
            questions.append(e['Question'])
            questions.append(h['Question'])
            qtype = 'Trivia'
            target = [e['Question'],h['Question']]
            eABCD = ['A','B','C','D']
            hABCD = ['A','B','C','D']
            elocation = eABCD.pop(r.randint(0,len(eABCD)-1))
            hlocation = hABCD.pop(r.randint(0,len(hABCD)-1))
            ecorrect = e['Answer']
            eposs = eval(e['Options'])
            hcorrect = h['Answer']
            hposs = eval(h['Options'])
            eanswer = {elocation : ecorrect}
            hanswer = {hlocation : hcorrect}
            eoptions = {}
            hoptions = {}
            eoptions[elocation] = ecorrect
            hoptions[hlocation] = hcorrect
            
            while len(eoptions) < 4:
                toadd = eposs[r.randint(0,len(eposs)-1)]
                while toadd in eoptions.values():
                    toadd = eposs[r.randint(0,len(eposs)-1)]
                location1 = eABCD.pop(r.randint(0,len(eABCD)-1))
                eoptions[location1] = toadd
            
            while len(hoptions) < 4:
                toadd1 = hposs[r.randint(0,len(hposs)-1)]
                while toadd1 in hoptions.values():
                    toadd1 = hposs[r.randint(0,len(hposs)-1)]
                location2 = hABCD.pop(r.randint(0,len(hABCD)-1))
                hoptions[location2] = toadd1
            
            answer = [eanswer,hanswer]
            options = [eoptions,hoptions]
            
            structure['abcdinput']['index'][i]['QType'] = qtype
            structure['abcdinput']['index'][i]['Target'] = target
            structure['abcdinput']['index'][i]['Answer'] = answer
            structure['abcdinput']['index'][i]['Options'] = options
            
            count += 1
            
        else:
            n = nearest.loc[r.randint(0,len(nearest)-1)]
            nq = n['Question']
            while nq in questions:
                n = nearest.loc[r.randint(0,len(nearest)-1)]
                nq = n['Question']
            questions.append(n['Question'])
            qtype = 'NearestTo'
            target = n['Question']
            answer = n['Answer']
            options = n['Options']
            
            structure['abcdinput']['index'][i]['QType'] = qtype
            structure['abcdinput']['index'][i]['Target'] = target
            structure['abcdinput']['index'][i]['Answer'] = answer
            structure['abcdinput']['index'][i]['Options'] = options
            count = 0
    
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
        if structure['warmup']['index'][index]['Exercise']:
            if structure['warmup']['index'][index]['Exercise'] == 'Cooldown':
                mainlayout = [quitbutton]
            else:
                mainlayout = [moveonbutton_ex,hidden_moveonbutton_re]
        scorelayout = []

    elif screentype == 'leaderboard':
        leaderboard = leader_board(code)
        headerlayout = [html.H6(children = [structure['leaderboard']['index'][index]['Exercise']], style = {'textAlign' : "center",'margin-top':'30px'})]
        mainlayout = [leaderboard,moveonbutton_ex,hidden_moveonbutton_re]
        scorelayout = []

    elif screentype == 'numinput':
        if newstate == 'Exercise':
            headerlayout = [html.H4(children = [exercisetype], style = {'textAlign' : "center",'margin-top':'30px'})]
            mainlayout = [numberinput,moveonbutton_re,hidden_moveonbutton_ex]
            scorelayout = []
        elif newstate == 'Rest':
            headerlayout = [html.H4(children = [exercisetype], style = {'textAlign' : "center",'margin-top':'30px'})]
            mainlayout = [numberinput,moveonbutton_ex,hidden_moveonbutton_re,check_submissions_interval]
            scorelayout = []

    elif screentype == 'abinput':
        target = structure['abinput']['index'][index]['Target']
        answer = structure['abinput']['index'][index]['Answer']
        if newstate == 'Exercise':
            headerlayout = [html.H6(children = ['ABB Challenge'], style = {'textAlign' : "center",'margin-top':'0px','margin-bottom':'0px','background-color':'#5AC4D8','padding':'30px'}),
                        html.H4(children = [exercisetype], style = {'textAlign' : "center",'margin-top':'0px','color':'#71CC97','padding':'30px', 'color':'#71CC97','font-size':'30px'}),
                        ]
            mainlayout = [html.H6(children = [target], style = {'textAlign' : "center",'margin-top':'30px'}),
                      html.H4(children = [answer], style = {'textAlign' : "center",'margin-top':'30px','font-size':'25px','color':'#0A4F69'}),
                      moveonbutton_re,hidden_moveonbutton_ex]
            scorelayout = []
        elif newstate == 'Rest':
            headerlayout = [html.H6(children = ['ABB Challenge'], style = {'textAlign' : "center",'margin-top':'30px',}),
                        html.H4(children = ['Rest 😎'], style = {'textAlign' : "center",'margin-top':'30px','color':'#5AC4D8','font-size':'30px'}),
                        ]
            mainlayout = [html.H6(children = [target], style = {'textAlign' : "center",'margin-top':'30px'}),
                      html.H4(children = [answer], style = {'textAlign' : "center",'margin-top':'30px'}),
                      html.H6(id = 'total-answers', children = [check_total_answers(code)], style = {'textAlign' : "center",'margin-top':'30px'}),
                      moveonbutton_ex, hidden_moveonbutton_re,check_submissions_interval]
            scorelayout = []

    elif screentype == 'abcdinput':
        try:
            qtype = structure['abcdinput']['index'][index]['QType']
        except KeyError:
            target = structure['abcdinput']['index'][index]['Target']
            targetplayer = structure['abcdinput']['index'][index]['Target Player']
            answer = structure['abcdinput']['index'][index]['Answer']
    #        options = structure['abcdinput']['index'][index]['Options']
            a = list(answer.values())
            if newstate == 'Exercise':
                headerlayout = [html.H6(children = ['Quiz Ups'], style = {'textAlign' : "center",'margin-top':'30px'}),
                                html.H4(children = [exercisetype[0]], style = {'textAlign' : "center",'margin-top':'30px', 'color':'#71CC97','font-size':'30px'}),
                                html.H4(children = [exercisetype[1]], style = {'textAlign' : "center",'margin-top':'10px', 'color':'#71CC97','font-size':'30px'}),
                                html.H6(children = [target], style = {'textAlign' : "center",'margin-top':'30px'}),
                                html.H4(children = [targetplayer], style = {'textAlign' : "center",'margin-top':'30px'}),
                                html.H6(children = ['Answer: ',a[0]], style = {'textAlign' : "center",'margin-top':'30px'})]
                mainlayout = [moveonbutton_re, hidden_moveonbutton_ex]
                scorelayout = []
            elif newstate == 'Rest':
                headerlayout = [html.H6(children = ['Quiz Ups'], style = {'textAlign' : "center",'margin-top':'30px'}),
                                html.H4(children = ['Rest 😎'], style = {'textAlign' : "center",'margin-top':'30px','color':'#5AC4D8','font-size':'30px'}),
                                html.H6(children = [target], style = {'textAlign' : "center",'margin-top':'30px'}),
                                html.H4(children = [targetplayer], style = {'textAlign' : "center",'margin-top':'30px'}),
                                html.H6(children = ['Answer: ',a[0]], style = {'textAlign' : "center",'margin-top':'30px'}),
                                html.H6(id = 'total-answers', children = [check_total_answers(code)], style = {'textAlign' : "center",'margin-top':'30px'})]
                mainlayout = [moveonbutton_ex, hidden_moveonbutton_re,check_submissions_interval]
                scorelayout = []
        else:
            if qtype == 'Trivia':
                etarget = structure['abcdinput']['index'][index]['Target'][0]
                htarget = structure['abcdinput']['index'][index]['Target'][1]
                eanswer = structure['abcdinput']['index'][index]['Answer'][0]
                hanswer = structure['abcdinput']['index'][index]['Answer'][1]
                ea = list(eanswer.values())
                ha = list(hanswer.values())
                
                if newstate == 'Exercise':
                    headerlayout = [html.H6(children = ['Quiz Ups'], style = {'textAlign' : "center",'margin-top':'30px'}),
                                    html.H4(children = [exercisetype[0]], style = {'textAlign' : "center",'margin-top':'30px', 'color':'#71CC97','font-size':'30px'}),
                                    html.H4(children = [exercisetype[1]], style = {'textAlign' : "center",'margin-top':'10px', 'color':'#71CC97','font-size':'30px'}),
                                    html.H6(children = ['Easy: ',etarget], style = {'textAlign' : "center",'margin-top':'30px'}),
                                    html.H6(children = ['Answer: ',ea[0]], style = {'textAlign' : "center",'margin-top':'10px'}),
                                    html.H6(children = ['Hard: ',htarget], style = {'textAlign' : "center",'margin-top':'30px'}),
                                    html.H6(children = ['Answer: ',ha[0]], style = {'textAlign' : "center",'margin-top':'10px'})]
                    mainlayout = [moveonbutton_re, hidden_moveonbutton_ex]
                    scorelayout = []
                elif newstate == 'Rest':
                    headerlayout = [html.H6(children = ['Quiz Ups'], style = {'textAlign' : "center",'margin-top':'30px'}),
                                    html.H4(children = ['Rest 😎'], style = {'textAlign' : "center",'margin-top':'30px','color':'#5AC4D8','font-size':'30px'}),
                                    html.H6(children = ['Easy: ',etarget], style = {'textAlign' : "center",'margin-top':'30px'}),
                                    html.H6(children = ['Answer: ',ea[0]], style = {'textAlign' : "center",'margin-top':'10px'}),
                                    html.H6(children = ['Hard: ',htarget], style = {'textAlign' : "center",'margin-top':'30px'}),
                                    html.H6(children = ['Answer: ',ha[0]], style = {'textAlign' : "center",'margin-top':'10px'}),
                                    html.H6(id = 'total-answers', children = [check_total_answers(code)], style = {'textAlign' : "center",'margin-top':'30px'})]
                    mainlayout = [moveonbutton_ex, hidden_moveonbutton_re, check_submissions_interval]
                    scorelayout = []
            else:
                target = structure['abcdinput']['index'][index]['Target']
                answer = structure['abcdinput']['index'][index]['Answer']
                if newstate == 'Exercise':
                    headerlayout = [html.H6(children = ['Quiz Ups'], style = {'textAlign' : "center",'margin-top':'30px'}),
                                    html.H4(children = [exercisetype[0]], style = {'textAlign' : "center",'margin-top':'30px', 'color':'#71CC97','font-size':'30px'}),
                                    html.H4(children = [exercisetype[1]], style = {'textAlign' : "center",'margin-top':'10px', 'color':'#71CC97','font-size':'30px'}),
                                    html.H6(children = [target], style = {'textAlign' : "center",'margin-top':'30px'}),
                                    html.H6(children = ['Answer: ',answer], style = {'textAlign' : "center",'margin-top':'30px'})]
                    mainlayout = [moveonbutton_re, hidden_moveonbutton_ex]
                    scorelayout = []
                elif newstate == 'Rest':
                    headerlayout = [html.H6(children = ['Quiz Ups'], style = {'textAlign' : "center",'margin-top':'30px'}),
                                    html.H4(children = ['Rest 😎'], style = {'textAlign' : "center",'margin-top':'30px','color':'#5AC4D8','font-size':'30px'}),
                                    html.H6(children = [target], style = {'textAlign' : "center",'margin-top':'30px'}),
                                    html.H6(children = ['Answer: ',answer], style = {'textAlign' : "center",'margin-top':'30px'}),
                                    html.H6(id = 'total-answers', children = [check_total_answers(code)], style = {'textAlign' : "center",'margin-top':'30px'})]
                    mainlayout = [moveonbutton_ex, hidden_moveonbutton_re, check_submissions_interval]
                    scorelayout = []
            
            
    elif screentype == 'impostorinput':
        headerlayout = [html.H4(children = [exercisetype], style = {'textAlign' : "center",'margin-top':'30px'}),
                        html.H6(id = 'total-answers', children = [check_total_answers(code)], style = {'textAlign' : "center",'margin-top':'30px'})]
        mainlayout = [impostorguess,moveonbutton_ex,hidden_moveonbutton_re,check_submissions_interval]
        scorelayout = []

    elif screentype == 'intenseburst':
        if newstate == 'Exercise':
            headerlayout = [html.H6(children = ['Intense Burst 💪'], style = {'textAlign' : "center",'margin-top':'30px'}),
                            html.H4(children = [exercisetype], style = {'textAlign' : "center",'margin-top':'30px', 'color':'#71CC97','font-size':'30px'}),]
            mainlayout = [moveonbutton_re,hidden_moveonbutton_ex]
            scorelayout = []
        if newstate == 'Rest':
            headerlayout = [html.H6(children = ['Intense Burst 💪'], style = {'textAlign' : "center",'margin-top':'30px'}),
                            html.H4(children = ['Rest 😎'], style = {'textAlign' : "center",'margin-top':'30px','color':'#5AC4D8','font-size':'30px'})]
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
    for i in range(len(sessioninfo[code]['Participants'])):
        if sessioninfo[code]['Participants'][i]['Name'] == name:
            partindex = i
            break

    people_number = people_joined(code)
    if screentype == 'inputs':
        headerlayout = headerlayout = [html.H6(children = ["Today's Instructor:"], style = {'textAlign' : "center",'margin-top':'0px','margin-bottom':'0px','background-color' : "#0A4F69",'color' : "#FFFFFF",'padding':'30px 0px 0px 0px'}),
                      html.H4(children = [sessioninfo[code]['Instructor']], style = {'textAlign' : "center",'margin-top':'0px','margin-bottom':'0px','background-color' : "#0A4F69",'color' : "#FFFFFF",'padding':'0px 0px 30px 0px'}),
                      html.H6(children = ["Today's Session:"], style = {'textAlign' : "center",'margin-top':'0px','margin-bottom':'0px','background-color' : "#5AC4D8",'padding':'30px 0px 0px 0px'}),
                      html.H4(children = [sessioninfo[code]['Workout Type']], style = {'textAlign' : "center",'margin-top':'0px','margin-bottom':'0px','background-color' : "#5AC4D8",'padding':'0px 0px 30px 0px'}),
                      html.H6(children = ["Waiting for {} to start the session...".format(sessioninfo[code]['Instructor'])], style = {'textAlign' : "center",'margin-top':'0px','margin-bottom':'0px','background-color' : "#0A4F69",'color' : "#FFFFFF",'padding':'15px 0px 15px 0px'})]
        mainlayout = [people_number,update_exercise_interval]
        scorelayout = []

    elif screentype == 'warmup':
        headerlayout = Warmcool(index,structure)
        if structure['warmup']['index'][index]['Exercise']:
            if structure['warmup']['index'][index]['Exercise'] == 'Cooldown':
                mainlayout = [quitbutton]
            else:
                mainlayout = [update_exercise_interval]
        scorelayout = []

    elif screentype == 'leaderboard':
        leaderboard = leader_board(code, name)
        headerlayout = [html.H6(children = [structure['leaderboard']['index'][index]['Exercise']], style = {'textAlign' : "center",'margin-top':'0px','margin-bottom':'0px','background-color':'#FFD700','padding':'15px'})]
        mainlayout = [update_exercise_interval, leaderboard]
        scorelayout = []

    elif screentype == 'numinput':
        create_score_entry(code,name)
        if state == 'Exercise':
            headerlayout = [html.H4(children = [exercisetype], style = {'textAlign' : "center",'margin-top':'0px','margin-bottom':'0px','background-color':'#5AC4D8','padding':'30px'})]
            mainlayout = [update_exercise_interval, numberinput]
            scorelayout = []
        elif state == 'Rest':
            if sessioninfo[code]['Participants'][partindex]['Scores'][index]['Answered'] == 1 and sessioninfo[code]['Participants'][partindex]['Scores'][index]['Score'] > 0:
                headerlayout = [html.H4(children = ['Rest 😎'], style = {'textAlign' : "center",'margin-top':'30px','color':'#5AC4D8','font-size':'30px'}),
                                html.H4(children = ['Correct :)'], style = {'textAlign' : "center",'margin-top':'30px','color':'#71CC97'}),
                                html.H6(children = ['Current Score: {}'.format(sessioninfo[code]['Participants'][partindex]['Total Score'])], style = {'textAlign' : "center",'margin-top':'30px'})]
                mainlayout = [update_exercise_interval]
                scorelayout = []
            elif sessioninfo[code]['Participants'][partindex]['Scores'][index]['Answered'] == 1 and sessioninfo[code]['Participants'][partindex]['Scores'][index]['Score'] == 0:
                headerlayout = [html.H4(children = ['Rest 😎'], style = {'textAlign' : "center",'margin-top':'30px','color':'#5AC4D8','font-size':'30px'}),
                                html.H4(children = ['Incorrect :('], style = {'textAlign' : "center",'margin-top':'30px','color':'#FF3830'})]
                mainlayout = [update_exercise_interval]
                scorelayout = []
            else:
                headerlayout = [html.H4(children = ['Rest 😎'], style = {'textAlign' : "center",'margin-top':'30px','color':'#5AC4D8','font-size':'30px'}),
                                html.H4(children = ['Enter your number below:'], style = {'textAlign' : "center",'margin-top':'30px'})]
                mainlayout = [update_exercise_interval, numberinput]
                scorelayout = [html.Div(id = 'score', style = {'display':'none'})]

    elif screentype == 'abinput':
        create_score_entry(code,name)
        target = structure['abinput']['index'][index]['Target']
        answer = structure['abinput']['index'][index]['Answer']
        if state == 'Exercise':
            headerlayout = [html.H6(children = ['ABB Challenge'], style = {'textAlign' : "center",'margin-top':'0px','margin-bottom':'0px','background-color':'#5AC4D8','padding':'15px'}),
                            html.H4(children = [exercisetype], style = {'textAlign' : "center",'padding-top':'50%','margin-bottom':'0px','padding-bottom':'75%','color':'#FFFFFF','background-color':'#71CC97','font-size':'35px'})
                            ]
            mainlayout = [update_exercise_interval]
            scorelayout = []
        elif state == 'Rest':
            if sessioninfo[code]['Participants'][partindex]['Scores'][index]['Answered'] == 1 and sessioninfo[code]['Participants'][partindex]['Scores'][index]['Score'] > 0:
                headerlayout = [html.H6(children = ['ABB Challenge'], style = {'textAlign' : "center",'margin-top':'0px','background-color':'#5AC4D8','padding':'15px'}),
                                html.H4(children = ['Rest 😎'], style = {'textAlign' : "center",'margin-top':'30px','color':'#5AC4D8','font-size':'30px'}),
                                html.H4(children = ['✅ +50!'], style = {'textAlign' : "center",'margin-top':'30px','font-size':'40px','color':'##71CC97'}),
                                html.H6(children = ['The answer was: ', answer], style = {'textAlign' : "center",'margin-top':'30px'}),
                                html.H6(children = ['Current Score: {}'.format(sessioninfo[code]['Participants'][partindex]['Total Score'])], style = {'textAlign' : "center",'margin-top':'30px'})
                                ]
                mainlayout = [update_exercise_interval]
                scorelayout = []

            elif sessioninfo[code]['Participants'][partindex]['Scores'][index]['Answered'] == 1 and sessioninfo[code]['Participants'][partindex]['Scores'][index]['Score'] == 0:
                headerlayout = [html.H6(children = ['ABB Challenge'], style = {'textAlign' : "center",'margin-top':'0px','background-color':'#5AC4D8','padding':'15px'}),
                                html.H4(children = ['Rest 😎'], style = {'textAlign' : "center",'margin-top':'30px','color':'#5AC4D8','font-size':'30px'}),
                                html.H4(children = ['❌'], style = {'textAlign' : "center",'margin-top':'30px','font-size':'40px'}),
                                html.H6(children = ['The correct answer was: ', answer], style = {'textAlign' : "center",'margin-top':'30px'}),
                                html.H6(children = ['Current Score: {}'.format(sessioninfo[code]['Participants'][partindex]['Total Score'])], style = {'textAlign' : "center",'margin-top':'30px'})
                                ]
                mainlayout = [update_exercise_interval]
                scorelayout = []

            else:
                headerlayout = [html.H6(children = ['ABB Challenge'], style = {'textAlign' : "center",'margin-top':'0px','background-color':'#5AC4D8','padding':'15px'}),
                                html.H4(children = ['Rest 😎'], style = {'textAlign' : "center",'margin-top':'30px','color':'#5AC4D8','font-size':'30px'}),
                                ]
                mainlayout = [html.H6(children = [target], style = {'textAlign' : "center",'margin-top':'30px'}),
                              html.H4(id = 'show-user-pattern', children = [update_ab_pattern(0,code,name)], style = {'textAlign' : "center",'margin-top':'30px'}),
                              dbc.Row([dbc.Col([abutton,clearbutton]),dbc.Col([bbutton,submitbutton])]),update_exercise_interval]
                scorelayout = [html.Div(id = 'score', style = {'display':'none'})]

    elif screentype == 'abcdinput':
        try:
            qtype = structure['abcdinput']['index'][index]['QType']
        except KeyError:
            create_score_entry(code,name)
            target = structure['abcdinput']['index'][index]['Target']
            targetplayer = structure['abcdinput']['index'][index]['Target Player']
            options = structure['abcdinput']['index'][index]['Options']
            if state == 'Exercise':
                headerlayout = [html.H6(children = ['Quiz Ups'], style = {'textAlign' : "center",'margin-top':'0px','margin-bottom':'0px','background-color':'#5AC4D8','padding':'15px'}),
                                html.Div(children = [html.H6(children = ['30 Secs'], style = {'textAlign' : "center",'margin-bottom':'0px','color':'#FFFFFF','font-size':'20px'}),
                                         html.H4(children = [exercisetype[0]], style = {'textAlign' : "center",'margin-bottom':'10px','color':'#FFFFFF','font-size':'35px'}),
                                         html.H6(children = ['30 Secs'], style = {'textAlign' : "center",'margin-bottom':'0px','color':'#FFFFFF','font-size':'20px'}),
                                         html.H4(children = [exercisetype[1]], style = {'textAlign' : "center",'color':'#FFFFFF','font-size':'35px'})], style = {'padding-top':'35%','padding-bottom':'75%','margin-bottom':'0px','background-color':'#71CC97','font-size':'35px'})
                                ]
                mainlayout = [update_exercise_interval]
                scorelayout = []
    
            elif state == 'Rest':
                if sessioninfo[code]['Participants'][partindex]['Scores'][index]['Answered'] == 1 and sessioninfo[code]['Participants'][partindex]['Scores'][index]['Score'] > 0:
                    headerlayout = [html.H6(children = ['Quiz Ups'], style = {'textAlign' : "center",'margin-top':'0px','margin-bottom':'0px','background-color':'#5AC4D8','padding':'15px'}),
                                    html.H4(children = ['Rest 😎'], style = {'textAlign' : "center",'margin-top':'30px','color':'#5AC4D8','font-size':'30px'}),
                                    html.H4(children = ['✅ +100!'], style = {'textAlign' : "center",'margin-top':'30px','font-size':'40px'}),
                                    html.H6(children = [targetplayer, ' answered: ', [*structure['abcdinput']['index'][index]['Answer'].values()][0]], style = {'textAlign' : "center",'margin-top':'30px','padding':'0px 10px 0px 10px'}),
                                    html.H6(children = ['Current Score: {}'.format(sessioninfo[code]['Participants'][partindex]['Total Score'])], style = {'textAlign' : "center",'margin-top':'30px'})]
                    mainlayout = [update_exercise_interval]
                    scorelayout = []
                elif sessioninfo[code]['Participants'][partindex]['Scores'][index]['Answered'] == 1 and sessioninfo[code]['Participants'][partindex]['Scores'][index]['Score'] == 0:
                    headerlayout = [html.H6(children = ['Quiz Ups'], style = {'textAlign' : "center",'margin-top':'0px','margin-bottom':'0px','background-color':'#5AC4D8','padding':'15px'}),
                                    html.H4(children = ['Rest 😎'], style = {'textAlign' : "center",'margin-top':'30px','color':'#5AC4D8','font-size':'30px'}),
                                    html.H4(children = ['❌'], style = {'textAlign' : "center",'margin-top':'30px','font-size':'40px'}),
                                    html.H6(children = [targetplayer, ' answered: ', [*structure['abcdinput']['index'][index]['Answer'].values()][0]], style = {'textAlign' : "center",'margin-top':'30px', 'padding':'0px 10px 0px 10px'}),
                                    html.H6(children = ['Current Score: {}'.format(sessioninfo[code]['Participants'][partindex]['Total Score'])], style = {'textAlign' : "center",'margin-top':'30px'})]
                    mainlayout = [update_exercise_interval]
                    scorelayout = []
                else:
                    headerlayout = [html.H6(children = ['Quiz Ups'], style = {'textAlign' : "center",'margin-top':'0px','margin-bottom':'0px','background-color':'#5AC4D8','padding':'15px'}),
                                    html.H4(children = ['Rest 😎'], style = {'textAlign' : "center",'margin-top':'30px','color':'#5AC4D8','font-size':'30px'}),
                                    html.H6(children = [target], style = {'textAlign' : "center",'margin-top':'30px','padding':'0px 10px 0px 10px'}),
                                    html.H6(children = ['What did ', targetplayer, ' answer?'], style = {'textAlign' : "center",'margin-top':'30px'})]
                    if len(options) == 2:
                        mainlayout = [dbc.Button(options['A'],id = 'a-button-1',n_clicks=0, color = 'danger', style = {'textAlign' : "center", 'display':'block','margin-left':'auto','margin-right':'auto', 'margin-top':'20px', 'width':'45vw', 'height':'10vh','touch-action': 'manipulation'}),
                                      dbc.Button(options['B'],id = 'b-button-1',n_clicks=0, color = 'primary', style = {'textAlign' : "center", 'display':'block','margin-left':'auto','margin-right':'auto', 'margin-top':'20px', 'width':'45vw', 'height':'10vh','touch-action': 'manipulation'}),
                                      dbc.Button(id = 'c-button-1',n_clicks=0, style = {'display' : 'none'}),
                                      dbc.Button(id = 'd-button-1',n_clicks=0, style = {'display' : 'none'}),
                                      update_exercise_interval]
                    elif len(options) == 3:
                        mainlayout = [dbc.Row([dbc.Col([dbc.Button(options['A'],id = 'a-button-1',n_clicks=0, color = 'danger', className="mr-auto", style = {'textAlign' : "center", 'display':'block','margin-left':'auto','margin-right':'auto', 'margin-top':'20px', 'width':'40vw', 'height':'10vh','touch-action': 'manipulation'}),
                                      dbc.Button(options['B'],id = 'b-button-1',n_clicks=0, color = 'primary', className="mr-auto", style = {'textAlign' : "center", 'display':'block','margin-left':'auto','margin-right':'auto', 'margin-top':'20px', 'width':'40vw', 'height':'10vh','touch-action': 'manipulation'})
                                      ]),
                                      dbc.Col([dbc.Button(options['C'],id = 'c-button-1',n_clicks=0, color = 'warning', className="ml-auto", style = {'textAlign' : "center", 'display':'block','margin-left':'auto','margin-right':'auto', 'margin-top':'20px', 'width':'40vw', 'height':'10vh','touch-action': 'manipulation'}),
                                      dbc.Button(id = 'd-button-1',n_clicks=0, style = {'display':'none'})
                                      ])]),
                                      update_exercise_interval]
                    elif len(options) == 4:
                        mainlayout = [dbc.Row([dbc.Col([dbc.Button(options['A'],id = 'a-button-1',n_clicks=0, color = 'danger', className="mr-auto", style = {'textAlign' : "center", 'display':'block','margin-left':'auto','margin-right':'10px', 'margin-top':'20px', 'width':'40vw', 'height':'10vh','touch-action': 'manipulation'}),
                                      dbc.Button(options['B'],id = 'b-button-1',n_clicks=0, color = 'primary', className="mr-auto", style = {'textAlign' : "center", 'display':'block','margin-left':'auto','margin-right':'10px', 'margin-top':'20px', 'width':'40vw', 'height':'10vh','touch-action': 'manipulation'})
                                      ]),
                                      dbc.Col([dbc.Button(options['C'],id = 'c-button-1',n_clicks=0, color = 'warning', className="ml-auto", style = {'textAlign' : "center", 'display':'block','margin-left':'10px','margin-right':'auto', 'margin-top':'20px', 'width':'40vw', 'height':'10vh','touch-action': 'manipulation'}),
                                      dbc.Button(options['D'],id = 'd-button-1',n_clicks=0, color = 'success', className="ml-auto", style = {'textAlign' : "center", 'display':'block','margin-left':'10px','margin-right':'auto', 'margin-top':'20px', 'width':'40vw', 'height':'10vh','touch-action': 'manipulation'})
                                      ])]),
                                      update_exercise_interval]
                    else:
                        mainlayout = [update_exercise_interval]
                    scorelayout = [html.Div(id = 'score-abcd', style = {'display':'none'})]
                    
        else:
            create_score_entry(code,name)
            if qtype == 'Trivia':
                if state == 'Exercise':
                    headerlayout = [html.H6(children = ['Quiz Ups'], style = {'textAlign' : "center",'margin-top':'0px','margin-bottom':'0px','background-color':'#5AC4D8','padding':'15px'}),
                                    html.Div(children = [html.H6(children = ['30 Secs'], style = {'textAlign' : "center",'margin-bottom':'0px','color':'#FFFFFF','font-size':'20px'}),
                                             html.H4(children = [exercisetype[0]], style = {'textAlign' : "center",'margin-bottom':'10px','color':'#FFFFFF','font-size':'35px'}),
                                             html.H6(children = ['30 Secs'], style = {'textAlign' : "center",'margin-bottom':'0px','color':'#FFFFFF','font-size':'20px'}),
                                             html.H4(children = [exercisetype[1]], style = {'textAlign' : "center",'color':'#FFFFFF','font-size':'35px'})], style = {'padding-top':'35%','padding-bottom':'75%','margin-bottom':'0px','background-color':'#71CC97','font-size':'35px'})
                                    ]
                    mainlayout = [update_exercise_interval]
                    scorelayout = []
                elif state == 'Rest':
                    if sessioninfo[code]['Participants'][partindex]['Scores'][index]['Answered'] == 1 and sessioninfo[code]['Participants'][partindex]['Scores'][index]['Score'] > 0:
                        if sessioninfo[code]['Participants'][partindex]['Scores'][index]['Selected'] == 'Hard':
                            headerlayout = [html.H6(children = ['Quiz Ups'], style = {'textAlign' : "center",'margin-top':'0px','margin-bottom':'0px','background-color':'#5AC4D8','padding':'15px'}),
                                        html.H4(children = ['Rest 😎'], style = {'textAlign' : "center",'margin-top':'30px','color':'#5AC4D8','font-size':'30px'}),
                                        html.H4(children = ['✅ +100!'], style = {'textAlign' : "center",'margin-top':'30px','font-size':'40px'}),
                                        html.H6(children = ['Answer: ', [*structure['abcdinput']['index'][index]['Answer'][1].values()][0]], style = {'textAlign' : "center",'margin-top':'30px','padding':'0px 10px 0px 10px'}),
                                        html.H6(children = ['Current Score: {}'.format(sessioninfo[code]['Participants'][partindex]['Total Score'])], style = {'textAlign' : "center",'margin-top':'30px'})]
                            mainlayout = [update_exercise_interval]
                        else:
                            headerlayout = [html.H6(children = ['Quiz Ups'], style = {'textAlign' : "center",'margin-top':'0px','margin-bottom':'0px','background-color':'#5AC4D8','padding':'15px'}),
                                        html.H4(children = ['Rest 😎'], style = {'textAlign' : "center",'margin-top':'30px','color':'#5AC4D8','font-size':'30px'}),
                                        html.H4(children = ['✅ +50!'], style = {'textAlign' : "center",'margin-top':'30px','font-size':'40px'}),
                                        html.H6(children = ['Answer: ', [*structure['abcdinput']['index'][index]['Answer'][0].values()][0]], style = {'textAlign' : "center",'margin-top':'30px','padding':'0px 10px 0px 10px'}),
                                        html.H6(children = ['Current Score: {}'.format(sessioninfo[code]['Participants'][partindex]['Total Score'])], style = {'textAlign' : "center",'margin-top':'30px'})]
                            mainlayout = [update_exercise_interval]
                            
                    elif sessioninfo[code]['Participants'][partindex]['Scores'][index]['Answered'] == 1 and sessioninfo[code]['Participants'][partindex]['Scores'][index]['Score'] == 0:
                        if sessioninfo[code]['Participants'][partindex]['Scores'][index] == 'Hard':
                            headerlayout = [html.H6(children = ['Quiz Ups'], style = {'textAlign' : "center",'margin-top':'0px','margin-bottom':'0px','background-color':'#5AC4D8','padding':'15px'}),
                                            html.H4(children = ['Rest 😎'], style = {'textAlign' : "center",'margin-top':'30px','color':'#5AC4D8','font-size':'30px'}),
                                            html.H4(children = ['❌'], style = {'textAlign' : "center",'margin-top':'30px','font-size':'40px'}),
                                            html.H6(children = ['Answer: ', [*structure['abcdinput']['index'][index]['Answer'][1].values()][0]], style = {'textAlign' : "center",'margin-top':'30px', 'padding':'0px 10px 0px 10px'}),
                                            html.H6(children = ['Current Score: {}'.format(sessioninfo[code]['Participants'][partindex]['Total Score'])], style = {'textAlign' : "center",'margin-top':'30px'})]
                            mainlayout = [update_exercise_interval]
                        else:
                            headerlayout = [html.H6(children = ['Quiz Ups'], style = {'textAlign' : "center",'margin-top':'0px','margin-bottom':'0px','background-color':'#5AC4D8','padding':'15px'}),
                                            html.H4(children = ['Rest 😎'], style = {'textAlign' : "center",'margin-top':'30px','color':'#5AC4D8','font-size':'30px'}),
                                            html.H4(children = ['❌'], style = {'textAlign' : "center",'margin-top':'30px','font-size':'40px'}),
                                            html.H6(children = ['Answer: ', [*structure['abcdinput']['index'][index]['Answer'][0].values()][0]], style = {'textAlign' : "center",'margin-top':'30px', 'padding':'0px 10px 0px 10px'}),
                                            html.H6(children = ['Current Score: {}'.format(sessioninfo[code]['Participants'][partindex]['Total Score'])], style = {'textAlign' : "center",'margin-top':'30px'})]
                            mainlayout = [update_exercise_interval]
                            
                    elif sessioninfo[code]['Participants'][partindex]['Scores'][index]['Selected'] == 'Easy':
                        target = structure['abcdinput']['index'][index]['Target'][0]
                        answer = structure['abcdinput']['index'][index]['Answer'][0]
                        options = structure['abcdinput']['index'][index]['Options'][0]
                        
                        headerlayout = [html.H6(children = ['Quiz Ups'], style = {'textAlign' : "center",'margin-top':'0px','margin-bottom':'0px','background-color':'#5AC4D8','padding':'15px'}),
                                    html.H4(children = ['Rest 😎'], style = {'textAlign' : "center",'margin-top':'30px','color':'#5AC4D8','font-size':'30px'}),
                                    html.H6(children = [target], style = {'textAlign' : "center",'margin-top':'30px','padding':'0px 10px 0px 10px'})]
                        
                        mainlayout = [dbc.Row([dbc.Col([dbc.Button(options['A'],id = 'a-button-1',n_clicks=0, color = 'danger', className="mr-auto", style = {'textAlign' : "center", 'display':'block','margin-left':'auto','margin-right':'10px', 'margin-top':'20px', 'width':'40vw', 'height':'10vh','touch-action': 'manipulation'}),
                                      dbc.Button(options['B'],id = 'b-button-1',n_clicks=0, color = 'primary', className="mr-auto", style = {'textAlign' : "center", 'display':'block','margin-left':'auto','margin-right':'10px', 'margin-top':'20px', 'width':'40vw', 'height':'10vh','touch-action': 'manipulation'})
                                      ]),
                                      dbc.Col([dbc.Button(options['C'],id = 'c-button-1',n_clicks=0, color = 'warning', className="ml-auto", style = {'textAlign' : "center", 'display':'block','margin-left':'10px','margin-right':'auto', 'margin-top':'20px', 'width':'40vw', 'height':'10vh','touch-action': 'manipulation'}),
                                      dbc.Button(options['D'],id = 'd-button-1',n_clicks=0, color = 'success', className="ml-auto", style = {'textAlign' : "center", 'display':'block','margin-left':'10px','margin-right':'auto', 'margin-top':'20px', 'width':'40vw', 'height':'10vh','touch-action': 'manipulation'})
                                      ])]),
                                      update_exercise_interval]
                    elif sessioninfo[code]['Participants'][partindex]['Scores'][index]['Selected'] == 'Hard':
                        target = structure['abcdinput']['index'][index]['Target'][1]
                        answer = structure['abcdinput']['index'][index]['Answer'][1]
                        options = structure['abcdinput']['index'][index]['Options'][1]
                        
                        headerlayout = [html.H6(children = ['Quiz Ups'], style = {'textAlign' : "center",'margin-top':'0px','margin-bottom':'0px','background-color':'#5AC4D8','padding':'15px'}),
                                    html.H4(children = ['Rest 😎'], style = {'textAlign' : "center",'margin-top':'30px','color':'#5AC4D8','font-size':'30px'}),
                                    html.H6(children = [target], style = {'textAlign' : "center",'margin-top':'30px','padding':'0px 10px 0px 10px'})]
                        
                        mainlayout = [dbc.Row([dbc.Col([dbc.Button(options['A'],id = 'a-button-1',n_clicks=0, color = 'danger', className="mr-auto", style = {'textAlign' : "center", 'display':'block','margin-left':'auto','margin-right':'10px', 'margin-top':'20px', 'width':'40vw', 'height':'10vh','touch-action': 'manipulation'}),
                                      dbc.Button(options['B'],id = 'b-button-1',n_clicks=0, color = 'primary', className="mr-auto", style = {'textAlign' : "center", 'display':'block','margin-left':'auto','margin-right':'10px', 'margin-top':'20px', 'width':'40vw', 'height':'10vh','touch-action': 'manipulation'})
                                      ]),
                                      dbc.Col([dbc.Button(options['C'],id = 'c-button-1',n_clicks=0, color = 'warning', className="ml-auto", style = {'textAlign' : "center", 'display':'block','margin-left':'10px','margin-right':'auto', 'margin-top':'20px', 'width':'40vw', 'height':'10vh','touch-action': 'manipulation'}),
                                      dbc.Button(options['D'],id = 'd-button-1',n_clicks=0, color = 'success', className="ml-auto", style = {'textAlign' : "center", 'display':'block','margin-left':'10px','margin-right':'auto', 'margin-top':'20px', 'width':'40vw', 'height':'10vh','touch-action': 'manipulation'})
                                      ])]),
                                      update_exercise_interval]
                    else:
                        headerlayout = [html.H6(children = ['Quiz Ups'], style = {'textAlign' : "center",'margin-top':'0px','margin-bottom':'0px','background-color':'#5AC4D8','padding':'15px'}),
                                    html.H4(children = ['Rest 😎'], style = {'textAlign' : "center",'margin-top':'30px','color':'#5AC4D8','font-size':'30px'})]
                        mainlayout = [easybutton,hardbutton,update_exercise_interval]
                    scorelayout = [html.Div(id = 'score-abcd', style = {'display':'none'}), html.Div(id = 'easy-hard', style = {'display':'none'})]
                    
            else:
                if state == 'Exercise':
                    headerlayout = [html.H6(children = ['Quiz Ups'], style = {'textAlign' : "center",'margin-top':'0px','margin-bottom':'0px','background-color':'#5AC4D8','padding':'15px'}),
                                    html.Div(children = [html.H6(children = ['30 Secs'], style = {'textAlign' : "center",'margin-bottom':'0px','color':'#FFFFFF','font-size':'20px'}),
                                             html.H4(children = [exercisetype[0]], style = {'textAlign' : "center",'margin-bottom':'10px','color':'#FFFFFF','font-size':'35px'}),
                                             html.H6(children = ['30 Secs'], style = {'textAlign' : "center",'margin-bottom':'0px','color':'#FFFFFF','font-size':'20px'}),
                                             html.H4(children = [exercisetype[1]], style = {'textAlign' : "center",'color':'#FFFFFF','font-size':'35px'})], style = {'padding-top':'35%','padding-bottom':'75%','margin-bottom':'0px','background-color':'#71CC97','font-size':'35px'})
                                    ]
                    mainlayout = [update_exercise_interval]
                    scorelayout = []
                elif state == 'Rest':
                    target = structure['abcdinput']['index'][index]['Target']
                    answer = structure['abcdinput']['index'][index]['Answer']
                    options = structure['abcdinput']['index'][index]['Options']
                    
                    if sessioninfo[code]['Participants'][partindex]['Scores'][index]['Answered'] == 1 and sessioninfo[code]['Participants'][partindex]['Scores'][index]['Score'] > 0:
                        headerlayout = [html.H6(children = ['Quiz Ups'], style = {'textAlign' : "center",'margin-top':'0px','margin-bottom':'0px','background-color':'#5AC4D8','padding':'15px'}),
                                    html.H4(children = ['Rest 😎'], style = {'textAlign' : "center",'margin-top':'30px','color':'#5AC4D8','font-size':'30px'}),
                                    html.H4(children = ['✅ +',sessioninfo[code]['Participants'][partindex]['Scores'][index]['Score'],'!'], style = {'textAlign' : "center",'margin-top':'30px','font-size':'40px'}),
                                    html.H6(children = ['Answer: ', structure['abcdinput']['index'][index]['Answer']], style = {'textAlign' : "center",'margin-top':'30px','padding':'0px 10px 0px 10px'}),
                                    html.H6(children = ['Current Score: {}'.format(sessioninfo[code]['Participants'][partindex]['Total Score'])], style = {'textAlign' : "center",'margin-top':'30px'})]
                        mainlayout = [update_exercise_interval]
                    elif sessioninfo[code]['Participants'][partindex]['Scores'][index]['Answered'] == 1 and sessioninfo[code]['Participants'][partindex]['Scores'][index]['Score'] == 0:
                        headerlayout = [html.H6(children = ['Quiz Ups'], style = {'textAlign' : "center",'margin-top':'0px','margin-bottom':'0px','background-color':'#5AC4D8','padding':'15px'}),
                                        html.H4(children = ['Rest 😎'], style = {'textAlign' : "center",'margin-top':'30px','color':'#5AC4D8','font-size':'30px'}),
                                        html.H4(children = ['❌'], style = {'textAlign' : "center",'margin-top':'30px','font-size':'40px'}),
                                        html.H6(children = ['Answer: ', structure['abcdinput']['index'][index]['Answer']], style = {'textAlign' : "center",'margin-top':'30px', 'padding':'0px 10px 0px 10px'}),
                                        html.H6(children = ['Current Score: {}'.format(sessioninfo[code]['Participants'][partindex]['Total Score'])], style = {'textAlign' : "center",'margin-top':'30px'})]
                        mainlayout = [update_exercise_interval]
                    else: 
                        headerlayout = [html.H6(children = ['Quiz Ups'], style = {'textAlign' : "center",'margin-top':'0px','margin-bottom':'0px','background-color':'#5AC4D8','padding':'15px'}),
                                    html.H4(children = ['Rest 😎'], style = {'textAlign' : "center",'margin-top':'30px','color':'#5AC4D8','font-size':'30px'}),
                                    html.H6(children = [target], style = {'textAlign' : "center",'margin-top':'30px','padding':'0px 10px 0px 10px'}),
                                    html.H6(children = ['Enter Number'], style = {'textAlign' : "center",'margin-top':'30px','padding':'0px 10px 0px 10px'})]
                        mainlayout = [numberinput, submitbutton]
                    scorelayout = html.Div(id = 'score', style = {'display':'none'})
            
    elif screentype == 'impostorinput':
        create_score_entry(code,name)
        headerlayout = [html.H4(children = [exercisetype], style = {'textAlign' : "center",'margin-top':'30px'})]
        mainlayout = [impostorguess,update_exercise_interval]
        scorelayout = []

    elif screentype == 'intenseburst':
        if state == 'Exercise':
            headerlayout = [html.H6(children = ['Intense Burst 💪'], style = {'textAlign' : "center",'margin-top':'0px','margin-bottom':'0px','background-color':'#EFEFEF','padding':'15px'}),
                            html.H4(children = [exercisetype], style = {'textAlign' : "center",'padding-top':'50%','margin-bottom':'0px','padding-bottom':'75%','color':'#FFFFFF','background-color':'#71CC97','font-size':'35px'})]
            mainlayout = [update_exercise_interval]
            scorelayout = []
        elif state == 'Rest':
            headerlayout = [html.H6(children = ['Intense Burst 💪'], style = {'textAlign' : "center",'margin-top':'0px','margin-bottom':'0px','background-color':'#EFEFEF','padding':'15px'}),
                            html.H4(children = ['Rest 😎'], style = {'textAlign' : "center",'padding-top':'50%','margin-bottom':'0px','padding-bottom':'75%','color':'#5AC4D8','font-size':'30px'})]
            mainlayout = [update_exercise_interval]
            scorelayout = []

    else:
        headerlayout = []
        mainlayout = [people_number,update_exercise_interval]
        scorelayout = []
    return headerlayout, mainlayout, scorelayout

def question_select(code,name,selection):
    index = sessioninfo[code]['Current Index']
    for i in range(len(sessioninfo[code]['Participants'])):
        if sessioninfo[code]['Participants'][i]['Name'] == name:
            partindex = i
            break
    if selection == 'Hard':
        sessioninfo[code]['Participants'][partindex]['Scores'][index]['Selected'] = 'Hard'
    elif selection == 'Easy':
        sessioninfo[code]['Participants'][partindex]['Scores'][index]['Selected'] = 'Easy'

def create_score_entry(code,name):
    index = sessioninfo[code]['Current Index']
    for i in range(len(sessioninfo[code]['Participants'])):
        if sessioninfo[code]['Participants'][i]['Name'] == name:
            partindex = i
            break
    try:
        if sessioninfo[code]['Participants'][partindex]['Scores'][index]:
            pass
    except KeyError:
        sessioninfo[code]['Participants'][partindex]['Scores'][index] =  {'Entry':'','Score':0,'Answered':0,'Selected':0}

def update_ab_pattern(button,code,name):
    index = sessioninfo[code]['Current Index']
    answerlen = len(sessioninfo[code]['Structure']['abinput']['index'][index]['Answer'])
    if code:
        for i in range(len(sessioninfo[code]['Participants'])):
            if sessioninfo[code]['Participants'][i]['Name'] == name:
                partindex = i
                break
        try:
            pattern = sessioninfo[code]['Participants'][partindex]['Scores'][index]['Entry']
        except KeyError:
            pattern = ''
        if button == 'A' and len(pattern) < answerlen:
            pattern+='A'
            sessioninfo[code]['Participants'][partindex]['Scores'][index]['Entry'] = pattern
            return pattern
        elif button == 'B' and len(pattern) < answerlen:
            pattern+='B'
            sessioninfo[code]['Participants'][partindex]['Scores'][index]['Entry'] = pattern
            return pattern
        elif button == 'Clear':
            pattern = ''
            sessioninfo[code]['Participants'][partindex]['Scores'][index]['Entry'] = pattern
            return pattern
        else:
            if pattern == '':
                return 'Tap A/B!'
            else:
                return pattern

def add_number_after_submit(number,code,name):
    index = sessioninfo[code]['Current Index']
    if code:
        for i in range(len(sessioninfo[code]['Participants'])):
            if sessioninfo[code]['Participants'][i]['Name'] == name:
                partindex = i
                break
        sessioninfo[code]['Participants'][partindex]['Scores'][index]['Entry'] = number

        
    
def check_answer_submit(code,name):
    index = sessioninfo[code]['Current Index']
    structure = sessioninfo[code]['Structure']
    for i in range(len(sessioninfo[code]['Participants'])):
        if sessioninfo[code]['Participants'][i]['Name'] == name:
            partindex = i
            break
    partans = sessioninfo[code]['Participants'][partindex]['Scores'][index]['Entry']
    sessioninfo[code]['Participants'][partindex]['Scores'][index]['Answered'] = 1
    for i in structure.keys():
        for j in structure[i]['index'].keys():
            if int(j) == int(index):
                screentype = i
                break
            else:
                screentype = 'initial'
        if int(j) == int(index):
            break

    if screentype == 'numinput':
        pass

    elif screentype == 'abinput':
        answer = structure['abinput']['index'][index]['Answer']
        if partans == answer:
            sessioninfo[code]['Participants'][partindex]['Scores'][index]['Score'] = 50
            update_current_score(partindex,code)
        else:
            update_current_score(partindex,code)
            
    elif screentype == 'abcdinput':
        answer = float(structure['abcdinput']['index'][index]['Answer'])
        options = float(structure['abcdinput']['index'][index]['Answer'])
        if float(answer) - float(options) < float(partans) < float(answer) + float(options):
            mod = abs(answer - float(partans))
            exp = abs(answer/(answer+mod))
            score = round(float(100)**exp,0)
            sessioninfo[code]['Participants'][partindex]['Scores'][index]['Score'] = score
            update_current_score(partindex,code)
        else:
            update_current_score(partindex,code)
        
    elif screentype == 'impostorinput':
        answer = structure['impostorinput']['index'][index]['Answer']
        update_current_score(partindex,code)
    else:
        pass
    
    return update_exercise_interval


def check_answer_abcd(button,code,name):
    index = sessioninfo[code]['Current Index']
    structure = sessioninfo[code]['Structure']
    for i in range(len(sessioninfo[code]['Participants'])):
        if sessioninfo[code]['Participants'][i]['Name'] == name:
            partindex = i
            break
    try:
        qtype = structure['abcdinput']['index'][index]['QType']
    except KeyError:
        sessioninfo[code]['Participants'][partindex]['Scores'][index]['Entry'] = button
        partans = sessioninfo[code]['Participants'][partindex]['Scores'][index]['Entry']
        sessioninfo[code]['Participants'][partindex]['Scores'][index]['Answered'] = 1
        answer = [*structure['abcdinput']['index'][index]['Answer'].keys()][0]
        if partans == answer:
            sessioninfo[code]['Participants'][partindex]['Scores'][index]['Score'] = 100
            update_current_score(partindex,code)
        else:
            update_current_score(partindex,code)
    else:
        if sessioninfo[code]['Participants'][partindex]['Scores'][index]['Selected'] == 'Easy':
            sessioninfo[code]['Participants'][partindex]['Scores'][index]['Entry'] = button
            partans = sessioninfo[code]['Participants'][partindex]['Scores'][index]['Entry']
            sessioninfo[code]['Participants'][partindex]['Scores'][index]['Answered'] = 1
            answer = [*structure['abcdinput']['index'][index]['Answer'][0].keys()][0]
            if partans == answer:
                sessioninfo[code]['Participants'][partindex]['Scores'][index]['Score'] = 50
                update_current_score(partindex,code)
            else:
                update_current_score(partindex,code)
                
        elif sessioninfo[code]['Participants'][partindex]['Scores'][index]['Selected'] == 'Hard':
            sessioninfo[code]['Participants'][partindex]['Scores'][index]['Entry'] = button
            partans = sessioninfo[code]['Participants'][partindex]['Scores'][index]['Entry']
            sessioninfo[code]['Participants'][partindex]['Scores'][index]['Answered'] = 1
            answer = [*structure['abcdinput']['index'][index]['Answer'][1].keys()][0]
            if partans == answer:
                sessioninfo[code]['Participants'][partindex]['Scores'][index]['Score'] = 100
                update_current_score(partindex,code)
            else:
                update_current_score(partindex,code)
            

def update_current_score(partindex,code):
    scores = []
    for i in sessioninfo[code]['Participants'][partindex]['Scores'].keys():
        scores.append(sessioninfo[code]['Participants'][partindex]['Scores'][i]['Score'])

    totalscore = sum(scores)
    sessioninfo[code]['Participants'][partindex]['Total Score'] = totalscore

def check_total_answers(code):
    index = sessioninfo[code]['Current Index']
    totalpeople = len(sessioninfo[code]['Participants'])
    if totalpeople > 0:
        try:
            totalanswers = sum([sessioninfo[code]['Participants'][i]['Scores'][index]['Answered'] for i in range(totalpeople)])
        except KeyError:
            totalanswers = 0
        return '{}/{} Answered'.format(totalanswers,totalpeople)
    else:
        return 'No Participants in Session'

def update_leaderboard(code,name):
    totalpeople = len(sessioninfo[code]['Participants'])
    if totalpeople > 0:
        participants_scores = [[sessioninfo[code]['Participants'][i]['Name'],sessioninfo[code]['Participants'][i]['Total Score']] for i in range(totalpeople)]
        participants_scores.sort(key = TakeSecond,reverse = True)
        participants_scores = CreatePosition(participants_scores)
        leader = participants_scores[0]
        for i in range(totalpeople):
            if participants_scores[i][0] == name:
                player = participants_scores[i]
                break
        leaderboard = html.Tbody(children = [
                                html.Tr([
                                    html.Td('🏆',style={'padding-left': '15px', 'padding-right': '15px', 'color':'#FFD700'}),
                                    html.Td(leader[0],style={'padding-left': '15px', 'padding-right': '15px', 'color':'#FFD700'}),
                                    html.Td(leader[1],style={'padding-left': '15px', 'padding-right': '15px', 'color':'#FFD700'})
                                    ]),
                                html.Tr([
                                    html.Td(player[2]),
                                    html.Td('You'),
                                    html.Td(player[1])
                                    ])
                                ], id = 'live-leaderboard')
        return leaderboard
    else:
        leaderboard = html.Tbody(children = [
                                html.Tr([
                                    html.Td('N/A'),
                                    ])
                                ], id = 'live-leaderboard')
        return leaderboard

def update_instructor_leaderboard(code):
    totalpeople = len(sessioninfo[code]['Participants'])
    if totalpeople > 0:
        participants_scores = [[sessioninfo[code]['Participants'][i]['Name'],sessioninfo[code]['Participants'][i]['Total Score']] for i in range(totalpeople)]
        participants_scores.sort(key = TakeSecond,reverse = True)
        participants_scores = CreatePosition(participants_scores)
        if totalpeople < 3:
            leaderboard = html.Tbody(children = [
                                    html.Tr([
                                        html.Td(participants_scores[i][2],style={'padding-left': '15px', 'padding-right': '15px'}),
                                        html.Td(participants_scores[i][0],style={'padding-left': '15px', 'padding-right': '15px'}),
                                        html.Td(participants_scores[i][1],style={'padding-left': '15px', 'padding-right': '15px'})
                                        ]) for i in range(totalpeople)
                                    ], id = 'live-leaderboard')
            return leaderboard
        else:
            leaderboard = html.Tbody(children = [
                                    html.Tr([
                                        html.Td(participants_scores[i][2],style={'padding-left': '15px', 'padding-right': '15px'}),
                                        html.Td(participants_scores[i][0],style={'padding-left': '15px', 'padding-right': '15px'}),
                                        html.Td(participants_scores[i][1],style={'padding-left': '15px', 'padding-right': '15px'})
                                        ]) for i in range(3)
                                    ], id = 'live-leaderboard')
            return leaderboard

    else:
        leaderboard = html.Tbody(children = [
                                html.Tr([
                                    html.Td('N/A'),
                                    ])
                                ], id = 'live-leaderboard')
        return leaderboard


