#######
# Objective: Create a histogram that plots the 'length' field
# from the Abalone dataset (../data/abalone.csv).
# Set the range from 0 to 1, with a bin size of 0.02
######

# Perform imports here:

import plotly.offline as pyo
import plotly.graph_objs as go
import numpy as np
import pandas as pd


# create a DataFrame from the .csv file:

df=pd.read_csv('../data/abalone.csv')

print(df.columns)


# create a data variable:

xBins = dict(start=0, end=1, size=0.02)
data=[go.Histogram(x=df['length'], xbins=xBins)]
layout = go.Layout(title='CARS ADN SHIT')
fig= go.Figure(data=data, layout=layout)
pyo.plot(fig)



# add a layout




# create a fig from data & layout, and plot the fig
