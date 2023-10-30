import os
from flask import Flask, render_template

app = Flask(__name__)

# Definindo a variável de ambiente
os.environ['FLASK_DEBUG'] = 'True'

# Configurando o modo de depuração com base na variável de ambiente
app.debug = os.environ.get('FLASK_DEBUG') == 'True'

@app.route('/')
def ola():
    return render_template('index.html')


@app.route('/sobre-equipe')
def sobre():
    return render_template('sobre.html')


if __name__ == "__main__":
    app.run()
