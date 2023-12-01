from flask import Flask, request, jsonify
from flask import Flask
from flask_cors import CORS
import numpy as np
import sympy as sp

import metodos.biseccion as biseccion

import metodos.punto_fijo as puntofijo



app = Flask(__name__)

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

#biseccion
@app.route('/api/biseccion', methods=['POST'])
def metodobiseccion():
    if request.method == 'POST':
        data = request.json  
        if 'ecuacion' in data:
            ecuacion = data['ecuacion']
            a = data['a']
            b = data['b']
            response=biseccion.bisection_solver(ecuacion,a,b)
            return jsonify({"response":response})
        else:
            return jsonify({'error': 'El campo "texto" es requerido'}), 400
        


@app.route('/api/puntofijo', methods=['POST'])
def metodopuntofijo():
    if request.method == 'POST':
        data = request.json  
        if 'ecuacion' in data:
            ecuacion = data['ecuacion']

            response= puntofijo.punto_fijo_inicio(ecuacion)
            return jsonify({"response": response})
        else:
            return jsonify({'error': 'El campo "texto" es requerido'}), 400
        
        

        





if __name__ == '__main__':
    app.run(debug=True)