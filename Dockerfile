from python:3.9-slim

workdir /app

# Устанавливаем необходимые зависимости для PostgreSQL
run apt-get update && apt-get install -y libpq-dev gcc

copy . /app/

run pip install -r requirements.txt

expose 8000

cmd ["python", "-m", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]

volume /app/data