from flask import Blueprint, request, make_response, redirect, url_for, render_template
import requests

from service.cliente_service import pegar_tokens

views_bp = Blueprint('views', __name__, url_prefix='/view', template_folder="../templates")

url_login = "http://localhost:5000/clientes/login"

@views_bp.route('/login', methods=['POST', 'GET'])
def login_template():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        res = requests.post(url_login, json={
            'email': email,
            'senha': senha
        })

        if res.status_code == 200:
            token = res.json()['token']

            response = make_response(redirect(url_for('index')))
            response.set_cookie('token', token, httponly=True, samesite='Lax')
            return response
        else:
            return render_template('login.html', error='Email ou Senha incorretos')
    return render_template('login.html')

