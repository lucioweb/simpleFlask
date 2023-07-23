# simpleFlask
## Criando um simples projeto com Flask em duas etapas
### ETAPA - 1

Crie sua conta no [Git Hub](https://github.com/)  se ainda não possuir uma.
Crie um projeto público no Git Hub com o nome que desejar, mas `simpleFlask` seria apropriado para o que se pretende demonstrar.
Lembre-se acresecentar ao projeto durante sua criação o `README.md` e o `.git ignore` sugeridos. 

Dentro de um terminal qualquer digite o comando abaixo, para importar o projeto do repositório remoto do Git.
Estou usando o Ubuntu 22.04 no WSL2.
```
$ git clone https://github.com/lucioweb/simpleFlask.git
```

Abrindo a pasta do projeto com o `VSCode`.
```
$ code .
```
### ETAPA - 2
Essa etapa utiliza o tutorial do próprio Flask disponível em [Flask - Installation](https://flask.palletsprojects.com/en/2.3.x/installation/#dependencies)

Criando o `.venv` na pasta do projeto `simpleflask`✔️
```
$ python3 -m venv .venv
```

Antes de trabalhar em seu projeto, ative o ambiente correspondente.
Ativando o `.venv` (Conforme https://flask.palletsprojects.com/en/2.3.x/installation/). 
Lembre-se, esse comando e o anterior devem ser dados dentro da pasta do projeto.
```
$ . .venv/bin/activate
```

Dentro do ambiente ativado, use o seguinte comando para instalar o Flask:
```
(.venv) luciolemos@dev:~/my_python_projects/simpleFlask$ pip install flask
```

Ou use um um Arquivo de Requisitos `requirements.txt` para instalar o flask e outras dependências:
```
(.venv) luciolemos@dev:~/my_python_projects/simpleFlask$ python3 -m pip install -r requirements.txt
```

Flask foi instalado com sucesso. As seguintes dependências foram instaladas dentro do ambiente ativado:
```
Successfully installed 
Flask-2.3.2 
Jinja2-3.1.2 
MarkupSafe-2.1.3 
Werkzeug-2.3.6 
blinker-1.6.2 
click-8.1.6 
itsdangerous-2.1.2
```
Crie um arquivo com o nome que desejar, mas `hello.py` seria apropriado para o que se pretende mostrar em seguida.
Via linha de comando no terminal integrado do VS Code o comando seria:
```
$ echo>hello.py
```
Dentro do arquivo `hello.py` criado, digite ou cole, se ainda não tem habilidade suficiente com o Flask, as seguintes linhas de código:
```
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
```
Como a lib do Flask está instalada em nosso projeto, vamos subir a aplicação com o seguinte comando:
```
$ flask --app hello run
```

Ou no modo de depuração com o seguinte comando:
```
$ flask --app hello run --debug
```

Veremos no terminal o seguinte retorno, indicando que a aplicação foi carregada com sucesso:
```
 * Serving Flask app 'hello'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
127.0.0.1 - - [21/Jul/2023 07:30:16] "GET / HTTP/1.1" 200 -
```
Basta digitar no seu navegador favorito o seguinte URL: http://127.0.0.1:5000

Pronto! 

Está criando o seu projeto Pythoh - Flask, rodando na porta 5000, porta de escuta padrão utilizada pelo Python, emitindo uma mensagem de boas vindas.

### ETAPA COMPLEMENTAR

#### CRIANDO O ARQUIVO DE MANIFESTO `requirements.txt`
Em vez de instalar pacotes individualmente, pip permite que você declare todas as dependências em um Arquivo de Requisitos.
Por exemplo: você pode criar um arquivo `requirements.txt` na raiz do projeto, contendo todas as bibliotecas que deseja instalar e instalá-las com esssa linha de comando:
```
$ python3 -m pip install -r requirements.txt
```
