# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 16:01:24 2021

@author: garla
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
import pandas as pd

from app import Homepage, Instructor, Workout, InstructorWorkout, update_inputs, instructor_setup, workout_structure, enter_session, update_participants_body, update_instructor_workout, update_index, update_workout

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],meta_tags=[{'name' : 'viewport',
                                                                                  'content' : 'width = device-width, initial-scale = 1.0, maximum-scale = 1.2, minimumscale = 0.8'}])

app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    dcc.Location(id = 'url', refresh = False),
    html.Div(id = 'page-content'),
    html.Div(id = 'hidden-div-1',
                style = {'display':'none'}
                ),
    html.Div(id = 'hidden-div-2',
                style = {'display':'none'}
                ),
    html.Div(id = 'hidden-div-3',
                style = {'display':'none'}
                )
    
])


"""
screentypes = ['inputs',
               'warmup',
               'leaderboard',
               'numinput',
               'abinput',
               'abcdinput',
               'impostorinput',
               'intenseburst'
               ]
"""

@app.callback(Output('page-content', 'children'),
            [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/instructor':
        return Instructor()
    elif pathname == '/workout':
        return Workout()
    elif pathname == '/instructor/workout':
        return InstructorWorkout()
    else:
        return Homepage()

@app.callback([Output('header-div','children'),
               Output('main-div','children'),
               Output('hidden-div-1','children')],
              [Input('enter-button','n_clicks')],
              [State('code-input','value')])
def input_updater(n_clicks,codein):

    header, main, hidden = update_inputs(codein)     
           
    return header, main, hidden

@app.callback([Output('header-div-2', 'children'),
                Output('main-div-2', 'children'),
                Output('score-div-2', 'children'),
                Output('hidden-div-2','children')],
                [Input('icebreaker-select','n_clicks'),
                 Input('impostor-select','n_clicks')],
                [State('instructor-name-input','value')])
def instructor_session_setup(n_clicks_1,n_clicks_2,name):    
    if n_clicks_1 == 0 and n_clicks_2 == 0:
        raise PreventUpdate
    else:
        changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
        if 'impostor-select' in changed_id:
            sessiontype = 'Impostor'
            header, main, score, hidden = instructor_setup(sessiontype, name)
            return header, main, score, hidden
        elif 'icebreaker-select' in changed_id:
            sessiontype = 'Icebreaker'
            header, main, score, hidden = instructor_setup(sessiontype, name)
            return header, main, score, hidden
        else:
            raise PreventUpdate
    
@app.callback([Output('hidden-div-3','children'),
               Output('url','pathname')],
              [Input('start-button', 'n_clicks')],
              [State('url','pathname'), State('name-dropdown','value'), State('hidden-div-1','children'), State('hidden-div-2','children')])    
def store_details_next_path(n_clicks,path,name,usrcode,inscode):
    if n_clicks == 0:
        raise PreventUpdate
    else:
        if path == '/instructor':
            workout_structure(inscode[0])
            children = []
            newpath = "/instructor/workout"
            return children, newpath
        else:
            if name:      
                children = [name]
                enter_session(usrcode[0], name)
                newpath = "/workout"
                return children, newpath
            else:
                children = []
                newpath = "/"
                return children, newpath

@app.callback([Output('current-participants','children')],
              [Input('check-participants-interval','n_intervals')],
              [State('hidden-div-1','children'), State('hidden-div-2','children')])
def update_participants_table(n_intervals,usrcode,inscode):
        if usrcode:
            children = update_participants_body(usrcode[0])
            return children
        elif inscode:
            children = update_participants_body(inscode[0])
            return children
        else:
            raise PreventUpdate
    
@app.callback([Output('header-div-3', 'children'),
                Output('main-div-3', 'children'),
                Output('score-div-3', 'children')],
                [Input('moveon-button','n_clicks')],
                [State('hidden-div-2','children')])
def update_instructor_exercise(n_clicks,inscode):
    if n_clicks == 0:
        header, main, score = update_instructor_workout(0,inscode[0])
    else:
        current_index = update_index(inscode[0])
        header, main, score = update_instructor_workout(current_index,inscode[0])
    return header, main, score

@app.callback([Output('header-div-1', 'children'),
                Output('main-div-1', 'children'),
                Output('score-div', 'children')],
                [Input('update-exercise-interval','n_intervals')],
                [State('hidden-div-1','children')])
def update_particpant_exercise(n_intervals,usrcode):
    if usrcode:
        header, main, score = update_workout(usrcode[0])
        return header, main, score
    else:
        raise PreventUpdate

if __name__ == '__main__':
    app.run_server(debug=True)