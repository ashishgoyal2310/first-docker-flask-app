from apps import app
from flask import render_template

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    message = "<h1>Hello World !!!<h1>"
    return message


@app.route('/home')
def home():
    return render_template('home.html')