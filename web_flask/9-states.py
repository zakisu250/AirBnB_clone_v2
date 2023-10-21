#!/usr/bin/python3
"""
Displays a states list
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_list():
    """ Display the templates of states in ascending order """
    states = storage.all(State).values()
    return render_template('9-states.html', Table="States",
                           states=states, condition="states_list")


@app.route('/states/<id>', strict_slashes=False)
def state_detail(id):
    """ Display a detail on a selected state """
    all_states = storage.all(State)
    try:
        state_ids = state_all[id]
        return render_template('9-states.html', state_id=state_id
                               condition="state_id")
    except:
        return render_template("9-states.html", condition="not_found")


@app.teardown_appcontext
def teardown_db(self):
    """ Close the session on teardown """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
