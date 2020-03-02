from flask import render_template
from app import app

@app.route("/")
def index():
    return render_template('login.html')

@app.route("/index/<user>")
def main(user):
    return render_template('main.html',
                           user=user)





############# EXEMPLOS #########################
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