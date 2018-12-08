#######
# Objective: build a dashboard that imports OldFaithful.csv
# from the data directory, and displays a scatterplot.
# The field names are:
# 'D' = date of recordings in month (in August),
# 'X' = duration of the current eruption in minutes (to nearest 0.1 minute),
# 'Y' = waiting time until the next eruption in minutes (to nearest minute).
######

# Perform imports here:

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import numpy as np

app = dash.Dash()

df = pd.read_csv('../data/OldFaithful.csv')

print(df.head())

# Launch the application:

marker01 = dict({ 'size':12,
                  'color': 'rgb(51,204,153)',
                  'symbol':'circle',
                  'line':{'width':2}
                })

data01 = [go.Scatter(x=df['X'],
                     y=df['Y'],
                     mode='markers',
                     marker = marker01
                     )]


app.layout = html.Div([
                    dcc.Graph(id='scatterplot',
                    figure = {'data':data01,
                    'layout':go.Layout(title='My Scatterplot',
                                    xaxis = {'title':'Matt #1'})}
                    )])


if __name__ == '__main__':
    app.run_server()

# Create a DataFrame from the .csv file:


# Create a Dash layout that contains a Graph component:





















# Add the server clause:
