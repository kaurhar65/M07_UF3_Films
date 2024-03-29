from pydantic import BaseModel
from datetime import date

#Definició dels camps de la base de dades Films
class Film(BaseModel):
        id:str
        title:str
        director:str
        year:int
        genre:str
        rating:int 
        country:str
        created_at:date
        updated_at:date
