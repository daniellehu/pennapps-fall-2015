"""
This script runs the testPhillyZipcode application using a development server.
"""

from os import environ
from testPhillyZipcode import app
from flask import render_template, url_for


if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/preferences')
def preferences():
    return render_template("preferences.html")

@app.route('/display')
def display():
    return render_template("display.html")