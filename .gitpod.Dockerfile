FROM gitpod/workspace-full

USER gitpod

RUN pip install \
    Flask==2.0.1 \
    rich==10.11.0
