from models.token_model import Token
from service.token_service import gerar_token

from exceptions.my_exceptions import LoginInvalidoException, UserNotFoundException, TokenInvalidoException
from models.clientModel import Cliente
from app import db
from email_validator import validate_email , EmailNotValidError
from werkzeug.security import generate_password_hash, check_password_hash


def validar_email(email):
    try:
        email_valid = validate_email(email, check_deliverability=True)
        return email_valid.normalized
    except EmailNotValidError:
        raise EmailNotValidError()


def cadastro_cliente(nome, email, senha):

    validar_email(email=email)

    senha_hash = generate_password_hash(senha)

    cliente = Cliente(
        nome = nome,
        email = email,
        senha = senha_hash
    )
    db.session.add(cliente)
    db.session.commit()

def login(email, senha):
    cliente = Cliente.query.filter_by(email = email).first()

    if not cliente:
        raise UserNotFoundException()

    if not check_password_hash(cliente.senha, senha):
        raise LoginInvalidoException()

    token = gerar_token(cliente)

    return token

def pegar_tokens(email):
    tokens = Token.query.filter_by(email = email).all()
    if tokens.__len__() == 0:
        raise TokenInvalidoException()

    return tokens




