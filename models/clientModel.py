from sqlalchemy.orm import relationship

from extensions.database import db


class Cliente(db.Model):

    __tablename__ = 'cliente'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    senha = db.Column(db.String(300))

    tokens = relationship('Token', back_populates="cliente", cascade='all, delete-orphan')

