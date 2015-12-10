import plotly.plotly as py
import plotly.graph_objs as go
py.sign_in('Scrapberg', 'hsa60sz9ly')
  #py.sign_in('ID', 'Key you get from plot.ly')
fig = {
    'data': [{'labels': ['Motor Vehicle', 'Local Transport', 'Non Motorized'],
              'values': [19, 26, 55],
              'type': 'pie'}],
    'layout': {'title': 'Driving Licences Type'}
}

url = py.plot(fig, filename='Pie Chart Example')
