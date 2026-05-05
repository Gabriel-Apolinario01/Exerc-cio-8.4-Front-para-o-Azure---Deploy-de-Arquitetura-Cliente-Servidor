from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='.')

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/compra')
def compra():
    return send_from_directory('.', 'compra.html')

@app.route('/compras')
def compras():
    return send_from_directory('.', 'compras.html')

if __name__ == '__main__':
    app.run()
