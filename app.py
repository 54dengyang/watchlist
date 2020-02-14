from flask import Flask
from flask import url_for

app = Flask(__name__)

'''
@app.route('/')
@app.route('/index')
@app.route('/home')
def hello():
	# return 'Welcome to My Watchlist!'
	# return	u'欢迎来到我的Watchlist!'
	return	'<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'

@app.route('/user/<name>')
def user_page(name):
	# return 'User page'
	return 'User: %s' % name

@app.route('/test')
def test_url_for():
	print(url_for('hello'))
	print(url_for('user_page',name='deng'))
	print(url_for('user_page',name='yang'))
	print(url_for('test_url_for'))
	print(url_for('test_url_for',num=2))
	return 'Test page'
'''

name = 'deng yang'
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
	{'title': 'Mahjong', 'year': '1996'},
	{'title': 'Swallowtail Butterfly', 'year': '1996'}, {'title': 'King of Comedy', 'year': '1999'}, {'title': 'Devils on the Doorstep', 'year': '1999'}, {'title': 'WALL-E', 'year': '2008'},
	{'title': 'The Pork of Music', 'year': '2012'},
]

from flask import Flask, render_template

@app.route('/')
def index():
	return render_template('index.html',name=name,movies=movies)
