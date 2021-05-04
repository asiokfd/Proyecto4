from config.configuration import collection


def insertartexto(texto, nombre, partido, tipo, claves, año):
    dict_insert = {"Texto": texto,
    "Nombre": nombre,
    "Partido": partido,
    "Tipo" : tipo,
    "Keywords" : claves,
    "Año" : año
    }
    collection.insert_one(dict_insert)


def insertartextos(lista, nombre, partido, tipo, claves, año): # esto no he conseguido que me funcione como quiero.
    dict_insert = [{"Texto": lista[i],
    "Nombre": nombre,
    "Partido": partido,
    "Tipo" : tipo,
    "Keywords" : claves,
    "Año" : año
    } for i in range (0, len (lista))]
    collection.insert_many(dict_insert)



    



