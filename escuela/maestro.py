from flask import Flask, jsonify, request, Blueprint
from flask_mysqldb import MySQL
from flask_cors import CORS
 
from config import config

maestros_bp=Blueprint('maestros',__name__, url_prefix='/api/maestros')

def fila_a_diccionario(cursor, fila):
    columnas=[columna[0]] for columna in cursor.description
    return dict(zip(columnas,filas))

@maestros_bp.route("/maeestro",methods=['GET'])
def listar_maestros():
    cursor =None
 
