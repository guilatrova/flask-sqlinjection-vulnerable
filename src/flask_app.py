from flask import Flask

from db import get_desafios_candidato

app = Flask(__name__)


@app.route("/desafios/<cpf>")
def get_desafios(cpf: str):
    """Misturar ingles e portugues, who never?"""
    desafios = get_desafios_candidato(cpf)
    output = [f"<li>{title}: {pontos}</li>" for title, pontos in desafios]

    return f"<ol>{''.join(output)}</ol>"
