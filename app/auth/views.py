# app/auth/views.py
# Written by Luke Grammer (12/19/19)

from flask import flash, render_template

from . import auth
from .forms import CustomForgotPasswordForm
from ..models import User


@auth.route('/forgot', methods=['GET', 'POST'])
def forgot():
    """
    Handle requests to the /forgot route
    Help the user reset a forgotten password
    """
    form = CustomForgotPasswordForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None:
            pass  # change this line later
        flash('A password reset request has been sent to ' + form.email.data)
    return render_template('auth/forgot.html', form=form,
                           title='Forgot Password')
