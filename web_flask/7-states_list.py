#!/usr/bin/python3
"""
script to set up Flask and creating templates to display
dynamic content fetched from the database
"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


@app.teardown_appcontext
def remove_session(_: None):
    """
    remove SQLAlchemy Session after each request
    """
    storage.close()


@app.route("/states_list", strict_slashes=False)
def state_list():
    """
    function to create HTML template to list
    states
    """
    states = storage.all(cls=State).values()
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
