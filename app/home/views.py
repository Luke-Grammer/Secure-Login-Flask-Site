# app/home/views.py
# Written by Luke Grammer (12/19/19)

# third-party imports
from flask import render_template
from flask_login import login_required

# local imports
from . import home


@home.route('/')
def homepage():
    """
    Render the homepage template on the '/' route
    """
    return render_template('home/index.html')


@home.route('/dashboard')
@login_required
def dashboard():
    """
    Render the dashboard template on the '/dashboard' route
    """
    return render_template('home/dashboard.html')
