from ..services.Contato import ContatoService
from ..repositories.Contato import ContatoRepository
from flask import jsonify, redirect, url_for, make_response

contato_repository = ContatoRepository()
contato_service = ContatoService(contato_repository)


class ContatoController:
    @staticmethod
    def add(request):
        if request.method == "POST":
            email = request.form.get("email")
            assunto = request.form.get("assunto")
            descricao = request.form.get("descricao")

            if email is not None:
                new_contact = contato_service.add(email, assunto, descricao)

                return redirect(url_for("contato.contato"))

            email = request.json.get("email")
            assunto = request.json.get("assunto")
            descricao = request.json.get("descricao")

            new_contact = contato_service.add(email, assunto, descricao)
            new_contact = {"id": new_contact.id, "email": new_contact.email, "assunto": new_contact.assunto,
                       "descricao": new_contact.descricao}

            return make_response(jsonify(mensagem="Contato adicionado com sucesso!", dados=new_contact), 201)

    @staticmethod
    def get_many():
        return contato_service.get_many()

    @staticmethod
    def get_by_id(contact_id):
        contact = contato_service.get_by_id(contact_id)
        if contact:
            contact = {"id": contact.id, "email": contact.email, "assunto": contact.assunto,
                       "descricao": contact.descricao}

            return make_response(jsonify(contact))

        return make_response(jsonify(mensagem=f"Contato com id {contact_id} não encontrado!"))

    @staticmethod
    def update_by_id(request, contact_id):
        contact = contato_service.get_by_id(contact_id)
        new_body = request.json
        if request.method == "PUT":
            if contact:
                contact_to_update = contato_service.update_by_id(contact_id, new_body)
                contact_to_update = {"email": contact_to_update.email, "assunto": contact_to_update.assunto,
                                     "descricao": contact_to_update.descricao}

                return make_response(
                    jsonify(mensagem=f"Contato {contact_id} atualizado com sucesso!", dados=contact_to_update))

            return make_response(jsonify(mensagem=f"Contato com id {contact_id} não encontrado!"))

        elif request.method == "GET":
            if contact:
                contato_service.delete_by_id(contact_id)

            return redirect(url_for("contato.contato"))

    @staticmethod
    def delete_by_id(request, contact_id):
        contact = ContatoController.get_by_id(contact_id)
        if request.method == "DELETE":
            if contact:
                contact_to_delete = contato_service.delete_by_id(contact_id)
                contact_to_delete = {"id": contact_to_delete.id, "email": contact_to_delete.email,
                                     "assunto": contact_to_delete.assunto, "descricao": contact_to_delete.descricao}

                return make_response(jsonify(mensagem=f"Contato {contact_id} apagado com sucesso!",
                                             dados=contact_to_delete))

            return make_response(jsonify(mensagem=f"Contato com id {contact_id} não encontrado!"))

        elif request.method == "GET":
            if contact:
                contato_service.delete_by_id(contact_id)

            return redirect(url_for("contato.contato"))
