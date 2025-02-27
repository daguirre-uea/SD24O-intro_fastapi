from fastapi import FastAPI
from bd_biblioteca import libros
from bd_biblioteca import usuarios
from pydantic import BaseModel
from typing import Optional #Para usar el tipo de dato None en FastAPI

app = FastAPI()

#Metodo: GET
#URL; '/'
@app.get('/')
def bienvenida():
    print("Atendiendo GET / ")
    respuesta = {"mensaje": "Bienvenido"}
    return respuesta

# EJERCICIO 1
# (1 puntos) Metodo Get
# Devuelva la lista de usuarios

# EJERCICIO 2
#(1 puntos) Metodo GET
# Devuelve los prestamos del usuario con id = id 

# EJERCICIO 3
#(1 puntos) Metodo DELETE
# Borra el prestamo con id = id 

# Para los ejercicios 4 y 5, se debe crear las clases para los esquemas de usuario y libro

# EJERCICIO 4
# (1.5 puntos) Metodo POST
# Inserta un nuevo usuario
# Este método usa parámetros de cuerpo (viajan en el cuerpo del mensaje HTTP)

# EJERCICIO 5
# (1.5 punto) Método PUT 
# Actualiza la información de un libro con id = id
# Este método usa parámetros de cuerpo y de ruta