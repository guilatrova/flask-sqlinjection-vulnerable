from flask import Flask

from db import get_challenges_for_candidate

app = Flask(__name__)


@app.route("/")
def index():
    return (
        "Hi 👋 head out to "
        '<a href="/challenges/111.111.111-11">this link</a> to get started.'
    )


@app.route("/challenges/<cpf>")
def get_challenges(cpf: str):
    print("-" * 50)
    print(f"Passing input: {cpf}")
    print("-" * 50)

    challenges = get_challenges_for_candidate(cpf)
    output = [f"<li>{title}: scored {score}</li>" for title, score in challenges]

    disclaimer = f"""
        <p>Here are the challenges I got for candidate:
            <pre><blockquote>{cpf}</blockquote></pre>
        </p>
    """
    return f"{disclaimer}<br/><ol>{''.join(output)}</ol>"
