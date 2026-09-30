FROM python:3.14-slim

WORKDIR /code

# Install dependencies first, so Docker can cache this layer
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app

# Run as a non-root user
RUN useradd --system --no-create-home appuser
USER appuser

EXPOSE 8000

# 0.0.0.0 is required so the port is reachable from outside the container
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]