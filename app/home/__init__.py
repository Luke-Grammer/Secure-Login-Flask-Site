# app/home/__init__.py
# Written by Luke Grammer (12/19/19)

# third-party imports
from flask import Blueprint

home = Blueprint('home', __name__)

# local imports
from . import views
