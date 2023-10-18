from flask import Blueprint, render_template, make_response, jsonify, request
from app.components.base_title_text import base_title_text
from app.components.base_input_text import base_input_text
from app.constants.contato import CONTACT_TEXT, EMAIL_INPUT, ASSUNTO_INPUT, DESCRICAO_INPUT
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
    return ContatoController.add(request)


@contato_blueprint.route('/contato/api/', methods=["GET"])
def get_many():
    return make_response(jsonify(ContatoController.get_many()))


@contato_blueprint.route('/contato/<int:contact_id>/', methods=["GET"])
def get_by_id(contact_id: int):
    return ContatoController.get_by_id(contact_id)


@contato_blueprint.route('/contato/<int:contact_id>/update', methods=["POST", "PUT"])
def update_by_id(contact_id: int):
    return ContatoController.update_by_id(request, contact_id)


@contato_blueprint.route('/contato/<int:contact_id>/delete', methods=["GET", "DELETE"])
def delete_by_id(contact_id: int):
    return ContatoController.delete_by_id(request, contact_id)
