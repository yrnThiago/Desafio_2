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

    def adicionar(self):
        db.session.add(self)
        db.session.commit()

    def update(self, new_contact: dict):
        self.email = new_contact.get("email")
        self.assunto = new_contact.get("assunto")
        self.descricao = new_contact.get("descricao")

        db.session.commit()

    def apagar(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all():
        contatos = [
            {"id": contato.id, "email": contato.email, "assunto": contato.assunto, "descricao": contato.descricao} for contato in Contato.query.all()
        ]

        return contatos

