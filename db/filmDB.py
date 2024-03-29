from db import client
import json
from bson.objectid import ObjectId
from datetime import datetime
import traceback

#TOTES LES FUNCIONES DEL CRUD

current_datetime = datetime.now()

#definició de schema per poder imprimir les dades en formar JSON
def filmSchema(film) -> dict:
    return{"id": str(film["_id"]),
            "title": film["title"],
            "director": film["director"],
            "year": film["year"],
            "genre": film["genre"],
            "rating": film["rating"],
            "country": film["country"],
            "created_at": film["created_at"],
            "updated_at": film["updated_at"]
        }

def filmsSchema(datosFilms)-> dict:
    return[filmSchema(film) for film in datosFilms]

# GET DEL TOTES LES PEL·LÍCULES 
def getAllFilms():
    filmsArray = []
    try:
        conn = client.database()
        collection = conn.films
        films = collection.find()
        filmsArray = filmsSchema(films)
        return {"status": 1, "data": filmsArray}
            
    except Exception as e:
        traceback.print_exc()
        return {"status": -1, "Error conexión": f'Ha habido un error: {e}'}

#GET DE UNA PELI SEGONS L'ID 
def getFilmById(id):
    try:
        conn = client.database()
        collection = conn.films
        film = collection.find_one({"_id": ObjectId(id)})
        filmData = filmSchema(film)
        return {"status": 1, "data": filmData}
            
    except Exception as e:
        traceback.print_exc()
        return {"status": -1, "Error conexión": f'Ha habido un error: {e}'}

#INSERTAR UNA PEL·LÍCULA A LA BD
def insertFilm(filmInsert):    
    try:
        filmToInsert = {
            "title": filmInsert.title,
            "director": filmInsert.director,
            "year": filmInsert.year,
            "genre": filmInsert.genre,
            "rating": filmInsert.rating,
            "country": filmInsert.country,
            "created_at": current_datetime,
            "updated_at": current_datetime
        }

        conn = client.database()
        collection = conn.films
        insertedFilm = collection.insert_one(filmToInsert)

        if insertedFilm.inserted_id:
            return {"status": 1, "message": "Film inserted successfully", "film_id": str(insertedFilm.inserted_id)}
        else:
            return {"status": -1, "message": "Failed to insert film"}

    except Exception as e:
        traceback.print_exc()
        return {"status": -1, "Error conexión": f'Ha habido un error: {e}'}
    
# EDITAR UNA PEL·LÍCULA DONAT UN ID
def updateFilm(id, film):
    try:
        infoToUpdate = {
            "$set":{
                "title": film.title,
                "director": film.director,
                "year": film.year,
                "genre": film.genre,
                "rating": film.rating,
                "country": film.country,
                "updated_at": current_datetime
            }            
        }

        conn = client.database()
        collection = conn.films
        
        updatedFilm = collection.update_one({"_id": ObjectId(id)},infoToUpdate)
        if updatedFilm.modified_count == 1:
            return {"status": 1, "message": "Film updated successfully"}
        else:
            return {"status": -1, "message": "Failed to update film"}
    
    except Exception as e:
        traceback.print_exc()
        return {"status": -1, "Error conexión": f'Ha habido un error: {e}'}

# ELIMINAR UNA PEL·LÍCULA 
def deleteFilm(id):
    try:
        conn = client.database()
        collection = conn.films
        deleteResult = collection.delete_one({"_id": ObjectId(id)})

        if deleteResult.deleted_count == 1:
            return {"status": 1, "message": "Film deleted successfully"}
        else:
            return {"status": 0, "message": "No film found with the given ID"}

    except Exception as e:
        traceback.print_exc()
        return {"status": -1, "Error conexión": f'Ha habido un error: {e}'}

# GET LLISTA DE LES PEL·LÍCULES SEGONS EL GÈNERE
def getFilmByGenre(genre: str):
    try:
        conn = client.database()
        collection = conn.films
        films = collection.find({"genre": genre})
        genreArray = filmsSchema(films)
        if genreArray:
            return {"status": 1, "data": genreArray}
        else:
            return {"status": 0, "message": f"No se encontraron películas del género '{genre}'"}
            
    except Exception as e:
        traceback.print_exc()
        return {"status": -1, "Error conexión": f'Ha habido un error: {e}'}

# LLISTA LIMITADA DE LES PEL·LÍCULES 
def getLimitedFilms(userLimit):
    try:
        conn = client.database()
        collection = conn.films
        films = collection.find().limit(userLimit)
        return {"status": 1, "data": filmsSchema(films)}
    
    except Exception as e:
        traceback.print_exc()
        return {"status": -1, "Error conexión": f'Ha habido un error: {e}'}

# LLISTA DE LES PEL·LÍCULES SEGONS EL CAMP I L'ORDRE
def getFilmByFieldOrd(field: str , order: str):    
    try:
        conn = client.database() 
        collection = conn.films
        if order not in ["asc", "desc"]:
            return {"status": -1, "message": "Orden no válida. Utiliza 'asc' o 'desc'."}
        filteredFilms = collection.find().sort(field, 1 if order == "asc" else -1)
        return {"status": 1, "data": filmsSchema(filteredFilms)}
    
    except Exception as e:
        traceback.print_exc()
        return {"status": -1, "Error conexión": f'Ha habido un error: {e}'}