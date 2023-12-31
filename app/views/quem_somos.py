from flask import Blueprint, render_template
from app.components.base_title_text import base_title_text
from app.constants.quem_somos import ABOUT_US_TEXT, OBJECTIVES_TEXT

quem_somos_blueprint = Blueprint('quemsomos', __name__)


@quem_somos_blueprint.route('/quemsomos')
def quemsomos():
    return render_template("quem_somos.html", about_us=base_title_text(ABOUT_US_TEXT),
                           objectives=base_title_text(OBJECTIVES_TEXT))
