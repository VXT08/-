#Импорт
from flask import Flask, render_template, request


app = Flask(__name__)


#Первая страница
@app.route('/')
def main():
    return render_template('main.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/info')
def info():
    return render_template('info.html')


app.run()