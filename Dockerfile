FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

WORKDIR /app/learning-sqlmodel
COPY . .
RUN pip install -r requirements.txt

# Run FastAPI
EXPOSE 8080
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
