from sqlalchemy.orm import relationship

from extensions.database import db


class Token(db.Model):

    __tablename__ = 'tokens'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    token = db.Column(db.String(500), unique=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'))

    cliente = relationship("Cliente", back_populates="tokens")
