#!/usr/bin/python3
# Python script that starts a flask application on 0.0.0.0 port 5000/ with
# variables if variable is a number
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """Python function to print Hello HBNB"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """Python function to print HBNB"""
    return "HBNB"


@app.route('/c/<text>')
def c_text(text):
    """Python function to print C with directory"""
    return "C " + text.replace('_', ' ')


@app.route('/python')
@app.route('/python/<text>')
def python_magic(text="is cool"):
    """Python function to print Python magic with directory"""
    return "Python " + text.replace('_', ' ')


@app.route('/number/<int:n>')
def number_route(n):
    """Python function to a number"""
    if isinstance(n, int):
        return str(n) + ' is a number'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
