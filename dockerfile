# Základní image
FROM python:3.9-slim

# Nastav pracovní adresář
WORKDIR /app

# Zkopíruj requirements a nainstaluj závislosti
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Zkopíruj celou aplikaci
COPY . .

# Exponuj port
EXPOSE 5000

# Start aplikace
CMD ["flask", "run", "--host=0.0.0.0"]

