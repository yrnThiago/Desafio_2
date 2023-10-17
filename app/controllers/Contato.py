from app.services.Contato import ContatoService
from app.repositories.Contato import ContatoRepository
from app.utils.Contato import get_body
from flask import jsonify, redirect, url_for, make_response

contato_repository = ContatoRepository()
contato_service = ContatoService(contato_repository)


class ContatoController:
    @staticmethod
    def add(request):
        if request.method == "POST":
            if request.form:
                email = request.form.get("email")
                assunto = request.form.get("assunto")
                descricao = request.form.get("descricao")

                if len(email) >= 5 and len(assunto) >= 5 and len(descricao) >= 5:
                    new_contact = contato_service.add(email, assunto, descricao)

                    return redirect(url_for("contato.contato"))

                return make_response(jsonify(mensagem="Email, Assunto e Descrição são obrigatórios!"))

            if request.json:
                email = request.json.get("email")
                assunto = request.json.get("assunto")
                descricao = request.json.get("descricao")

                if not email or not assunto or not descricao:
                    return make_response(jsonify(mensagem="Email, Assunto e Descrição são obrigatórios!"))

                new_contact = contato_service.add(email, assunto, descricao)
                new_contact = get_body(new_contact)

                return make_response(jsonify(mensagem="Contato adicionado com sucesso!", dados=new_contact), 201)

    @staticmethod
    def get_many():
        return contato_service.get_many()

    @staticmethod
    def get_by_id(contact_id):
        contact = contato_service.get_by_id(contact_id)
        if contact is None: return make_response(jsonify(mensagem=f"Contato com id {contact_id} não encontrado!"))

        contact = get_body(contact)

        return make_response(jsonify(contact))

    @staticmethod
    def update_by_id(request, contact_id):
        contact = contato_service.get_by_id(contact_id)
        if contact is None: return make_response(jsonify(mensagem=f"Contato com id {contact_id} não encontrado!"))

        if request.method == "PUT":
            new_body = request.json
            contact_to_update = contato_service.update_by_id(contact_id, new_body)
            contact_to_update = get_body(contact_to_update)

            return make_response(
                jsonify(mensagem=f"Contato {contact_id} atualizado com sucesso!", dados=contact_to_update))

        elif request.method == "GET":
            new_body = {"email": "testemailASDSAD@email.com", "assunto": "assunto teste 5", "descricao": "descricao teste 5"}
            contact_to_update = contato_service.update_by_id(contact_id, new_body)
            contact_to_update = get_body(contact_to_update)

            return redirect(url_for("contato.contato"))

    @staticmethod
    def delete_by_id(request, contact_id):
        contact = contato_service.get_by_id(contact_id)
        if contact is None: return make_response(jsonify(mensagem=f"Contato com id {contact_id} não encontrado!"))

        if request.method == "DELETE":
            contact_to_delete = contato_service.delete_by_id(contact_id)
            contact_to_delete = get_body(contact_to_delete)

            return make_response(jsonify(mensagem=f"Contato {contact_id} apagado com sucesso!",
                                             dados=contact_to_delete))

        elif request.method == "GET":
            if contact:
                contato_service.delete_by_id(contact_id)

            return redirect(url_for("contato.contato"))
