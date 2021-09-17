from flask import Flask, request, Response, send_from_directory
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from pathlib import Path
import requests
import pendulum

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "ons": generate_password_hash("senha_para_acesso_do_ons"),
    "outro_usuario": generate_password_hash("senha_outro_usuario")
}

def uniformiza_string(string:str) -> str:
    """Remove caracteres especiais da string e torna todas as letras minúsculas.

    Args:
        string (str): string a ser uniformizada

    Returns:
        str: string uniformizada
    """

    new_string = ''.join(filter(str.isalnum, string))
    new_string = new_string.lower()

    return new_string

@auth.verify_password
def verify_password(username:str, password:str) -> str:
    """Verifica se login e senha digitados constam na dict users

    Args:
        username (str): login do usuário
        password (str): senha do usuário

    Returns:
        str: retorna o nome do usuario logado
    """
    if username in users and \
            check_password_hash(users.get(username), password):
        return username


@app.route('/')
@auth.login_required
def hello_world() -> str:
    """Página inicial
    Checagem se o app está funcionando

    Returns:
        str: Retorna mensagem de funcionamento do app
    """
    return f"""Aplicação webhook funcionando!!! Olá {auth.current_user()}"""


#caminho do webhook
@app.route('/webhook', methods=['POST'])
@auth.login_required
def webhook():
    """Página da aplicação para coletar o método Post do ONS

    Returns:
        Any: Resposta http 200
    """
    data = request.json

    arquivo_nome = uniformiza_string(data['nome'])
    print(data['dataProduto'])
    arquivo_data = pendulum.from_format(data['dataProduto'], 'DD/MM/YYYY', tz='America/Sao_Paulo')

    download_path = Path('download')
    download_path.mkdir(exist_ok=True, parents=True)

    resp=requests.get(data['url']).content

    with open(f"{download_path}/{arquivo_nome}-{arquivo_data.format('DD-MM-YYYY')}" , "wb") as arquivo_:
        arquivo_.write(resp)

    return Response(status=200)

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
