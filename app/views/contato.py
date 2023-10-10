from flask import Blueprint, render_template, make_response, jsonify, request, redirect, url_for
from app.components.base_title_text import base_title_text
from app.components.base_input_text import base_input_text
from app.constants.contato import CONTACT_TEXT, EMAIL_INPUT, ASSUNTO_INPUT, DESCRICAO_INPUT
from app.models.Contato import Contato
from app.controllers.Contato import ContatoController

contato_blueprint = Blueprint('contato', __name__)


@contato_blueprint.route('/contato')
def contato():
    all_contacts = get_many().json
    return render_template("contato.html", contact=base_title_text(CONTACT_TEXT),
                           input_email=base_input_text(EMAIL_INPUT), input_assunto=base_input_text(ASSUNTO_INPUT),
                           input_descricao=base_input_text(DESCRICAO_INPUT, "textarea"), contacts=all_contacts)


@contato_blueprint.route('/contato/add', methods=["GET", "POST"])
def add():
    if request.method == "POST":
        email = request.form.get("email")
        assunto = request.form.get("assunto")
        descricao = request.form.get("descricao")

        novo_contato = ContatoController.add(email, assunto, descricao)

    return redirect(url_for("contato.contato"))


@contato_blueprint.route('/contato/api/', methods=["GET"])
def get_many():
    contatos = Contato.get_all()

    return make_response(jsonify(contatos))


@contato_blueprint.route('/contato/<int:contact_id>/', methods=["GET"])
def get_by_id(contact_id: int):
    contact = Contato.query.filter_by(id=contact_id).first()
    if request.method == "GET":
        if contact:
            print(contact)

            return make_response(jsonify(mensagem=f"Contato {contact_id} atualizado com sucesso!", dados=contact))

        return make_response(jsonify(mensagem=f"Contato com id {contact_id} não encontrado!"))

    return contato()


@contato_blueprint.route('/contato/<int:contact_id>/update', methods=["GET", "PUT"])
def update_by_id(contact_id: int):
    contact = Contato.query.filter_by(id=contact_id).first()
    if request.method == "PUT":
        if contact:
            contact.update(request.json)

            return make_response(jsonify(mensagem=f"Contato {contact_id} atualizado com sucesso!", dados=request.json))

        return make_response(jsonify(mensagem=f"Contato com id {contact_id} não encontrado!"))

    return contato()


@contato_blueprint.route('/contato/<int:contact_id>/delete', methods=["GET", "DELETE"])
def delete_by_id(contact_id: int):
    contact = Contato.query.filter_by(id=contact_id).first()
    if request.method == "DELETE":
        if contact:
            contact.apagar()

            return make_response(jsonify(mensagem=f"Contato {contact_id} apagado com sucesso!"))

        return make_response(jsonify(mensagem=f"Contato com id {contact_id} não encontrado!"))

    elif request.method == "GET":
        if contact:
            contact.apagar()

        return redirect(url_for("contato.contato"))
