# webhook-sintegre

crie a imagem com:
```
docker build -t flask-container .
```


Rode o container
```
docker run -p 5000:5000 -v /home/ubuntu/webhook-sintegre2/download:/app/download flask-container
```
-p = use a porta 5000 do host para refletir a porta 5000 do container
-v = volume/no/pc : pasta/no/docker

fontes: https://aws.amazon.com/pt/getting-started/hands-on/serve-a-flask-app/
https://flask.palletsprojects.com/en/2.0.x/
