# app/home/views.py
# Written by Luke Grammer (12/19/19)

# third-party imports
from flask import abort, redirect, url_for, render_template
from flask_security import current_user, login_required

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

    if current_user.admin:
        return redirect(url_for('home.admin_dashboard'))

    return render_template('home/dashboard.html')


@home.route('/admin/dashboard')
@login_required
def admin_dashboard():
    if not current_user.admin:
        abort(403)

    return render_template('home/admin_dashboard.html')
