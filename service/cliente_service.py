from flask import jsonify

from models.clientModel import Cliente
from app import db
from email_validator import validate_email , EmailNotValidError
from werkzeug.security import generate_password_hash


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


