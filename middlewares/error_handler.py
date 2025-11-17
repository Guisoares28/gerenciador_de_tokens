from email_validator import EmailNotValidError
from flask import jsonify

from exceptions.my_exceptions import LoginInvalidoException, TokenInvalidoException, QuantidadeExcedidaException


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
        }),401

    @app.errorhandler(TokenInvalidoException)
    def handle_invalid_token(error):
        return jsonify({
            'Erro': 'Token inválido',
            'Solução': 'Informe um token válido'
        })

    @app.errorhandler(QuantidadeExcedidaException)
    def handle_quantidade_invalid(error):
        return jsonify({
            'Erro': 'Quantidade de tokens gerados excedido Máximo 3 tokens',
            'Solução': 'Delete algum token que não esteja em uso, ou pague o plano adicional'
        })

    @app.errorhandler(TokenInvalidoException)
    def handle_token_not_found(error):
        return jsonify({
            'Erro': 'Nenhum token encontrado para o usuário informado.',
            'Solução': 'Gere um token para sua aplicação.'})