
import plotly.offline as pyo
import plotly.graph_objs as go
import numpy as np
import pandas as pd

df = pd.read_csv('../data/mpg.csv')

xBins = dict(start=0, end=25, size=0.1)

data=[go.Histogram(x=df['mpg'], xbins=xBins)]

layout = go.Layout(title='CARS ADN SHIT')

fig= go.Figure(data=data, layout=layout)

pyo.plot(fig)


print(df)

