#######
# Objective: Make a DataFrame using the Abalone dataset (../data/abalone.csv).
# Take two independent random samples of different sizes from the 'rings' field.
# HINT: np.random.choice(df['rings'],10,replace=False) takes 10 random values
# Use box plots to show that the samples do derive from the same population.
######

# Perform imports here:

import plotly.offline as pyo
import plotly.graph_objs as go
import numpy as np
import pandas as pd



# create a DataFrame from the .csv file:

df = pd.read_csv('../data/abalone.csv')
print(df)


# take two random samples of different sizes:

choice1 = np.random.choice(df['rings'],1000,replace=False)
choice2 = np.random.choice(df['rings'],1000,replace=False)

# create a data variable with two Box plots:


data = [
    go.Box(
        y=choice1,
        name='choice1'
    ),
    go.Box(
        y=choice2,
        name='choice2'
    )
]
layout = go.Layout(
    title = 'Comparison of three-letter-word frequencies<br>\
    between Quintus Curtius Snodgrass and Mark Twain'
)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='box3.html')








# add a layout




# create a fig from data & layout, and plot the fig


