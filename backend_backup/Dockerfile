FROM python:3.11-slim

WORKDIR /app

# Instalar herramientas de compilación necesarias
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements.txt y eliminar la línea de torch (la instalaremos aparte)
COPY requirements.txt .
RUN sed -i '/^torch==/d' requirements.txt

# Instalar PyTorch para CPU (mucho más ligero)
RUN pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu

# Instalar el resto de dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código de la aplicación
COPY . .

# Crear directorio de uploads
RUN mkdir -p uploads

# Ejecutar la aplicación
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
