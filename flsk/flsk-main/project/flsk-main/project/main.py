#Импорт
from flask import Flask, render_template, request


app = Flask(__name__)


#Первая страница
@app.route('/')
def index():
    return render_template('main.html')


app.run()