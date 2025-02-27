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

#Metodo Get
#URL '/libros'
#devuelva la lista de libros
#Query string
@app.get('/libros')
def lista_libros(pagina:int,orden:Optional[str]=None,lote:int=10):
    print("Atendiendo GET '/libros'")
    respuesta = libros
    return respuesta

#Metodo GET
#URL '/libros/{id}'
#devuelve un json
#parametro de ruta id
@app.get('/libros/{id}')
def informacion_libro(id:int):
    print("Atendiendo GET /libros/",id)
    if id >=0 and id <=len(libros)-1:
        respuesta = libros[id]
    else:
        respuesta = {
            "mensaje":"El libro no existe"
        }
    return respuesta

#Metodo DELETE
#URL  'libros/{id}'
#devuelve un mensaje
@app.delete('/libros/{id}')
def borra_libro(id:int):
    print("Atendiendo DELETE /libros/", id)
    if id >=0 and id <=len(libros)-1:
        del libros[id]
    respuesta = {
        "mensaje": "Elemento borrado" 
    }
    return respuesta

# GET '/usuarios'
@app.get('/usuarios')
def lista_usuarios():
    print("Atendiendo GET '/usuarios'")
    respuesta = usuarios
    return respuesta

# GET '/usuarios/{id}'
@app.get('/usuarios/{id}')
def informacion_usuario(id:int):
    print("Atendiendo GET /usuarios/",id)
    if id >=0 and id <=len(usuarios)-1:
        respuesta = usuarios[id]
    else:
        respuesta = {
            "mensaje":"El usuario no existe"
        }
    return respuesta

# Mapear los recursos
class LibroBase(BaseModel):
    titulo:str
    unidades:int=1
    autor:str
    unidades_disponibles:bool=True

class UsuarioBase(BaseModel):
    nombre:str
    direccion:str

#POST '/libros'
#Parametros de cuerpo (viajan en el cuerpo del mensaje HTTP)
@app.post('/libros')
def insertar_libro(libro:LibroBase):
    print("Insertando un nuevo libro")
    libro_nuevo = {}
    libro_nuevo['titulo'] = libro.titulo
    libro_nuevo['unidades'] = libro.unidades
    libro_nuevo['autor'] = libro.autor
    libro_nuevo['unidades_disponible'] = libro.unidades_disponibles
    libro_nuevo['id'] = len(libros)
    libros.append(libro_nuevo)
    return libro_nuevo

#POST '/usuarios'
#Parametros de cuerpo (viajan en el cuerpo del mensaje HTTP)
@app.post('/usuarios')
def insertar_usuario(usuario:UsuarioBase):
    print("Insertando un nuevo usuario")
    usuario_nuevo = {}
    usuario_nuevo['nombre'] = usuario.nombre
    usuario_nuevo['direccion'] = usuario.direccion
    usuario_nuevo['id'] = len(usuarios)
    usuario.append(usuario_nuevo)
    return usuario_nuevo

#PUT '/libros/{id}'
#orden de los parámteros: 1) de ruta, 2) de cuerpo
@app.put('/libros/{id}')
def actualizar_disponibilidad_libro(id:int,libro:LibroBase):
    # libros[id] -> libro de la BD
    # libro -> información actualizada que envio el cliente
    libros[id]['titulo'] = libro.titulo
    libros[id]['autor'] = libro.autor
    libros[id]['unidades'] = libro.unidades
    libros[id]['unidades_disponible'] = libro.unidades_disponibles
    respuesta = {
        "mensaje": "Se actualizo el libro"
    }
    return respuesta
