# Use uma imagem base do Python
FROM python:3.10

# Define o diretório de trabalho no contêiner
WORKDIR /home/ubuntu/djangoapp

# Copia o arquivo requirements.txt para o diretório de trabalho
COPY . /home/ubuntu/djangoapp

# Instala as dependências do Django

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /home/ubuntu/djangoapp/requirements.txt

# Executa as migrações e inicia o servidor quando o contêiner for iniciado
ENTRYPOINT python /home/ubuntu/djangoapp/manage.py runserver 0.0.0.0:8000

EXPOSE 8000
