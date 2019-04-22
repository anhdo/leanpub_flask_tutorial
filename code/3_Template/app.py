from flask import Flask
from flask import redirect
app = Flask(__name__)

@app.route('/hello')
def hello():
	return 'Hello'


@app.route('/hello/<name>')
def specific_hello(name):
	return 'Hello {}'.format(name)


@app.route('/double/<int:num>')
def double(num):
	return 'Double of {} is {}'.format(num, num*2)


@app.route('/old_hello')
def old_hello():
	return redirect('/hello')


@app.route('/custom_code')
def custom_code():
	return 'custom code', 201
