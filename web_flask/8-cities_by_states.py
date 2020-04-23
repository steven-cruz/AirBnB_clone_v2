#!/usr/bin/python3
# Python script that starts a flask application on 0.0.0.0 port 5000/ with
# variables: Show if number is even or odd
from flask import Flask, render_template
from models import storage
app = Flask(__name__)
app.url_map.strict_slashes = False
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


@app.teardown_appcontext
def teardown_app(exception):
    """Calls Storage close on appcontext"""
    storage.close()


@app.route('/cities_by_states')
def cities_by_states():
    states = []
    for key, values in storage.all('State').items():
        states.append(values)
    cities = []
    for key, values in storage.all('City').items():
        cities.append(values)
    return render_template('8-cities_by_states.html',
                           states=states, cities=cities)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
