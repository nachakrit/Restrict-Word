import plotly.plotly as py
import plotly.graph_objs as go
py.sign_in('thasorn', 'cmf6kajkjy')
#py.sign_in('ID', 'Key you get from plot.ly')
fig = {
    'data': [{'labels': ['Western', 'Southern', 'North East', 'Northern', 'Central', 'Eastern'],
              'values': [6.68, 0.11, 47.35, 16.64, 14.45, 14.78],
              'type': 'pie'}],
    'layout': {'title': 'Type 14: Public  Motor  Tricycle Statistics'}
}

url = py.plot(fig, filename='Type 14')
