#!/bin/bash

#DOCKER DB
# Ingresar al directorio del DB
cd DB/

# Construir la imagen docker db.py
docker build -t db .

# Contruir y ejecutar el contenedor db
docker run -t -d -p 500:500 --name dockerdb db


#DOCKER API
# Ingresar al directorio del API
cd ../API/

# Construir la imagen docker api.py
docker build -t api .

# Contruir y ejecutar el contenedor api
docker run -t -d -p 5000:5000 --name dockerapi api


#DOCKER FRONT
# Ingresar al directorio del FRONT
cd ../FRONT/

# Construir la imagen docker front.py
docker build -t front .

# Contruir y ejecutar el contenedor front
docker run -t -d -p 5010:5010 --name dockerfront front
