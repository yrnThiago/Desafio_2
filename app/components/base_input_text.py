def base_input_text(info: dict, input_type: str = "input"):
    res = f'<label for="{info.get("label")}">{info.get("title")}:</label><br> <{input_type} class="formulario__input" '
    for key, value in info.get("args").items():
        res += f'{key}="{value}"'
    res += f"></{input_type}>"

    return res
