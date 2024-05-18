#!/usr/bin/python3
"""
file to make webflask directory a package and to initiate Flask
"""
from flask import Flask
app = Flask(__name__)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
