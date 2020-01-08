# app/home/__init__.py
# Written by Luke Grammer (12/19/19)

from flask import Blueprint

home = Blueprint('home', __name__)

from . import views
