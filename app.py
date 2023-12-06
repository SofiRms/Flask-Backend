# app.py
from flask import Flask
from waitress import serve 

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '¡Hola, mundo! Este es mi primer servidor con Flask.'

if __name__ == '__main__':
    # Use the serve function from Waitress to run the app
    serve(app, host='0.0.0.0', port=5000, url_scheme='http', threads=4)
