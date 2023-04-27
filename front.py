import pandas as pd
import plotly.graph_objects as go


import dash
import dash_core_components as dcc
import dash_html_components as html


url = "http://172.31.90.134:5000/mostrar_estacionesnivel?psw=12345678"
data = pd.read_json(url,convert_dates='True')

latr = []
lonr = []
zr = []
for i in range(0,100):
  zr.append(data['datos'][i]['porcentajeNivel'])
  latr.append(data['datos'][i]['coordenadas'][0]['latitud'])
  lonr.append(data['datos'][i]['coordenadas'][0]['longitud'])

fig = go.Figure(go.Densitymapbox(lat=latr,lon=lonr,z=zr,radius=20, opacity=0.9, zmin=0, zmax = 100))
fig.update_layout(mapbox_style="stamen-terrain",mapbox_center_lon=-75.589,mapbox_center_lat=6.2429)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})



app = dash.Dash()
app.layout = html.Div([
               html.H1("Este es mi proyecto"),
               dcc.Graph(figure=fig)
               ])

app.run_server(host='0.0.0.0',port=80)
