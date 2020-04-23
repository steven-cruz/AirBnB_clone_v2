#!/usr/bin/python3
# Python script that starts a flask application on 0.0.0.0 port 5000/ with
# variables: Show if number is even or odd
from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    """Python function to print Hello HBNB"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """Python function to print HBNB"""
    return "HBNB"


@app.route('/c/<text>')
def c_is_fun(text):
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


@app.route('/number_template/<int:n>')
def number_template(n=None):
    """Python function to a number"""
    if isinstance(n, int):
        return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n=None):
    """Python function to a number"""
    if isinstance(n, int):
        return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
