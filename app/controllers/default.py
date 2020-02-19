from app import app

@app.route("/index")
@app.route("/")
def index():
    return "Hello Funcionou"

@app.route("/teste")
def teste():
    return "Olá"