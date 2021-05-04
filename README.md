## Proyecto de creaci&oacute;n de api y an&aacute;lisis del sentimiento:
En este proyecto lo que vamos a hacer es crear una api y conectarla a una base de datos, en mi caso con MongoDb, despu&eacute;s a&ntilde;adiremos algunos datos y finalmente haremos un an&aacutelisis del sentimiento de nuestros datos.

## Paso 1 " Mi primera api :)":

Desde Vscode y a trav&eacute;s de flask hemos creado una sencilla api que nos conecta con nuestro MongoDb, y hemos listado una serie de querys para que poder extraer datos de ella.

### &#191;C&oacute;mo Funciona?

#### M&eacute;todo @POST para agregar datos:
Endpoint
    
    - //ntexto
    - A este endpoint le tenemos que agregar nuestros datos en forma de diccionario que coincidan con los par&aacute;metros siguientes:
- @Texto: aqu&iacute; a&ntilde;adiremos el texto que queremos incluir en nuestra base de datos
- @Nombre: el nombre del autor, cuanto m&aacute;s completo mejor
- @partido: su filicaci&oacute;n pol&iacute;tica, se recomienda el uso de siglas en may&uacute;sculas
- @tipo: el tipo de texto
- @claves: palabras claves que puedan facilitar su localizaci&oacute;n

#### M&eacute;todo @GET para pedir datos:
Endpoints

    - "/texto/nombre=<name>", "/texto/fecha=<fecha>", "/texto/tipo=<tipo>"...
    - Estos endpoint devolver&aacute;n todos los datos de esas condiciones
- ejemplo: url= "http://localhost:5000/texto/"
- query= "nombre= Aznar"

- requests.get (url + query), nos devolver&aacute; todos los textos de Aznar

        - &#191;Quieres usar dos?
        - "/texto/nombre=<name>/tipo=<tipo>"
- Pues los usamos. No disponible con todas las b&uacute;squedas, pero si con las necesarias ;)

 - Por ultimo tenemos un endpoint para buscar por rango de fechas.
       
       - "rango/nombre=<nombre>/fecha1=<fecha1>/fecha2=<fecha2>"
 
## Paso 2 Llenando nuestra base de datos:
    
Primero he conseguido los datos scrapeando algunas p&aacute;ginas y despu&eacute;s mediante los he cargado en la base de datos a trav&eacute;s de nuestra api

## Paso 3 An&aacute;lisis del sentimiento:
    
He extraido los datos de la api y posteriormente he realizado un an&aacute;lisis con el uso de la libreria sentiment_analysis_spanish


### Contenido y estructura:
- Archivo yml con el entorno y un requirements con las librer&iacuteas instaladas
- Archivo gitignore con los documentos a ignorar.
- Este Readme
- Ejecutable con la api
- Carpeta Tools con las funciones utilizadas por la api
- Carpeta Config con la configuraci&oacute;n inicial de la api
- Carpeta src con 2 jupyters con el proceso de carga de datos y an&aacute;lisis de sentimiento y 2    ejecutables de python con las funciones utilizadas
    
    
### Recursos y documentación
- [pymongo](https://pymongo.readthedocs.io/en/stable/)
- [sy, os](https://docs.python.org/3/library/sys.html)
- [dotenv](https://pypi.org/project/python-dotenv/)
- [flask](https://flask.palletsprojects.com/en/1.1.x/) 
- [jsonify](https://www.kite.com/python/docs/flask.jsonify)
- [json](https://docs.python.org/3/library/json.html)
- [markdown.extensions.fenced_code](https://python-markdown.github.io/extensions/)
- [pandas](https://pandas.pydata.org/docs/)
- [selenium](https://www.selenium.dev/documentation/en/)
- [seaborn](https://seaborn.pydata.org/)
- [requests](https://docs.python-requests.org/en/master/)
- [TextBlob](https://textblob.readthedocs.io/en/dev/)
- [googletrans](https://py-googletrans.readthedocs.io/en/latest/)
- [goslate](https://pypi.org/project/goslate/)
- [sentiment_analysis_spanish](https://pypi.org/project/sentiment-analysis-spanish/)
- [unidecode]( https://pypi.org/project/Unidecode/)
-[Ras class](https://github.com/Ironhack-Data-Madrid-Marzo-2021/Classroom-Materials-FT/tree/main/special_apis)
- [Fer class](https://github.com/breogann/nlp)
- [Solucionador de problemas](https://stackoverflow.com/)

    
