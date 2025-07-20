FROM python:3.13-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip3 install uv

COPY pyproject.toml uv.lock /app

RUN uv sync

COPY . /app