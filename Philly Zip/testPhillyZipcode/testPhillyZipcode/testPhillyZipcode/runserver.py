"""
This script runs the testPhillyZipcode application using a development server.
"""

from os import environ
from flask import Flask, render_template, url_for, request
app = Flask(__name__)

@app.route('/')
def index(): # returns homepage
    return render_template("index.html")

@app.route('/preferences')
def preferences(): # returns page to select different preferences
    return render_template("preferences.html")

@app.route('/display')
def display(): # displays the data needed
    preferences_dict = dict()
    preferences_dict['libraries'] = request.args.get('libraries')
    preferences_dict['farmer_market'] = request.args.get('farmer_market')
    preferences_dict['healthcare'] = request.args.get('healthcare')
    preferences_dict['recreation'] = request.args.get('recreation')
    preferences_dict['pool'] = request.args.get('pool')
    preferences_dict['healthy_corner'] = request.args.get('healthy_corner')
    preferences_dict['parks'] = request.args.get('parks')
    preferences_dict['golf'] = request.args.get('golf')
    preferences_dict['police'] = request.args.get('police')
    preferences_dict['fire_department'] = request.args.get('fire_department')
    preferences_dict['litter'] = request.args.get('litter')

    #put function here that will talk to database

    return render_template("display.html")

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT, debug=True)
