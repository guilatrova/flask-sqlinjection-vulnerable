import random
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class User:
    id: int
    cpf: str
    email: str
    birth_date: str = "01-01-1990"
    phone_number: str = "1234567899"


@dataclass
class Challenge:
    user_id: int
    title: str
    score: int = field(init=False)
    id: Optional[int] = None

    def __post_init__(self):
        # We don't care about score, we just want random values
        self.score = random.randint(0, 10)
