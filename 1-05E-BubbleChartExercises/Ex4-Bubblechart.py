#######
# Objective: Create a bubble chart that compares three other features
# from the mpg.csv dataset. Fields include: 'mpg', 'cylinders', 'displacement'
# 'horsepower', 'weight', 'acceleration', 'model_year', 'origin', 'name'
######

# Perform imports here:

import plotly.offline as pyo
import plotly.graph_objs as go
import numpy as np
import pandas as pd


# create a DataFrame from the .csv file:

df = pd.read_csv('../data/mpg.csv')

# create data by choosing fields for x, y and marker size attributes


myDict=dict(size=df['acceleration'], color=df['acceleration'],showscale=True)

data=[go.Scatter(x=df['model_year'], y=df['mpg'], text=df['name'], mode='markers', marker=myDict)]

layout=go.Layout(title='Bubble Chart')
fig=go.Figure(data=data, layout=layout)
pyo.plot(fig)


print(df.columns)





# create a layout with a title and axis labels







# create a fig from data & layout, and plot the fig
