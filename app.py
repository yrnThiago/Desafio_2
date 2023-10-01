from flask import Flask, render_template
from components.input_forms import form_inputs_html
from components.base_title_text import base_title_text
from constants.QuemSomos import reasons_to_study, ABOUT_US_TEXT, OBJECTIVES_TEXT
from constants.Home import ABOUT_TEXT
from constants.Contato import CONTACT_TEXT

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('Home.html', about_university=base_title_text(ABOUT_TEXT))


@app.route("/quemsomos")
def quemsomos():
    return render_template("QuemSomos.html", about_us=base_title_text(ABOUT_US_TEXT),
                           qty_reasons=len(reasons_to_study), reasons=reasons_to_study,
                           objectives=base_title_text(OBJECTIVES_TEXT))


@app.route("/contato")
def contato():
    return render_template("contato.html", contact=base_title_text(CONTACT_TEXT),
                           inputs_forms=form_inputs_html)


if __name__ == "__main__":
    app.run(debug=True)
