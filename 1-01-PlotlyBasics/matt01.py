
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(42)
random_x = np.random.randint(0,101,100)
random_y = np.random.randint(0,101,100)

xTitle=dict(title='My X Axis')
xTitle=dict(title='My Y Axis')
myMarker=dict(
                size=12,
                color='rgb(46,2,211)',
                symbol='circle',
                line={'width':2}
            )


data = [go.Scatter(x=random_x, y=random_y, mode="markers", marker=myMarker)]
layout = go.Layout(title='My CHART', xaxis=xTitle, yaxis=xTitle, hovermode='closest')
fig=go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='scatter.html')


print(random_x)

