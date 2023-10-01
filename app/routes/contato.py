from flask import Blueprint, render_template
from app.components.base_title_text import base_title_text
from app.components.base_input_text import base_input_text
from app.constants.contato import CONTACT_TEXT, EMAIL_INPUT, ASSUNTO_INPUT, DESCRICAO_INPUT

contato_blueprint = Blueprint('contato', __name__)


@contato_blueprint.route('/contato')
def contato():
    return render_template("contato.html", contact=base_title_text(CONTACT_TEXT),
                           input_email=base_input_text(EMAIL_INPUT), input_assunto=base_input_text(ASSUNTO_INPUT),
                           input_descricao=base_input_text(DESCRICAO_INPUT, "textarea"))
