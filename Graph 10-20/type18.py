import plotly.plotly as py
import plotly.graph_objs as go
py.sign_in('thasorn', 'cmf6kajkjy')
#py.sign_in('ID', 'Key you get from plot.ly')
fig = {
    'data': [{'labels': ['Western', 'Southern', 'North East', 'Northern', 'Central', 'Eastern'],
              'values': [8.09, 7.26, 23.6, 29.43, 19.51, 11.91],
              'type': 'pie'}],
    'layout': {'title': 'Type 18: Tractor Driving Licence Statistics'}
}

url = py.plot(fig, filename='Type 18')
