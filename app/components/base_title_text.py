def base_title_text(text_info: dict) -> str:
    title_text_html = f"<h2 class='apresentacao__conteudo__texto_title text-center'>{text_info.get('title')}</h2>"
    for p in text_info.get('text'):
        title_text_html += f"<p class='apresentacao__conteudo__texto_subtitle text-center mt-3 mb-5'>{p}</p>"

    return title_text_html
