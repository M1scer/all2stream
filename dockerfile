# Wählen Sie ein leichtes Python-Image
FROM python:3.9-slim

# Installiere systemweite Abhängigkeiten für pydub und MP3-Encoding
RUN apt-get update && apt-get install -y \
    ffmpeg \
    lame \
    && rm -rf /var/lib/apt/lists/*

# Arbeitsverzeichnis setzen
WORKDIR /app

# Kopiere die Anforderungen und installiere sie
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Kopiere das Python-Skript ins Container-Verzeichnis
COPY app.py /app/app.py

# Exponiere Port 8000
EXPOSE 8000

# Starte den Flask-Server
CMD ["python", "app.py"]
