from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt, get_jwt_identity

from service.cliente_service import cadastro_cliente
from service.cliente_service import login
from service.token_service import gerar_token_usuario, pegar_claims

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

@clientes_bp.route('/create/token', methods = ['POST'])
@jwt_required()
def create_token_route():
    data = request.get_json()
    email = get_jwt_identity()
    claims = get_jwt()

    if 'target' in claims:
        return jsonify({'Erro': 'Token Inválido'})

    token = gerar_token_usuario(email, data)
    return jsonify({"token": token})

@clientes_bp.route('/claims', methods = ['POST'])
def recuperar_claims():
    data = request.get_json()
    token = data.get('token')
    claims = pegar_claims(token)
    return jsonify(claims)

