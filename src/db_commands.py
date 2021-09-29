from random import randint

from db import connection_context
from models import Challenge, User

CREATE_TABLE_USER = """
CREATE TABLE IF NOT EXISTS users (
    id integer PRIMARY KEY,
    cpf varchar(16) UNIQUE NOT NULL,
    email varchar(100) UNIQUE NOT NULL,
    birth_date varchar(12) NOT NULL,
    phone_number varchar(20) NOT NULL
);
"""


CREATE_TABLE_CHALLENGE = """
CREATE TABLE IF NOT EXISTS challenges (
    id integer PRIMARY KEY,
    title varchar(100),
    score integer NOT NULL,
    user_id integer NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user (id)
);
"""

CLEAR_TABLE_CHALLENGE = "DELETE FROM challenges"

USER_DATA = [
    User(1, email="any@email.com", cpf="111.111.111-11"),
    User(2, email="another@email.com", cpf="222.222.222-22"),
    User(3, email="yetanother@email.com", cpf="333.333.333-33"),
]

MIN_CHALLENGES_PER_USER = 2
MAX_CHALLENGES_PER_USER = 6


def start_database():
    with connection_context() as cur:
        cur.execute(CREATE_TABLE_USER)
        cur.execute(CREATE_TABLE_CHALLENGE)
        cur.execute(CLEAR_TABLE_CHALLENGE)

        for user in USER_DATA:
            insert_cmd = f"""
                INSERT INTO users (id, email, cpf, birth_date, phone_number)
                VALUES (
                    {user.id},
                    '{user.email}',
                    '{user.cpf}',
                    '{user.birth_date}',
                    '{user.phone_number}'
                )
                ON CONFLICT DO NOTHING
            """
            cur.execute(insert_cmd)

            challenges_count = randint(
                MIN_CHALLENGES_PER_USER,
                MAX_CHALLENGES_PER_USER,
            )
            CHAR_A_OFFSET = 65
            for i in range(CHAR_A_OFFSET, challenges_count + CHAR_A_OFFSET):
                challenge = Challenge(user.id, f"Challenge {chr(i)}")
                insert_cmd = f"""
                    INSERT INTO challenges (title, score, user_id)
                    VALUES (
                        '{challenge.title}',
                        {challenge.score},
                        {challenge.user_id}
                    )
                    ON CONFLICT DO NOTHING
                """
                cur.execute(insert_cmd)
