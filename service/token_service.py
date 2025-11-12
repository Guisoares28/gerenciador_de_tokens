from flask_jwt_extended import create_access_token


def gerarToken(user):
    return create_access_token(
        identity = user.email,
        additional_claims={'id': user.id}
    )
