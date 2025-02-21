#!/usr/bin/python3
"""
This script starts a server at 0.0.0.0 on port 5000
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ Returns string Hello """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Returns a simple string for the route """
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
