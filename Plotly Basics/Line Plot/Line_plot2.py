#importing the libraries
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

#loadij]ng the data
data = pd.read_csv('Line Plot\data.csv')
print(data.head())

#filtering the dataset
df2 = data[data['DIVISION']=='1']
df2.set_index('NAME',inplace=True)
list_of_pop_col=[col for col in df2.columns if col.startswith('POP')]
df2 = df2[list_of_pop_col]

fig = [go.Scatter(x=df2.columns,
                    y=df2.loc[name],
                    mode='lines+markers') for name in df2.index]

pyo.plot(fig)