#!/usr/bin/python3
"""
script that starts Flask web application and routes it to
different pages of the hbnb website
"""
from flask import Flask
from markupsafe import escape
from flask import render_template


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


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_route(text="is cool"):
    """
    returns python page and displays info about the route
    """
    return f"Python {escape(text.replace('_', ' '))}"


@app.route("/number/<int:n>", strict_slashes=False)
def number_route(n):
    """
    returns statement if file is an integer
    """
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """
    renders template information
    """
    return render_template("5-number.html", number=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
