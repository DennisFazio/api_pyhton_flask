from flask import render_template
from app import app

@app.route("/index/<user>")
@app.route("/", defaults={'user': None})
def index(user):
    return render_template('index.html',
                           user=user)

@app.route("/test", defaults={'name': None}) # Rota com retorno padrão
@app.route("/test/<name>")
def teste(name):
    if name:
        return "Teste \n Olá, %s" %name
    else:
        return "Teste \n Olá, ser sem nome"

@app.route("/test_dois", methods=['GET']) # Limitar qual o verbo a utilizar na rota
def teste_dois(name=None):
    if name:
        return "Teste \n Olá, %s" %name
    else:
        return "Teste \n Olá, ser sem nome"