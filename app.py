"""
    Primeiro para fazer o deploy para AWS usando o docker, primeiro
    é necessário ter a aplicação flask montada, seguindo com Dockerfile
    definido e uma lista de dependências.
    
    Segundo cria uma instância na AWS com o servico EC2, e fazer as configurações
    após isso, conectar com a instância usando o ssh -i <chave.pem> <ec2-user@ip-public>,
    instalar e atualizar o docker na instância, copiar a pasta do projeto para a instância
    com scp -i <caminho/chave.pem> -r <pasta> <ec2-user@ip-public>, ir ate o diretório da pasta
    builtar a imagem docker e finalmente executar o container.
"""

    
    