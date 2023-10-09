from flask import jsonify
from ..models.Contato import Contato


class ContatoController:
    @staticmethod
    def add(email, assunto, descricao):
        novo_contato = Contato(email=email, assunto=assunto, descricao=descricao)
        novo_contato.adicionar()

        return jsonify(mensagem="Contato criado com sucesso!", dados={})
