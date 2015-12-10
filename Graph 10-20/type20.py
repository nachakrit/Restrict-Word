import plotly.plotly as py
import plotly.graph_objs as go
py.sign_in('thasorn', 'cmf6kajkjy')
#py.sign_in('ID', 'Key you get from plot.ly')
fig = {
    'data': [{'labels': ['Western', 'Southern', 'North East', 'Northern', 'Central', 'Eastern'],
              'values': [88.89, 0.0, 0.0, 11.11, 0.0, 0.0],
              'type': 'pie'}],
    'layout': {'title': 'Type 20: Others Driving Licence Statistics'}
}

url = py.plot(fig, filename='Pie Chart Example')
