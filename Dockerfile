# Usa a imagem oficial do Python
FROM python:3.11

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos do projeto
COPY . .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Cria a pasta de downloads
RUN mkdir -p /app/downloads

# Comando para rodar o servidor Flask
CMD ["python", "app.py"]
