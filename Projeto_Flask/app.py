from flask import Flask, render_template, request
from random import randint

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    variavel = "Jogo de Adivinhação"
    if request.method == 'GET':
        return render_template('index.html', variavel=variavel)
    else:
        num = randint(0, 20)
        inserido = int(request.form.get('name'))
        if num == inserido:
            return render_template('acerto.html')
        else:
            return render_template('erro.html')
if __name__ == '__main__':
    app.run(debug=True)