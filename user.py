from fastapi import APIRouter
from modelos import *
from typing import Optional
import database

user = APIRouter()


@user.get("/")
def inicio():
  return "mi trabajo final"


@user.post("/agregar/peliculas",tags=["Peliculas"])
def agregar_peliculas(per:peliculas):
  database.guardarDatos(per)
  return {"msg":"Datos guardados"}  

@user.put("/actualizar/peliculas",tags=["Peliculas"])
def actualizar_peliculas(per:peliculas):
  database.actualizarDatos(per)
  return {"msg":"Datos Actualizados"} 

@user.get("/listar/datos",tags=["Peliculas"])
def listardatos():
  tmp = database.cargarDatos()
  return tmp  

@user.delete("/Eliminar/peliculas",tags=["Peliculas"])
def eliminar_peliculas(per:peliculas):
  database.eliminarDatos(per)
  return {"msg":"Datos eliminados"}   