import plotly.plotly as py
import plotly.graph_objs as go
py.sign_in('thasorn', 'cmf6kajkjy')
#py.sign_in('ID', 'Key you get from plot.ly')
fig = {
    'data': [{'labels': ['Western', 'Southern', 'North East', 'Northern', 'Central', 'Eastern'],
              'values': [0.14, 0.06, 82.55, 16.74, 0.37, 0.14],
              'type': 'pie'}],
    'layout': {'title': 'Type 19: Farm Vehicle Driving Licence Statistics'}
}

url = py.plot(fig, filename='Pie Chart Example')
