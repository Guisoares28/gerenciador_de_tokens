from email_validator import EmailNotValidError
from flask import jsonify

from exceptions.my_exceptions import LoginInvalidoException


def init_error_handler(app):

    @app.errorhandler(EmailNotValidError)
    def handle_email_not_valid(error):
        return jsonify({
            'Erro': 'Email inválido',
            'Solução':'Informe um Email válido exemplo: emailvalido@gmail.com'
        }), 400

    @app.errorhandler(LoginInvalidoException)
    def handle_invalid_login(error):
        return jsonify({
            'Erro': 'Email ou Senha inválidos',
            'Solução': 'Informe um Email e Senha válidos'
        })