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


@app.route('/states')
def states():
    states = []
    for key, values in storage.all('State').items():
        states.append(values)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>')
def states_var(id=None):
    cities = []
    for key, values in storage.all('City').items():
        if values.state_id == str(id):
            cities.append(values)

    name = None
    for key, values in storage.all('State').items():
        if values.id == str(id):
            name = values.name

    if len(cities) == 0 and name is None:
        return render_template('9-states.html', err=1)

    return render_template('9-states.html', name=name, cities=cities)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
