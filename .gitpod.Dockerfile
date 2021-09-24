FROM gitpod/workspace-full

USER gitpod

RUN pip install poetry
RUN poetry config virtualenvs.create false
