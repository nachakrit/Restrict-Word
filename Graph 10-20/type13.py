import plotly.plotly as py
import plotly.graph_objs as go
py.sign_in('thasorn', 'cmf6kajkjy')
#py.sign_in('ID', 'Key you get from plot.ly')
fig = {
    'data': [{'labels': ['Western', 'Southern', 'North East', 'Northern', 'Central', 'Eastern'],
              'values': [7.99, 6.9, 26.17, 4.34, 48.67, 5.94],
              'type': 'pie'}],
    'layout': {'title': 'Type 13: Public  Automobile Statistics'}
}

url = py.plot(fig, filename='Pie Chart Example')
