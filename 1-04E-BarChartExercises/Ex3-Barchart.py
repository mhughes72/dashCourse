#######
# Objective: Create a stacked bar chart from
# the file ../data/mocksurvey.csv. Note that questions appear in
# the index (and should be used for the x-axis), while responses
# appear as column labels.  Extra Credit: make a horizontal bar chart!
######

# Perform imports here:

import plotly.offline as pyo
import plotly.graph_objs as go
import numpy as np
import pandas as pd


# create a DataFrame from the .csv file:

df = pd.read_csv('../data/mocksurvey.csv')
print(df.columns)

# create traces using a list comprehension:


trace1=go.Bar(x=df['Unnamed: 0'],y=df['Strongly Agree'],name='Strongly Agree',marker={'color':'#FFD700'})
trace2=go.Bar(x=df['Unnamed: 0'],y=df['Somewhat Agree'],name='Somewhat Agree',marker={'color':'#FF5487'})
trace3=go.Bar(x=df['Unnamed: 0'],y=df['Neutral'],name='Neutral',marker={'color':'#FF3234'})
trace4=go.Bar(x=df['Unnamed: 0'],y=df['Somewhat Disagree'],name='Somewhat Disagree',marker={'color':'#FF6598'})
trace5=go.Bar(x=df['Unnamed: 0'],y=df['Strongly Disagree'],name='Strongly Disagree',marker={'color':'#FF4599'})



data = [trace1,trace2,trace3,trace4,trace5]

layout=go.Layout(title='Medals',barmode='stack')
fig=go.Figure(data=data,layout=layout)

pyo.plot(fig)




# create a layout, remember to set the barmode here





# create a fig from data & layout, and plot the fig.
