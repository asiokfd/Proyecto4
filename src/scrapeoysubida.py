from selenium import webdriver
from pymongo import MongoClient
import requests
from unidecode import unidecode


def porparrafos(url, xpath):
    """
    Función que recibe como parámetro una url y el xpath del body de un texto, y lo separa por párrafos en tanto esté separado 
    en el html original mediante tags "p". El escrapeo se hace mediante selenium. También aplica unidecode al resultado
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.get (url)
    discurso=driver.find_element_by_xpath (xpath)
    parrafos=[]
    for p in discurso.find_elements_by_tag_name ("p"):
        parrafos.append (unidecode ((p).text))
    return parrafos



def preparando_parrafos (lista, nombre, partido, tipo, keywords, año):
    """ 
    Función ad hoc para preparar los datos para introducirlos en nuestra api. Toma como parámetros una lista de textos, y los elementos
    necesarios para utilizar la api, nombre, partido, tipo, keywords y año. Nos devolverá una lista de diccionarios habiendo añadido los
    parámetros a cada texto.
    """
    lista=[{"Texto" : lista[i],
     "Nombre" : nombre,
     "Partido" : [partido],
     "Tipo": tipo,
     "Keywords": [keywords],
     "Año": año
     
     
     
     } for i in range (1, (len (lista)))]
    return lista




def query_post_pa_discursos (lista, urlm):
    """
    Función ad hoc para introducir datos en nuestra api. Toma como parámetros una lista de diccionarios y la url adecuada para 
    agregar datos y los añade 1 a 1
    """
    for i in range (0, len (lista)):
            requests.post (urlm, data=lista[i])