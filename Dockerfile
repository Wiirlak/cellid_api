################################
# PYTHON-BASE
# Sets up all our shared environment variables
################################
FROM python:3.12-bookworm AS python-base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.7.1 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

################################
# BUILDER-BASE
# Used to build deps + create our virtual environment
################################
FROM python-base AS dev

WORKDIR $PYSETUP_PATH

RUN apt-get update && apt-get install --no-install-recommends -y curl build-essential
RUN curl -sSL https://install.python-poetry.org | python3 -

COPY poetry.lock pyproject.toml ./
RUN --mount=type=cache,target=/root/.cache poetry install --with dev

COPY src ./src
COPY main.py ./

WORKDIR /usr/src/upciti