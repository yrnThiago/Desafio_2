from app.repositories.Contato import ContatoRepository


class ContatoService:
    def __init__(self, contato_repository: ContatoRepository):
        self.contato_repository = ContatoRepository

    def add(self, email, assunto, descricao):
        return self.contato_repository.add(email, assunto, descricao)

    def get_many(self):
        return [{"id": contact.id, "email": contact.email, "assunto": contact.assunto, "descricao": contact.descricao}
                for contact in self.contato_repository.get_many()]

    def get_by_id(self, contact_id):
        return self.contato_repository.get_by_id(contact_id)

    def update_by_id(self, contact_id, email, assunto, descricao):
        contact_to_update = self.contato_repository.get_by_id(contact_id)

        return self.contato_repository.update_by_id(contact_to_update, email, assunto, descricao)

    def delete_by_id(self, contact_id):
        contact_to_delete = self.contato_repository.get_by_id(contact_id)

        return self.contato_repository.delete_by_id(contact_to_delete)
