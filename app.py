from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='.')

# Página principal
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# Página de compra (com query ?id=...)
@app.route('/compra')
def compra():
    return send_from_directory('.', 'compra.html')

# Página de histórico
@app.route('/compras')
def compras():
    return send_from_directory('.', 'compras.html')


# IMPORTANTE: fallback para evitar erro 404 no Azure
@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('.', path)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
