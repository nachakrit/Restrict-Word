import plotly.plotly as py
import plotly.graph_objs as go
py.sign_in('thasorn', 'cmf6kajkjy')
#py.sign_in('ID', 'Key you get from plot.ly')
fig = {
    'data': [{'labels': ['Western', 'Southern', 'North East', 'Northern', 'Central', 'Eastern'],
              'values': [6.61, 4.67, 51.27, 14.37, 13.48, 9.61],
              'type': 'pie'}],
    'layout': {'title': 'Type 11: Motor  Tricycle (Life) Statistics'}
}

url = py.plot(fig, filename='Type 11')
