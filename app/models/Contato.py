from app import db


class Contato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    assunto = db.Column(db.String(120), unique=False, nullable=False)
    descricao = db.Column(db.String(120), unique=False, nullable=False)

    def __init__(self, email, assunto, descricao):
        self.email = email
        self.assunto = assunto
        self.descricao = descricao
