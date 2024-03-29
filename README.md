# Pràctica de CRUD M07

Pràctica de CRUD (Create, Read, Update, Delete) utilitzant FastApi i MongoDB.

## Objectius

- Aprender a utilizar FastApi
- Aprender a realizar consultas con MongoDB
- CRUd Python
- Consultas query parameters

## Pràctica

1. Crear l'entorn virtual: `py -m venv nomDelEntorn`
2. Instal·lar els paquets necessaris amd `pip install`
3. Crear una bases de dades amb MongoDB i tingui una colecció que es digui films.
4. Fer el CRUD de films: 
    - getAllFilms: retorna la llista de totes les pel·lícules.
    - getFilmById(id): retorna una pel·lícula segons l'id.
    - insertFilm(filmInsert): insertar una pel·lícula a la BD.
    - updateFilm(id, film): permet editar una pel·lícula. 
    - deleteFilm(id): permet eliminar una pel·lícula. 
    - getFilmByGenre(genre: str): retorna llista segons el gènere específicat
    - getLimitedFilms(userLimit): retorna una llista d’objectes json segons el límit definit en el query parameter.
    - getFilmByFieldOrd(field: str , order: str): retorna una llista json ordenada ascendent o descendent segons el camp de field.

### Harpreet Kaur
