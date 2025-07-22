# Dockerfile

FROM python:3.11-slim

# Setăm directorul de lucru
WORKDIR /app

# Copiem requirements și instalăm dependențele
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiem restul aplicației
COPY . .

# Comandă de rulare a serverului
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
