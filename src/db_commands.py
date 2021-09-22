from random import randint

from db import connection_context
from models import Challenge, User

CREATE_TABLE_USUARIO = """
CREATE TABLE IF NOT EXISTS usuario (
    id integer PRIMARY KEY,
    email varchar(100) UNIQUE NOT NULL,
    cpf varchar(16) UNIQUE NOT NULL,
    data_nascimento varchar(12) NOT NULL,
    telefone varchar(20) NOT NULL
);
"""


CREATE_TABLE_DESAFIO = """
CREATE TABLE IF NOT EXISTS desafio (
    id integer PRIMARY KEY,
    title varchar(100),
    pontos integer NOT NULL,
    usuario_id integer NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES usuario (id)
);
"""

CLEAR_TABLE_DESAFIO = "DELETE FROM desafio"

USER_DATA = [
    User(1, "qualquer@email.com", "111.111.111-11"),
    User(2, "outro@email.com", "222.222.222-22"),
    User(3, "maisum@email.com", "333.333.333-33"),
]

MIN_CHALLENGES_PER_USER = 2
MAX_CHALLENGES_PER_USER = 6


def start_database():
    with connection_context() as cur:
        cur.execute(CREATE_TABLE_USUARIO)
        cur.execute(CREATE_TABLE_DESAFIO)
        cur.execute(CLEAR_TABLE_DESAFIO)

        for user in USER_DATA:
            insert_cmd = f"""
                INSERT INTO usuario (id, email, cpf, data_nascimento, telefone)
                VALUES (
                    {user.id}, '{user.email}',
                    '{user.cpf}',
                    '{user.data_nascimento}',
                    '{user.telefone}'
                )
                ON CONFLICT DO NOTHING
            """
            cur.execute(insert_cmd)

            challenges_count = randint(
                MIN_CHALLENGES_PER_USER,
                MAX_CHALLENGES_PER_USER,
            )
            for i in range(1, challenges_count + 1):
                challenge = Challenge(user.id, f"Desafio {i}")
                insert_cmd = f"""
                    INSERT INTO desafio (title, pontos, usuario_id)
                    VALUES (
                        '{challenge.title}',
                        {challenge.pontos},
                        {challenge.usuario_id}
                    )
                    ON CONFLICT DO NOTHING
                """
                cur.execute(insert_cmd)
