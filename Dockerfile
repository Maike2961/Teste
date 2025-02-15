#Baixando uma imagem do python no docker hub
FROM python:3.13-alpine

#criando uma pasta no container
WORKDIR /app

#copiando o arquivo de dependências
COPY requirements.txt /app

#instaland as dependências no container
RUN pip install -r requirements.txt 

#copiando a aplicação
COPY app.py /app

#expondo a porta no container
EXPOSE 5000

#comando para ir ate a aplicação e executar no container
CMD [ "sh", "-c", "python app.py", "--host", "0.0.0.0" ]