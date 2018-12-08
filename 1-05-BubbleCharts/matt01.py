
import plotly.offline as pyo
import plotly.graph_objs as go
import numpy as np
import pandas as pd


df = pd.read_csv('../data/mpg.csv')

myDict=dict(size=df['weight']/100, color=df['cylinders'],showscale=True)

data=[go.Scatter(x=df['horsepower'], y=df['mpg'], text=df['name'], mode='markers', marker=myDict)]

layout=go.Layout(title='Bubble Chart')
fig=go.Figure(data=data, layout=layout)
pyo.plot(fig)


print(df.columns)
print(df)

