FROM python:3.12-slim
RUN pip3 install poetry --break-system-packages
WORKDIR /app
COPY pyproject.toml poetry.lock ./
COPY src /app/src

RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi --no-root

EXPOSE 8000

WORKDIR /app/src
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
