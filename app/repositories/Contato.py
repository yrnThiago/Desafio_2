from app.models.Contato import Contato
from app import db
from sqlalchemy.exc import IntegrityError


class ContatoRepository:
    @staticmethod
    def add(email, assunto, descricao):
        try:
            new_contact = Contato(email, assunto, descricao)
            db.session.add(new_contact)
            db.session.commit()

            return new_contact

        except IntegrityError as ie:
            print(ie)

    @staticmethod
    def get_many():
        return Contato.query.all()

    @staticmethod
    def get_by_id(contact_id: int):
        return Contato.query.filter_by(id=contact_id).first()

    @staticmethod
    def update_by_id(contact, email, assunto, descricao):
        contact.email = email
        contact.assunto = assunto
        contact.descricao = descricao

        db.session.commit()

        return contact

    @staticmethod
    def delete_by_id(contact):
        db.session.delete(contact)
        db.session.commit()

        return contact
