#!/usr/bin/python3
# Python script that starts a flask application on 0.0.0.0 port 5000
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    """Python function to print Hello HBNB"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
