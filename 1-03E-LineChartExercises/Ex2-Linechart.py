#######
# Objective: Using the file 2010YumaAZ.csv, develop a Line Chart
# that plots seven days worth of temperature data on one graph.
# You can use a for loop to assign each day to its own trace.
######

# Perform imports here:

import numpy as np
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go


# Create a pandas DataFrame from 2010YumaAZ.csv
df = pd.read_csv('../data/2010YumaAZ.csv')
days = ['TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY','MONDAY']
print(df.columns)

# Use a for loop (or list comprehension to create traces for the data list)



myMarker=dict(
                size=12,
                color='rgb(46,2,211)',
                symbol='circle',
                line={'width':2}
            )

# data = [ go.Scatter(x=df['LST_TIME'],
#                     y=df['T_HR_AVG'],
#                     mode='lines',
#                     name=DAY) for DAY in df.index]

dayList = [day for day in df['DAY'].unique()]
print(dayList)

myMarker = dict(
            size = 12,
            color = 'rgb(51,204,153)',
            symbol = 'pentagon',
            line = dict(
            width = 2
            ))

data = [go.Scatter(x=df['LST_TIME'],
                    y=df['T_HR_AVG'],
                    mode='markers+lines',
                    name=dayList
                    )]

pyo.plot(data)

# for day in days:
#     # What should go inside this Scatter call?
#     trace = go.Scatter()
#     data.append(trace)

# Define the layout





# Create a fig from data and layout, and plot the fig




