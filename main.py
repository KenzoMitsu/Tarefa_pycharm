from flask import Flask, render_template, request, redirect

app = Flask(__name__)

nome_musica = []
artistas = []

musica = [
    [1, 'Despacito', 'Luis Fonsi', 'Pop latino'],
    [2, 'Happy Nation', 'Ace of Base', 'Pop'],
    [3, 'Monster', 'Skillet', 'Rock cristão']
]

@app.route('/')
def index():
    return render_template('index.html', artistas=artistas, musica=musica)

@app.route('/favoritamento')
def favoritamento():
    return render_template('favoritamento.html')

@app.route('/lista_musical')
def lista_musical():
    return render_template('lista_musical.html', nome_musica=nome_musica)

@app.route('/verificar_musica', methods=['GET', 'POST'])
def verificar_musica():
    if request.method == 'POST':
        nome_da_musica = request.form['nome_musica']
        nome_artista = request.form['nome_artista']
        genero_musical = request.form['genero_musical']
        codigo = len(nome_musica)
        nome_musica.append([codigo, nome_da_musica, nome_artista, genero_musical])
        return redirect('/lista_musical')
    else:
        return render_template('favoritamento.html')

# Rota para apagar uma música da lista
@app.route('/apagar_musica/<int:codigo>', methods=['GET', 'POST'])
def apagar_musica(codigo):
    del nome_musica[codigo]
    return redirect('/lista_musical')  # Redireciona de volta para a página da lista musical

# Rota para a página da música
@app.route('/musica')
def musica_route():
    return render_template('musica.html')

# Rota para editar uma música existente
@app.route('/editar_musica/<int:codigo>', methods=['GET', 'POST'])
def editar_musica(codigo):
    if request.method == 'POST':
        nome_da_musica = request.form['nome_musica']
        nome_artista = request.form['nome_artista']
        genero_musical = request.form['genero_musical']
        nome_musica[codigo] = [codigo, nome_da_musica, nome_artista, genero_musical]
        return redirect('/')
    else:
        musica_selecionada = nome_musica[codigo]
        return render_template('editar_musica.html', musica=musica_selecionada)

# Rota para apagar uma música da lista (duplicada)
@app.route('/apagar_musica/<int:codigo>')
def apagar_musica_duplicado(codigo):
    del nome_musica[codigo]
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)