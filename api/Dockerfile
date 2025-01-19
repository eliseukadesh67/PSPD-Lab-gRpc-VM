# Base image
FROM python:3.9-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos de dependências para a imagem
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código da aplicação para o diretório de trabalho
COPY . .

# Define a porta em que o Flask será executado
EXPOSE 5000

# Comando para executar o servidor
CMD ["python", "server.py"]
