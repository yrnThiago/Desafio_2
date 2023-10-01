from flask import Flask, render_template

app = Flask(__name__)

reasons_to_study = ["Material sempre atualizado", "Tablets em sala de aula", "Professores renomados",
                    "Universidade bem avaliada", "Ótima localização"]

inputs_forms = [
    {"tag": "input", "title": "Seu e-mail", "type": "email", "id": "email", "placeholder": "seuemail@email.com"},
    {"tag": "input", "title": "Assunto", "type": "text", "id": "assunto", "placeholder": "Assunto"},
    {"tag": "textarea", "title": "Descrição", "rows": "2", "cols": "29", "id": "descricao", "placeholder": "Isso é uma descrição..."},
]


def convert_to_input_form(form_inputs):
    form_inputs_html, input_element = "", ""
    for form_input in form_inputs:
        if form_input.get("tag") == "input":
            input_element = f"""<input class="formulario__input" type="{form_input.get('type')}"
             id="{form_input.get('id')}" placeholder="{form_input.get('placeholder')}">"""
        else:
            input_element = f"""<textarea rows="{form_input.get('rows')}" cols="{form_input.get('cols')}"
             id="{form_input.get('id')}" placeholder="{form_input.get('placeholder')}"></textarea>"""

        form_inputs_html += f"""
            <div class="formulario__{form_input.get('type')}">
                <label for="{form_input.get('type')}">{form_input.get('title')}:</label><br>
                {input_element}
            </div>
        """

    return form_inputs_html


@app.route('/')
@app.route('/home')
def home():
    return render_template('Home.html')


@app.route("/quemsomos")
def quemsomos():
    return render_template("QuemSomos.html", qty_reasons=len(reasons_to_study), reasons=reasons_to_study)


@app.route("/contato")
def contato():
    return render_template("contato.html", inputs_forms=convert_to_input_form(inputs_forms))


if __name__ == "__main__":
    app.run(debug=True)
