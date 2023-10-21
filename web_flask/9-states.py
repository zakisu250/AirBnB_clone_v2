#!/usr/bin/python3
"""
Displays a states list
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """ Display the templates of states in ascending order """
    states = storage.all(State).values()
    return render_template('9-states.html', Table="States",
                           states=states, condition="states_list")


@app.route('/states/<id>', strict_slashes=False)
def states_with_id(id):
    """ Display a detail on a selected state """
    all_states = storage.all(State).values()
    try:
        state_ids = all_states[id]
        return render_template('9-states.html', state_id=state_ids,
                               condition="state_id")
    except Exception:
        return render_template("9-states.html", condition="not_found")


@app.teardown_appcontext
def teardown_db(self):
    """ Close the session on teardown """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
