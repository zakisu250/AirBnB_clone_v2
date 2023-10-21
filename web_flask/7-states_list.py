#!/usr/bin/python3
"""
Displays a states list
"""
from flask import Flask, render_template
from models import storage
import sys
sys.path.append('../')

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ Display the templates of states in ascending order """
    states = storage.all("State")
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """ Close the session on teardown """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
