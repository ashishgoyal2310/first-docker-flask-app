"""
python runserver-sample.py
"""
import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    """Return a friendly HTTP greeting."""
    message = "Hello World"
    return message

if __name__ == "__main__":
    app.run(host="0.0.0.0")
