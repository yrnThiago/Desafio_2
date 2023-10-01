from flask import Blueprint, render_template
from app.components.base_title_text import base_title_text
from app.components.input_forms import form_inputs_html
from app.constants.contato import CONTACT_TEXT

contato_blueprint = Blueprint('contato', __name__)


@contato_blueprint.route('/contato')
def contato():
    return render_template("contato.html", contact=base_title_text(CONTACT_TEXT),
                           inputs_forms=form_inputs_html)
