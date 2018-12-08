
import plotly.offline as pyo
import plotly.graph_objs as go
import numpy as np
import pandas as pd


df = pd.read_csv('../data/2018WinterOlympics.csv')

trace1=go.Bar(x=df['NOC'],y=df['Gold'],name='Gold',marker={'color':'#FFD700'})

trace2=go.Bar(x=df['NOC'],y=df['Silver'],name='Silver',marker={'color':'#FF7864'})

trace3=go.Bar(x=df['NOC'],y=df['Bronze'],name='Bronze',marker={'color':'#FFB754'})

data = [trace1,trace2,trace3]

layout=go.Layout(title='Medals',barmode='stack')
fig=go.Figure(data=data,layout=layout)

pyo.plot(fig)


print(df.head())