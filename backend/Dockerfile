# backend/Dockerfile
FROM python:3.11-slim

WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

# 1) install deps from file (cache layer)
COPY requirements.txt .
RUN python -m pip install --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

# 2) copy app and run
COPY . .
CMD ["uvicorn", "agentos:app", "--host", "0.0.0.0", "--port", "7777"]
