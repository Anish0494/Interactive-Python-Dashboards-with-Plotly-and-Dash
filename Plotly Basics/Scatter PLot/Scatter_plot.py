#importing the libraries
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

#Creating the random data
np.random.seed(42)
random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)

#Plot the data
data = [go.Scatter(x=random_x,
                    y=random_y,
                    mode='markers',
                    marker=dict(
                        size=12,
                        color='rgb(51,205,156)',
                        symbol='pentagon',
                        line = {'width':2}
                    ))]
##defining layout
layout = go.Layout(title='Scatter PLot',
                    xaxis={'title':'Random X data'},
                    yaxis=dict(title='Random y data'),
                    hovermode='closest')
fig = go.Figure(data=data,layout=layout)
pyo.plot(fig,filename='scatter.html')