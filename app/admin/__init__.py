# app/admin/__init__.py
# Written by Luke Grammer (12/19/19)

from flask import Blueprint

admin = Blueprint('admin', __name__)

from . import views
