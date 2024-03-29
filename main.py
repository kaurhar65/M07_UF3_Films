from db import filmDB
from model.film import Film
from fastapi import FastAPI
from typing import Union

app = FastAPI()

# Trucada a les funciones de CRUD que es troben en el fitxer filmDB

#GETS
@app.get("/films")
def getAllFilms():
    return filmDB.getAllFilms()

@app.get("/films/{id}")
def getFilmById(id):
    return filmDB.getFilmById(id)

@app.get("/filmList/{genre}")
def getFilmByGenre(genre: str):
    return filmDB.getFilmByGenre(genre)

@app.get("/filmsLimit")
def getLimitedFilms(limit: int):
    return filmDB.getLimitedFilms(limit)

@app.get("/filmList/{field}/{order}")
def getFilmByFieldOrd(field: str, order:str):
    return filmDB.getFilmByFieldOrd(field, order)

#POST/INSERT
@app.post("/film/")
def insertFilm(film:Film):
    return filmDB.insertFilm(film)

#UPDATE/PUT 
@app.put("/film/{id}")
def updateFilm(id, film:Film):
    return filmDB.updateFilm(id, film)

#DELETE
@app.delete("/film/{id}")
def deleteFilm(id):
    return filmDB.deleteFilm(id)

