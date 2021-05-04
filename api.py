from flask import Flask, request
from flask import jsonify
import json
import markdown.extensions.fenced_code
import tools.getdata as get
import tools.postdata as post
from config.configuration import db, collection




app = Flask(__name__)


@app.route("/")
def index():
    readme_file = open("Readme.md", "r")
    md_template = markdown.markdown( 
        readme_file.read(), extensions=["fenced_code"]
    )
    return md_template

# consultas simples (6)
@app.route("/texto") #todos los textos
def texto():
    texto = get.texto()
    return jsonify (texto)



@app.route("/texto/nombre=<name>") #todos los textos de name
def textonombre(name):
    textos = get.textoxnombre (name)
    return jsonify(textos)

@app.route("/texto/fecha=<fecha>") #todos los textos de ese año
def textofecha(fecha):
    textos = get.textoxfecha(fecha)
    return jsonify(textos)

@app.route("/texto/tipo=<tipo>") #todos los textos de ese tipo
def textotipo(tipo):
    textos = get.textoxtipo(tipo)
    return jsonify(textos)

@app.route("/texto/clave=<clave>") #todos los textos que contengan esa clave 
def textoclave(clave):
    textos = get.textoxclave(clave)
    return jsonify(textos)

@app.route("/texto/partido=<partido>") #todos los textos de ese partido
def textopartido(partido):
    textos = get.textoxpartido(partido)
    return jsonify(textos)

#consultas con filtro (5):

@app.route("/texto/nombre=<name>/tipo=<tipo>") #todos los textos de 1 name y 1 tipo
def textonombretipo(name, tipo):
    textos = get.textoxnombreytipo(name, tipo)
    return jsonify(textos)

@app.route("/texto/nombre=<name>/clave=<clave>") #todos los textos de 1 name y 1 palabra clave
def textonombreclave(name, clave):
    textos = get.textoxnombreyclave(name, clave)
    return jsonify(textos)

@app.route("/texto/nombre=<name>/fecha=<fecha>") #todos los textos de 1 name y 1 año
def textonombrefecha(name, fecha):
    textos = get.textoxnombreyfecha(name, fecha)
    return jsonify(textos)

@app.route("/texto/clave=<clave>/fecha=<fecha>") #todos los textos de 1 palabra clave y 1 año
def textoclavefecha(fecha, clave):
    textos = get.textoxclaveyfecha(clave, fecha)
    return jsonify (textos)

@app.route("/texto/clave=<clave>/partido=<partido>") #todos los textos de 1 palabra clave y 1 partido
def textoclavepartido(clave, partido):
    textos = get.textoxclaveypartido(clave, partido)
    return jsonify(textos)

@app.route ("/rango/nombre=<nombre>/fecha1=<fecha1>/fecha2=<fecha2>") #todos los textos de ese nombre y en ese rango
def rangofechas(nombre, fecha1, fecha2):
    textos= get.textosxrango (nombre, fecha1, fecha2)
    return jsonify (textos)








@app.route("/ntexto", methods=["POST"])
def insertartexto():
    texto = request.form.get("Texto")
    nombre = request.form.get("Nombre")
    partido = request.form.get("Partido")
    tipo= request.form.get ("Tipo")
    claves = ("Keywords")
    año = request.form.get ("Año")


    post.insertartexto(texto, nombre, partido, tipo, claves, año)
    return "Se ha introducido el mensaje en la base de datos"

@app.route("/ntextos", methods=["POST"])
def insertartextos():
    
    lista = request.form.get ("Texto")
    nombre = request.form.get("Nombre")
    partido = request.form.get("Partido")
    tipo= request.form.get ("Tipo")
    claves = request.form.get ("Keywords")
    año = request.form.get ("Año")

    post.insertartextos(lista, nombre, partido, tipo, claves, año)
    return "Se ha introducido el mensaje en la base de datos"












app.run("0.0.0.0", 5000, debug=True)