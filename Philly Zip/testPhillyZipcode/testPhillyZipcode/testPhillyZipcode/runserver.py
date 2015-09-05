"""
This script runs the testPhillyZipcode application using a development server.
"""

from os import environ
from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/preferences')
def preferences():
    return render_template("preferences.html")

@app.route('/display')
def display():
    return render_template("display.html")

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT, debug=True)
    print "hi"
