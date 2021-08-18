from pkgutil import read_code
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc 
import dash_html_components as html
from flask.templating import render_template

from pandas_datareader import data as web 
from datetime import datetime as dt
import csv
from os import write
import csv
from typing import Text



app = dash.Dash('Hello World',
                external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])


f = open('text1.csv', 'r')
stock_list = csv.reader(f)
for txt in stock_list: 
    
    app.layout = html.Div([
    dcc.Dropdown(
        id="my-dropdown",
        options=[{"label": x, "value": x} 
                 for x in txt],
        value= '000020.KS',
        clearable=False,
        
    ),
    dcc.Graph(id="my-graph"), 
], title='이현수 초 천재', style={'width': 500})

@app.callback(Output('my-graph', 'figure'), [Input('my-dropdown', 'value')])
def update_graph(selected_dropdown_value):
    df = web.DataReader(
        selected_dropdown_value,
        'yahoo',
        dt(2017, 1, 1), 
        dt.now()
    )   
    return {
        'data': [{
            'x': df.index,
            'y': df.Close
        }], 
        'layout': {'margin': {'l': 40, 'r': 0, 't': 150, 'b': 30},
        'title': '사랑해',

        }
        
    }   



if __name__ == '__main__':
    app.run_server(debug=True)