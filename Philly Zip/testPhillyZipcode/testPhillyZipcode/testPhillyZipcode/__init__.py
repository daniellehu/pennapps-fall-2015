"""
The flask application package.
"""

import config

from flask import Flask
app = Flask(__name__)
app.config.from_pyfile('config.py')
import testPhillyZipcode.views
