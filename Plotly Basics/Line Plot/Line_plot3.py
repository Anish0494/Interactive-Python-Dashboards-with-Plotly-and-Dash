#Importing the libraries
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df=pd.read_csv('Line Plot\YumaAZ.csv')
print(df.head())
day=['MONDAY','TUESDAY','WEDNESDAY','THRUSDAY','FRIDAY','SATURDAY','SUNDAY']

data = []

for d in day:
    trace=go.Scatter(x=df['LST_TIME'],
                    y=df[df['DAY']==d]['T_HR_AVG'],
                    mode='lines+markers')
    data.append(trace)
layout=go.Layout(title='Line Graph')
fig=go.Figure(data=data,
              layout=layout)
pyo.plot(fig)
    