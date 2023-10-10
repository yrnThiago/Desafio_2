from app.models.Contato import Contato
from app import db


class ContatoRepository:
    @staticmethod
    def add(email, assunto, descricao):
        new_contact = Contato(email, assunto, descricao)
        db.session.add(new_contact)
        db.session.commit()

        return new_contact

    @staticmethod
    def get_many():
        return Contato.query.all()

    @staticmethod
    def get_by_id(contact_id: int):
        return Contato.query.filter_by(id=contact_id).first()

    @staticmethod
    def update_by_id(contact, new_body):
        contact.email = new_body.get("email")
        contact.assunto = new_body.get("assunto")
        contact.descricao = new_body.get("descricao")

        db.session.commit()

        return contact

    @staticmethod
    def delete_by_id(contact):
        db.session.delete(contact)
        db.session.commit()

        return contact
