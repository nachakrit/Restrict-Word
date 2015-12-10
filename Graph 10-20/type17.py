import plotly.plotly as py
import plotly.graph_objs as go
py.sign_in('thasorn', 'cmf6kajkjy')
#py.sign_in('ID', 'Key you get from plot.ly')
fig = {
    'data': [{'labels': ['Western', 'Southern', 'North East', 'Northern', 'Central', 'Eastern'],
              'values': [2.94, 36.03, 16.18, 12.5, 8.82, 23.53],
              'type': 'pie'}],
    'layout': {'title': 'Type 17: Tractor Statistics'}
}

url = py.plot(fig, filename='Pie Chart Example')
