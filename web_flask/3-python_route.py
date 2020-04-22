#!/usr/bin/python3
# starts a flask application on 0.0.0.0 port 5000
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Python function that prints Hello HBNB! """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Python function that prints HBNB """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ Python function that prints C follewed by value of the <text> """
    return "C {}".format(text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """
    Python function that prints Python follewed by value of the <text>
    variable, the default value of <text> is "is cool"
    """
    return "Python {}".format(text.replace("_", " "))


if __name__ == '__mian__':
    app.run(host="0.0.0.0", port=5000)
