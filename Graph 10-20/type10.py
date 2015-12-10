import plotly.plotly as py
import plotly.graph_objs as go
py.sign_in('thasorn', 'cmf6kajkjy')
#py.sign_in('ID', 'Key you get from plot.ly')
fig = {
    'data': [{'labels': ['Western', 'Southern', 'North East', 'Northern', 'Central', 'Eastern'],
              'values': [13.12, 13.28, 19.93, 24.65, 16.88, 12.13],
              'type': 'pie'}],
    'layout': {'title': 'Type 10: Private  Automobile (Life) Statistics'}
}

url = py.plot(fig, filename='Type 10')
