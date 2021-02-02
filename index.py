# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 16:01:24 2021

@author: garla
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd

from app import Homepage, Instructor, Workout, update_inputs, update_workout

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.UNITED])

app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    dcc.Location(id = 'url', refresh = False),
    html.Div(id = 'page-content')
])


"""
screentypes = ['inputs',
               'warmup',
               'leaderboard',
               'numinput',
               'abinput',
               'abcdinput',
               'impostorinput',
               ]
"""

# List of exercises avaliable
current_index = 0

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
    'inputs' : {'index' : {0 : None
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

@app.callback(Output('page-content', 'children'),
            [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/instructor':
        return Instructor()
    elif pathname == '/workout':
        return Workout()
    else:
        global current_index
        current_index = 0
        return Homepage()

@app.callback([Output('header-div','children'),
               Output('main-div','children')],
              [Input('code-input','value')])
def input_updater(codein):

    header, main = update_inputs(codein)     
           
    return header, main

@app.callback([Output('header-div-1', 'children'),
                Output('main-div-1', 'children'),
                Output('score-div', 'children')],
                [Input('next-button','n_clicks')])
def update_exercise(n_clicks):
    global current_index 
    current_index += 1
    header, main, score = update_workout(current_index)
    return header, main, score



if __name__ == '__main__':
    app.run_server(debug=True)