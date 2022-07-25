from flask import Flask, render_template, request, redirect


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('God of War', 'Hack n Slash', 'PS2')
jogo3 = Jogo('Mortal Kombat', 'Luta', 'PS2')
lista = [jogo1, jogo2, jogo3]

app = Flask(__name__)  # inicializa uma aplicação feita em Flask


@app.route('/')  # Definição das rotas da aplicação através do @app.route.
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista)  # acessa diretamente o html dentro da pasta
    # 'templates'


@app.route("/novo")
def novo():
    return render_template('novo.html', titulo='Novo Jogo')


@app.route('/criar', methods=['POST'])
def criar():
    nome = request. form['nome']
    categoria = request. form['categoria']
    console = request. form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect('/')


app.run(debug=True)

# Para definir a porta como 8080 e o host como 0.0.0.0 devemos chamar o run da seguinte maneira.trecho
# da app.

# app.run(host='0.0.0.0', port=8080)

# Observação: não utilizar estas definições para produção, estas opções foram preparadas para ajudar
# no ambiente de desenvolvimento.

# Tipos de Delimitadores do Jinja2:

# {%....%}: usado para inserir estruturas Python dentro de um arquivo html;
# {{....}}: usado para facilitar a exibição de código python como um output em um template HTML. Alternativa: {% print(....) %};
# {#....#}: usado para adicionar comentários que não serão exibidos no output do template HTML.