import plotly.plotly as py
import plotly.graph_objs as go
py.sign_in('thasorn', 'cmf6kajkjy')
#py.sign_in('ID', 'Key you get from plot.ly')
fig = {
    'data': [{'labels': ['Western', 'Southern', 'North East', 'Northern', 'Central', 'Eastern'],
              'values': [12.2, 15.76, 20.61, 30.31, 12.67, 8.45],
              'type': 'pie'}],
    'layout': {'title': 'Type 12: Motor  Tricycle (Life) Statistics'}
}

url = py.plot(fig, filename='Pie Chart Example')
