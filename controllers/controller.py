from flask import Blueprint, request, jsonify, render_template
from models.perro import Perro
from models.gato import Gato
from models.huron import Huron
from models.boa_constrictor import Boa_Constrictor

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template("index.html")

# Controlador para manejar la consulta del formulario
@main.route('/consulta', methods=['POST'])
def consulta_animal():
    tipo = request.form['tipo']
    
    if tipo.lower() == "gato":
        animal = Gato()
    elif tipo.lower() == "perro":
        animal = Perro()
    elif tipo.lower() == "huron":
        animal = Huron()
    elif tipo.lower() == "boa":
        animal = Boa_Constrictor()
    else:
        return jsonify({"error": "Tipo de animal no reconocido"}), 404
    
    return render_template('animal.html', sonido=animal.sound, especie=animal.species)
# Controlador para peticiones Postman o URL
@main.route('/animal/<tipo>', methods=["GET"])
def get_animal(tipo):
    if request.method == 'GET':
        if tipo.lower() == "gato":
            animal = Gato()
        elif tipo.lower() == "perro":
            animal = Perro()
        elif tipo.lower() == "huron":
            animal = Huron()
        elif tipo.lower() == "boa":
            animal = Boa_Constrictor()
        else:
            return jsonify({"error": "Tipo de animal no reconocido"}), 404

    return jsonify({"Animal": animal.species, "Sonido": animal.sound})


