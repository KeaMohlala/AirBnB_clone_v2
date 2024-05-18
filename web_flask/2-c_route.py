#!/usr/bin/python3
"""
script that starts Flask web application and routes it to
different pages of the hbnb website
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home_hbnb():
    """
    Returns message on home page
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Returns /hbnb page
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """
    returns c page and displays the info about the route
    on the page
    """
    return f"C {escape(text.replace('_', ' '))}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
