# Usa uma imagem leve do Python 3.10
FROM python:3.10-slim

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia apenas o arquivo de dependências primeiro (melhora cache do Docker)
COPY requirements.txt .

# Instala as dependências da API
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código do projeto para dentro do contêiner
COPY . .

# Expõe a porta da API
EXPOSE 8000

# Comando de execução - Sem realod para a produção
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
