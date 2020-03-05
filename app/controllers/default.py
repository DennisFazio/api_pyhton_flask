from flask import render_template
from app import app

@app.route("/signin")
def index():
    return render_template('/signin/signin.html')

@app.route("/main")
def main():
    return render_template('main.html')

@app.route("/base")
def base():
    return render_template('base.html')

@app.route("/original")
def original():
    return render_template('original.html')




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