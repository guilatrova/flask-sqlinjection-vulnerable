import random
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class User:
    id: int
    email: str
    cpf: str
    data_nascimento: str = "01-01-1990"
    telefone: str = "1234567899"


@dataclass
class Challenge:
    usuario_id: int
    title: str
    pontos: int = field(init=False)
    id: Optional[int] = None

    def __post_init__(self):
        self.pontos = random.randint(0, 10)
