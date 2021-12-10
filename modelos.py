from pydantic import BaseModel

class peliculas(BaseModel):
  id:int
  nombre:str
  fecha:str
  comentario:str

  