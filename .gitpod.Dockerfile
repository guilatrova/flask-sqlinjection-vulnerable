FROM gitpod/workspace-full

USER gitpod

RUN pip install \
    Flask==2.0.1 \
    rich==10.11.0 \
    # linters
    black==21.9b0 \
    flake8==3.9.2 \
    isort==5.9.3 \
    mypy==0.910 \
    tryceratops==0.6.0
