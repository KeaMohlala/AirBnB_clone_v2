#!/usr/bin/python3
"""
script that starts Flask web application and routes it to home page
"""
from. import app


@app.route('/', strict_slashes=false)
def hello_hbnb():
    """
    Returns message on home page
    """
    return "Hello HBNB!"
