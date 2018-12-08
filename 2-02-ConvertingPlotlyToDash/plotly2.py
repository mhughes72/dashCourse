import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np

app = dash.Dash()

# Creating DATA
np.random.seed(42)
random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)

marker01 = dict({ 'size':12,
                  'color': 'rgb(51,204,153)',
                  'symbol':'square',
                  'line':{'width':2}
                })

data01 = [go.Scatter(x=random_x,
                     y=random_y,
                     mode='line-markers',
                     marker = marker01
                     )]

marker02 = dict({'size':12,
                 'color': 'rgb(200,204,53)',
                 'symbol':'pentagon',
                 'line':{'width':2}
                 }) 
                            
data02 = [go.Scatter(x=random_x,
                     y=random_y,
                     mode='markers',
                     marker = marker02
                      )]     
                            
                            

app.layout = html.Div([
                    dcc.Graph(id='scatterplot',
                    figure = {'data':data01,
                    'layout':go.Layout(title='My Scatterplot',
                                    xaxis = {'title':'Matt #1'})}
                    ),
                    dcc.Graph(id='scatterplot2',
                    figure = {'data':data02,
                    'layout':go.Layout(title='Second Plot 2',
                                       xaxis = {'title':'Matt #2'})}
                     )])

if __name__ == '__main__':
    app.run_server()
