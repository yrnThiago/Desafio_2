def base_title_text(text_info: dict) -> str:
    title_text_html = f"<h1>{text_info.get('title')}</h1>"
    for p in text_info.get('text'):
        title_text_html += f"<p>{p}</p>"

    return title_text_html
