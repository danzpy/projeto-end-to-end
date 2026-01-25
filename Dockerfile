FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    POETRY_VIRTUALENVS_CREATE=false

WORKDIR /app

RUN pip install --no-cache-dir poetry

COPY pyproject.toml poetry.lock* ./
RUN poetry install --no-interaction --no-ansi --no-root

RUN apt-get update && apt-get install -y wget unzip && \
   wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
   apt install -y ./google-chrome-stable_current_amd64.deb && \
   rm google-chrome-stable_current_amd64.deb && \
   apt-get clean

COPY . .

CMD ["poetry", "run", "python", "main.py"]
