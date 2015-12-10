import plotly.plotly as py
import plotly.graph_objs as go
py.sign_in('thasorn', 'cmf6kajkjy')
#py.sign_in('ID', 'Key you get from plot.ly')
fig = {
    'data': [{'labels': ['Western', 'Southern', 'North East', 'Northern', 'Central', 'Eastern'],
              'values': [6.32, 16.26, 26.43, 21.69, 17.39, 11.91],
              'type': 'pie'}],
    'layout': {'title': 'Type 16: International  Driving  Licence Statistics'}
}

url = py.plot(fig, filename='Type 16')
