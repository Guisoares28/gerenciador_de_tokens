from flask import Blueprint, request, jsonify
from service.cliente_service import cadastro_cliente
from service.cliente_service import login

clientes_bp = Blueprint('clientes', __name__, url_prefix='/clientes')

@clientes_bp.route('/cadastro', methods = ['POST'])
def cadastro_route():
    data = request.get_json()
    nome = data.get('nome')
    email = data.get('email')
    senha = data.get('senha')

    cadastro_cliente(nome, email, senha)
    return jsonify({"Message":"Cliente cadastrado com sucesso"})

@clientes_bp.route('/login', methods = ['POST'])
def login_route():
    data = request.get_json()
    email = data.get('email')
    senha = data.get('senha')

    token = login(email=email, senha=senha)

    return jsonify({"token": token})