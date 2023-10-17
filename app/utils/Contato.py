def get_body(contato):
    return {"id": contato.id, "email": contato.email, "assunto": contato.assunto, "descricao": contato.descricao}
