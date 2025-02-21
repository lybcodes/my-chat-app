FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

COPY my_chat_app/static /app/my_chat_app/static

EXPOSE 8080

CMD ["uvicorn", "my_chat_app.app:app", "--host", "0.0.0.0", "--port", "8080"]
