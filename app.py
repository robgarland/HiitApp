# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 14:48:37 2021

@author: garla
"""
import pandas as pd 
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input

header1 = html.H3(
    'Enter Code:'
)

header2 = html.H3(
    'Enter Name:'
)

codeinput = dcc.Input(id = 'code', type = 'text', placeholder = "Enter Code", maxLength = '5')

nameinput = dcc.Input(id = 'name', type = 'text', placeholder = "Enter Name", maxLength = '15')

output1 = html.Div(id = 'output1',
                children = [],
                )

def Homepage():
    layout = html.Div([
        header,
        inputtype
    ])
    return layout

def Instructor():
    layout = html.Div([

    ])
    return layout
    



    

