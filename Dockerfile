# Utilizando uma imagem oficial do Python
FROM python:3.11-slim

# Definindo o diretório de trabalho
WORKDIR /src

# Copiando os arquivos para o container
COPY requirements.txt ./

# Instalando as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiando o restante dos arquivos
COPY . .

# Expondo a porta utilizada pelo Flet
EXPOSE 8000

# Comando para rodar o aplicativo Flet
CMD flet run --web