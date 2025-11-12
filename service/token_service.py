from datetime import timedelta

from flask_jwt_extended import create_access_token


def gerar_token(user):
    return create_access_token(
        identity = user.email,
        expires_delta = timedelta(days=7),
        additional_claims={'id': user.id, 'owner': 'gerenciaToken'}
    )