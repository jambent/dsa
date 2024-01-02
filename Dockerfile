FROM python:3

RUN apt-get update && \
    apt-get upgrade --yes

RUN useradd --create-home dsa_user
USER dsa_user
WORKDIR /home/dsa_user

ENV VIRTUALENV=/home/dsa_user/venv
RUN python3 -m venv $VIRTUALENV
ENV PATH="$VIRTUALENV/bin:$PATH"

COPY --chown=dsa_user pyproject.toml constraints.txt ./

RUN python -m pip install --upgrade pip setuptools && \
    python -m pip install --no-cache-dir -c constraints.txt ".[dev]"