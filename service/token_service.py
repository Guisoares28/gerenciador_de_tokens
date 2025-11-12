from datetime import timedelta
from flask_jwt_extended import create_access_token, decode_token

from exceptions.my_exceptions import TokenInvalidoException, QuantidadeExcedidaException
from extensions.database import db
from models.clientModel import Cliente
from models.token_model import Token


def gerar_token(user):
    return create_access_token(
        identity = user.email,
        expires_delta = timedelta(days=7),
        additional_claims={'id': user.id, 'owner': 'gerenciaToken', "bloqueado":True}
    )

def gerar_token_usuario(email, claims):
    cliente = Cliente.query.filter_by(email=email).first()

    if len(cliente.tokens) >= 3:
        raise QuantidadeExcedidaException()

    claims['owner'] = 'gerenciaToken'
    claims['target'] = 'cliente'

    token = create_access_token(
        identity = email,
        additional_claims=claims
    )



    tk = Token(token=token, cliente=cliente)
    db.session.add(tk)
    db.session.commit()

    return token

def pegar_claims(token):

    claims = decode_token(token)

    if('bloqueado' in claims):
        raise TokenInvalidoException()

    return claims
