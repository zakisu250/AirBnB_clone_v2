#!/usr/bin/python3
"""
Flask App that integrates with AirBnB static HTML Template
"""
from flask import Flask, render_template, url_for
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.user import User

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """
    after each request, this method calls .close() (i.e. .remove()) on
    the current SQLAlchemy Session
    """
    storage.close()


@app.route('/hbnb')
def hbnb_main(id=None, strict_slashes=False):
    """
    handles request to custom template with states, cities & amentities
    """
    states = storage.all(State).values()
    amens = storage.all(Amenity).values()
    place_dic = storage.all(Place).values()
    users = storage.all(User)
    places = []
    for key, val in users.items():
        for place in place_dic:
            if key == place.user_id:
                places.append(["{val.first_name} {val.last_name}", place])
    places.sort(key=lambda x: x[1].name)
    return render_template('100-hbnb.html', states=states, amens=amens,
                           places=places)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
