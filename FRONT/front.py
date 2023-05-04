import pandas as pd
import plotly.graph_objects as go


import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State

import requests

url = "http://44.199.102.82:5000/mostrar_estacionesnivel?psw=12345678"
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

urldB = 'http://44.199.102.82:500/users'

response = requests.get(urldB)

app = dash.Dash()



if response.status_code == 200:
   data = response.json()
   #app = dash.Dash()
   #primero verificamos que pase una pagina de validación
   app.layout = html.Div([
       html.H3('Iniciar Sesión'),
       html.Label('Usuario'),
       dcc.Input(id='input-usuario', type='text', placeholder='Ingresa tu usuario'),
       html.Label('Contraseña'),
       dcc.Input(id='input-contrasena', type='password', placeholder='Ingresa tu contraseña'),
       html.Button('Aceptar', id='button'),
       html.Div(id='output')
       ])
        
   @app.callback(
       Output('output', 'children'),
       [Input('button', 'n_clicks')],
       [State('input-usuario', 'value'), State('input-contrasena', 'value')]
       )


   def validar(n_clicks, usuario, contrasena):
       coincidencia = False
       if n_clicks:
           for usuariodB in data:
               if usuariodB['nombre'] == usuario and usuariodB['contraseña'] == contrasena:
                  coincidencia = True
                  #return html.Div('¡Bienvenido, {}!'.format(usuario))
                  break
           if coincidencia:
               return html.Div([html.H1("PROYECTO API SIATA"),dcc.Graph(figure=fig)])
           else:
               return html.Div('Usuario o contraseña incorrectos.')


#           if usuario == 'admin' and contrasena == 'admin':
#               return html.Div('¡Bienvenido, {}!'.format(usuario))
#           else:
#               return html.Div('El usuario o la contraseña son incorrectos.')


'''
app = dash.Dash()
#primero verificamos que pase una pagina de validación
app.layout = html.Div([
    html.H3('Iniciar Sesión'),
    html.Label('Usuario'),
    dcc.Input(id='input-usuari', type='text', placeholder='Ingresa tu usuario'),
    html.Label('Contraseña'),
    dcc.Input(id='input-contrasena', type='password', placeholder='Ingresa tu contraseña'),
    html.Button('Aceptar', id='button'),
    html.Div(id='output')
    ])

@app.callback(
    Output('output', 'children'),
    [Input('button', 'n_clicks')],
    [State('input-usuari', 'value'), State('input-contrasena', 'value')]
    )


def validar(n_clicks, usuario, contrasena):
    if n_clicks:
        if usuario == 'admin' and contrasena == 'admin':
            return html.Div('¡Bienvenido, {}!'.format(usuario))
        else:
            return html.Div('El usuario o la contraseña son incorrectos.')

'''
#app.layout = html.Div([
#	       html.H1("PROYECTO API SIATA"),
#	       dcc.Graph(figure=fig)
#	       ])


app.run_server(host='0.0.0.0',port=5010)
