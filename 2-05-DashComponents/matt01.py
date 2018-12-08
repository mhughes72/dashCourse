

#######
# This provides examples of Dash Core Components.
# Feel free to add things to it that you find useful.
######
import dash
import dash_core_components as dcc
import dash_html_components as html
from datetime import datetime as dt

app = dash.Dash()

app.layout = html.Div([

    # DROPDOWN https://dash.plot.ly/dash-core-components/dropdown
    html.Label('Dropdown'),
    dcc.Dropdown(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Mon', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='MTL'
    ),

    html.Label('Multi-Select Dropdown'),
    dcc.Dropdown(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Mon', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value=['MTL', 'SF'],
        multi=True
    ),
    html.P(
    html.Label('Date Picker')),
    dcc.DatePickerSingle(
        id='date-picker-single',
        date=dt(1997, 5, 10)
    ),

    # SLIDER https://dash.plot.ly/dash-core-components/slider
    html.P(html.Label('Slider')),
    html.P(
    dcc.Slider(
        min=-5,
        max=10,
        step=0.5,
        marks={i: i for i in range(-5,11)},
        value=-3
    )),

    # RADIO ITEMS https://dash.plot.ly/dash-core-components/radioitems
    html.Label('Radio Items'),
    dcc.RadioItems(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Mon', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='MTL'
    )
], style={'width': '50%'})

if __name__ == '__main__':
    app.run_server()
