FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /app

CMD ["sh", "-c", "sleep 5 && python db_init/init_db.py && uvicorn main:app --host 0.0.0.0 --port 7531"]
