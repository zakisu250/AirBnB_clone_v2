#!/usr/bin/python3
"""
    Sript that starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)

@app.teardown_appcontext
def teardown_db(self):
    """
        method to handle teardown
    """
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def filters_list():
    """
        method to display html page 6-index.html
    """
    states = storage.all(State).values()
    amens = storage.all(Amenity).values()
    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amens)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
