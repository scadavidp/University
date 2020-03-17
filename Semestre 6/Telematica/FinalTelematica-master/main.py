#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, jsonify
from flask_pymongo import PyMongo

from bson.json_util import dumps

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://duvanmongo:123@cluster0-xkkwx.mongodb.net/test?retryWrites=true&w=majority"
mongo = PyMongo(app)

@app.route("/")
def inicio(): 
    return render_template("/inicio.html")
    


@app.route("/login", methods=["POST", "GET"])
def login():

    if request.method == "GET":

        return render_template("/login.html")
        
    else:

        numeroDocumento = request.form["txtNumeroDocumento"]
        contrasena = request.form["pswClave"]
        
        cursor = mongo.db.names.find({"NumeroDocumento": numeroDocumento, "Contraseña": contrasena})

        resultadoConsulta = list(cursor)

        if len(resultadoConsulta) > 0:

            return render_template("/login.html", mensaje="Bienvenido")
        
        return render_template("/login.html", mensaje="Incorrecto")


@app.route("/registroCliente", methods=["POST", "GET"])
def registroCliente():

    if request.method == "GET":

        return render_template("/registro_cliente.html")
        
    else:

        tipoDocumento = request.form["selectTipoDocumento"]
        numeroDocumento = request.form["txtNumeroDocumento"]
        nombres = request.form["txtNombres"]
        apellidos = request.form["txtApellidos"]
        sexo = request.form["radioSexo"]
        edad = request.form["txtEdad"]
        ciudad = request.form["txtCiudad"]
        direccion = request.form["txtDireccion"]
        email = request.form["txtEmail"]
        contrasena = request.form["pswClave"]
        
        documento = {'TipoDocumento':tipoDocumento, 'NumeroDocumento':numeroDocumento, 'Nombres':nombres, 'Apellidos':apellidos, 'Sexo':sexo, 
                'Edad':edad, 'Ciudad':ciudad, 'Dirección':direccion, 'Email':email, 'Contraseña':contrasena}

        mongo.db.names.insert_one(documento)
        
        return render_template("/registro_cliente.html", estado="El cliente se ha registrado satisfactoriamente.")

        
app.run(debug=True)
