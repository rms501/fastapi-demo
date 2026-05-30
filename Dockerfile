FROM python:3.13

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

RUN useradd -m app
USER app

WORKDIR /usr/local/app

COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev --no-install-project

COPY ./ ./
RUN uv sync --frozen --no-dev

EXPOSE 8000

CMD ["uv", "run", "python", "main.py"]