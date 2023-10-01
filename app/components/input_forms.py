from app.constants.contato import form_fields

form_inputs_html, input_element = "", ""
for form_input in form_fields:
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
