from email_validator import EmailNotValidError
from flask import jsonify


def init_error_handler(app):

    @app.errorhandler(EmailNotValidError)
    def handle_email_not_valid(error):
        return jsonify({
            'Erro': 'Email inválido',
            'Solução':'Informe um Email válido exemplo: emailvalido@gmail.com'
        }), 400