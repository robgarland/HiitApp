# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 16:01:24 2021

@author: garla
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd

from app import Homepage, Instructor

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.UNITED])

app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    dcc.Location(id = 'url', refresh = False),
    html.Div(id = 'page-content')
])

@app.callback(Output('page-content', 'children'),
            [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/instructor':
        return Instructor()
    else:
        return Homepage()

@app.callback(Output('page-content', 'children'),
            [Input('code', 'value')])
def check_text_input(value):
    if value == "11111":
        
        

if __name__ == '__main__':
    app.run_server(debug=True)
