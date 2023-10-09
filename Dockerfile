FROM docker.io/library/python:3.12-alpine
ENV PYTHONPATH /app:$PYTHONPATH
COPY pyproject.toml /app/pyproject.toml
RUN pip install --disable-pip-version-check --no-cache-dir /app
COPY src/ /app/src/
ENTRYPOINT ["python3", "-m", "src"]
