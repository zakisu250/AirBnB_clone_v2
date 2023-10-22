#!/usr/bin/python3
"""
Displays a states list
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_with_id(id=None):
    """ Display a detail on a selected state """
    states = storage.all(State)
    if id is not None:
        id = 'State.' + id
    return render_template('9-states.html', states=states, state_id=id)


@app.teardown_appcontext
def teardown_db(self):
    """ Close the session on teardown """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
