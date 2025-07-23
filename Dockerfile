# Usa un'immagine base leggera di Python 3.13
FROM python:3.13-slim

# Imposta la working directory dentro il container
WORKDIR /app

# Copia solo il requirements.txt prima per ottimizzare la cache di Docker
COPY requirements.txt .

# Installa le dipendenze Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia tutto il codice sorgente dentro il container
COPY . .

# Imposta variabile ambiente per output immediato (utile per i log)
ENV PYTHONUNBUFFERED=1

# Esponi la porta su cui gira Flask
EXPOSE 8000

# Comando per avviare l'app Flask (modifica se usi un altro file entrypoint)
CMD ["python", "exporter.py"]
