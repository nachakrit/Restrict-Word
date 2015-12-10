import plotly.plotly as py
import plotly.graph_objs as go
py.sign_in('thasorn', 'cmf6kajkjy')
#py.sign_in('ID', 'Key you get from plot.ly')
fig = {
    'data': [{'labels': ['Western', 'Southern', 'North East', 'Northern', 'Central', 'Eastern'],
              'values': [15.71, 10.89, 8.91, 6.05, 43.42, 15.01],
              'type': 'pie'}],
    'layout': {'title': 'Type 15: Public  Motorcycle Statistics'}
}

url = py.plot(fig, filename='Type 15')
