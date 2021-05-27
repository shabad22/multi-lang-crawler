# Start Importing Packages Statements
from dotenv import find_dotenv, load_dotenv
from flask.templating import render_template
from flask import (Flask, jsonify, request, session, g, redirect,
                   url_for, abort, render_template, flash)
import os

# End Importing Packages Statements

# Load Enviourment
load_dotenv(find_dotenv())

# Create Application
app = Flask(__name__) 

# Application Configration
app.config.from_object(__name__)  # load config from this file , flaskr.py
SECRET_KEY = os.environ.get("SECRET_KEY")

if not SECRET_KEY:
    raise ValueError("No SECRET_KEY set for Flask application")
app.config.update(
    # In order to use session in flask you need to set the secret key in your application settings.
    # Secret key is a random key used to encrypt your cookies and save, send them to the browser.
    SECRET_KEY = SECRET_KEY
    # User Name and Password for Login Page saved then as session variale
)

from app import routes
from app.crawler import Crawl


