from peewee import *
from modelos import *

db = SqliteDatabase('pelicula.db')

class Peliculas(Model):
    nombre = CharField()
    fecha = CharField()
    comentario = TextField()

    class Meta:
        database = db # This model uses the "people.db" database.

db.connect()

db.create_tables([Peliculas])


def guardarDatos(obj:peliculas):
  per = Peliculas()
  per.nombre = obj.nombre
  per.fecha = obj.fecha
  per.comentario = obj.comentario
  per.save()

def cargarDatos():
  peliculass = []
  for per in Peliculas.select().dicts():
    peliculass.append(per)
    return peliculass

def actualizarDatos(obj:peliculas):
  per =Peliculas.get(Peliculas.id == obj.id) 
  per.nombre = obj.nombre
  per.fecha = obj.fecha
  per.comentario = obj.comentario
  per.save()

def eliminarDatos(obj:peliculas):
  qry = Peliculas.delete().where(Peliculas.id == obj.id)
  qry.execute()  
