#!/usr/bin/python3
# Starts a flask applicaction on 0.0.0.0 port 5000
from flask import Flask
app = Flask(__name__)
app. url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """ Python function that prints Hello HBNB """
    return "Hello HBNB!"

@app.route('/hbnb')
def hbnb():
    """ Python function that prints HBNB """
    return "HBNB"

@app.route('/c/<text>')
def c():
    """ Python function that prints C followed by the value ot the <text> """
    return "C %s" % escape(text)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
