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

@app.route('/test')
def test():
    return render_template("test.html")

@app.route('/<size>')
def one(size):
    return render_template(
                            'one.html', 
                            size=size
                           )

def result_calculate(size, lights, device):
    #Переменные для энергозатратности приборов
    home_coef = 100
    light_coef = 0.04
    devices_coef = 5   
    return size * home_coef + one * light_coef + device * devices_coef 


app.run()