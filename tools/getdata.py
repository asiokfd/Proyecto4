from config.configuration import db, collection

# consultas simples (6)
def texto():
    """
    Función que devuelve toda la coleccion
    """
    query = {"Texto": {"$exists": True}}
    textos = list(collection.find(query,{"_id": 0}))
    if len (textos)==0:
        return ("su búsqueda no ha dado ningún resultado")
    else:
        return textos



def textoxnombre(name):
    """
    Función que devuelve todos los textos de una persona
    """
    query = {"Nombre": {"$regex" : f"{name}"}}
    textos = list(collection.find(query,{"_id": 0}))
    if len (textos)==0:
        return ("su búsqueda no ha dado ningún resultado")
    else:
        return textos

def textoxfecha(fecha):
    """
    Función que devuelve todas los textos de un año
    """
    query = {"Año": f"{fecha}"}
    textos = list(collection.find(query,{"_id": 0}))
    if len (textos)==0:
        return ("su búsqueda no ha dado ningún resultado")
    else:
        return textos

def textoxtipo(tipo):
    """
    Función que devuelve todas los textos de un tipo determinado
    """
    query = {"Tipo": f"{tipo}"}
    textos = list(collection.find(query,{"_id": 0}))
    if len (textos)==0:
        return ("su búsqueda no ha dado ningún resultado")
    else:
        return textos

def textoxclave(clave):
    """
    Función que devuelve todas los textos que tengan esa keyword
    """
    query = {"Keywords": f"{clave}"}
    textos = list(collection.find(query,{"_id": 0}))
    if len (textos)==0:
        return ("su búsqueda no ha dado ningún resultado")
    else:
        return textos

def textoxpartido(partido):
    """
    Función que devuelve todas los textos de un partido
    """
    query = {"Partido": f"{partido}"}
    textos = list(collection.find(query,{"_id": 0}))
    if len (textos)==0:
        return ("su búsqueda no ha dado ningún resultado")
    else:
        return textos

#consultas con filtro (5)

def textoxnombreytipo(name, tipo):
    """
    Función que devuelve todas los textos de una persona y un tipo determinado
    """
    query = {"Nombre": {"$regex" : f"{name}"}}
    query2= {"Tipo": f"{tipo}"}
    textos = list ((collection.find (({ "$and" : [query, query2 ]}) ,  {"_id": 0})))
    
    if len (textos)==0:
        return ("su búsqueda no ha dado ningún resultado")
    else:
        return textos

def textoxnombreyclave(name, clave):
    """
    Función que devuelve todas los textos de una persona y un tipo determinado
    """
    query = {"Nombre": {"$regex" : f"{name}"}}
    query2= {"Keywords": f"{clave}"}
    textos = list ((collection.find (({ "$and" : [query, query2 ]}) ,  {"_id": 0})))
    
    if len (textos)==0:
        return ("su búsqueda no ha dado ningún resultado")
    else:
        return textos

def textoxnombreyfecha(name, fecha):
    """
    Función que devuelve todas los textos de una persona y un año
    """
    query = {"Nombre": {"$regex" : f"{name}"}}
    query2= {"Año": f"{fecha}"}
    textos = list ((collection.find (({ "$and" : [query, query2 ]}) ,  {"_id": 0})))
    
    if len (textos)==0:
        return ("su búsqueda no ha dado ningún resultado")
    else:
        return textos

def textoxclaveyfecha(clave, fecha):
    """
    Función que devuelve todas los textos de una palabra clave y una fecha
    """
    query = {"Keywords": f"{clave}"}
    query2= {"Año": f"{fecha}"}
    textos = list ((collection.find (({ "$and" : [query, query2 ]}) ,  {"_id": 0})))
    
    if len (textos)==0:
        return ("su búsqueda no ha dado ningún resultado")
    else:
        return textos

def textoxclaveypartido(clave, partido):
    """
    Función que devuelve todas los textos de una palabra clave y un partido
    """
    query = {"Keywords": f"{clave}"}
    query2= {"Partido": f"{partido}"}
    textos = list ((collection.find (({ "$and" : [query, query2 ]}) ,  {"_id": 0})))
    
    if len (textos)==0:
        return ("su búsqueda no ha dado ningún resultado")
    else:
        return textos

def textosxrango (nombre, fecha1, fecha2):
    """
    Función que devuelve los textos de una persona en un rango de años
    """

    query = {"Nombre": {"$regex" : f"{nombre}"}}
    query2 = {"Año": {"$gte": f"{fecha1}"}}
    query3 = {"Año": {"$lte": f"{fecha2}"}}

    textos= list((collection.find (({"$and": [query, query2, query3]}), {"_id": 0})))

    if len (textos)==0:
        return ("su búsqueda no ha dado ningún resultado")
    else:
        return textos


