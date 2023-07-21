from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Bem vindo ao seu primeiro projeto com Python, utilizando o micro framework Flask!</p>"
