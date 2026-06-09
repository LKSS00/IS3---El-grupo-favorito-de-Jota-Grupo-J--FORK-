from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Simulacion TP5 Entorno de Desarrollo funcionando al 100%"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)