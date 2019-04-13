from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
	text = 'simple math'
	number = 100
	return render_template('index.html', text=text, number=number)

@app.route('/')
def index():
	user = {'name': 'John', 'age': 20, 'hobby': 'basketball'}
	return render_template('index.html', user=user)

@app.route('/')
def index():
	shopping_list = ['banana', 'egg', 'milk']
	return render_template('index.html', shopping_list=shopping_list)
