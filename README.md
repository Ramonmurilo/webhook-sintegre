# [Webhook-Sintegre]

![texto](https://img.shields.io/static/v1?label=linguagem&message=python&color=green&style=flat-square "linguagem")
![texto](https://img.shields.io/static/v1?label=ambiente&message=docker&color=orange&style=flat-square "ambiente")
![texto](https://img.shields.io/badge/status-operacional-success.svg "status")



1. [Descrição do projeto](#descrição-do-projeto)  
2. [Funcionalidades](#funcionalidades)   
4. [Pré-requisitos](#pré-requisitos)  
5. [Como instalar](#como-instalar)
6. [Desenvolvimento](#desenvolvimento)
7. [Como rodar](#como-rodar)
8. [I/O](#I/O)


## :scroll: Descrição do projeto

Webhook para download e consumo de dados do Sintegre-ONS. [Navegue pela documentação aqui (ainda não disponível)]


## :sparkles: Funcionalidades

:wrench: Ativa um servidor/aplicativo com login e senha de acesso   
:wrench: Aguarda a disponibilização de um arquivo pelo ONS      
:wrench: Baixa os arquivos e trata seu nome   

## :warning: Pré-requisitos

- Porta 5000 do Host liberada
- [Docker](https://docs.docker.com) (obrigatório)


## :cd: Como instalar

Baixe o repositório:
```bash
# 1. no terminal, clone o projeto
git clone https://github.com/Ramonmurilo/webhook-sintegre.git

# 2. entre na pasta do projeto
cd webhook-sintegre
```
Ambientes Docker não necessitam de instalação. Pode seguir diretamente ao tópico "Como rodar"

## :construction: Desenvolvimento

:white_check_mark: O código já se encontra operacional

## :rotating_light: Como rodar

crie a imagem com:
```bash
docker build -t flask-container .
```

Rode o container com volumes:
```bash
docker run -p 5000:5000 -v /home/ubuntu/webhook-sintegre/download:/app/download flask-container
```
-p = use a porta 5000 do host para refletir a porta 5000 do container 

-v = volume/no/pc : pasta/no/docker

## :green_apple: I/O

Os Inputs/entradas e outputs/saídas ficam na pasta ```donwload``` do container e do Host   

fontes: https://aws.amazon.com/pt/getting-started/hands-on/serve-a-flask-app/

https://flask.palletsprojects.com/en/2.0.x/
