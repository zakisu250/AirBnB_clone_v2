#!/usr/bin/python3
"""
Displays a states list
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_list():
    """ Display the templates of states in ascending order """
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html',
                           Table="States", states=states)


@app.teardown_appcontext
def teardown_db(self):
    """ Close the session on teardown """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
