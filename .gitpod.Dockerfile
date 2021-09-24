FROM gitpod/workspace-full

USER gitpod

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3
ENV PATH="$HOME/.poetry/bin:$PATH"
RUN poetry config virtualenvs.create false
