
import numpy as np
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go


df = pd.read_csv('../SourceData/nst-est2017-alldata.csv')


df2 = df[df['DIVISION']=='1']
df2.set_index('NAME', inplace=True)
list_of_pop_col = [col for col in df2.columns if col.startswith('POP')]
#newComp = [col for col in df2.columns if col=='POPESTIMATE2013']
df2 = df2[list_of_pop_col]

data = [ go.Scatter(x=df2.columns,
                    y=df2.loc[name],
                    mode='lines',
                    name=name) for name in df2.index]

pyo.plot(data)



# xTitle=dict(title='My X Axis')
# xTitle=dict(title='My Y Axis')
# myMarker=dict(
#                 size=12,
#                 color='rgb(46,2,211)',
#                 symbol='circle',
#                 line={'width':2}
#             )
# 
# trace0=go.Scatter(x=random_x, y=random_y+5, mode="markers", marker=myMarker, name='markers')
# trace1=go.Scatter(x=random_x, y=random_y, mode="lines", marker=myMarker, name='myLines')
# trace2=go.Scatter(x=random_x, y=random_y-5, mode="lines+markers", marker=myMarker, name='linesmarkers')
# data=[trace0,trace1,trace2]
# layout = go.Layout(title='My CHART', xaxis=xTitle, yaxis=xTitle, hovermode='closest')
# fig=go.Figure(data=data, layout=layout)
# pyo.plot(fig, filename='scatter.html')




