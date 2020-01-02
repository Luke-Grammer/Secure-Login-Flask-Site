# app/auth/forms.py
# Written by Luke Grammer (12/19/19)

from wtforms import (PasswordField, StringField,
                     BooleanField, SubmitField, ValidationError)
from flask_security import (LoginForm, ConfirmRegisterForm,
                            ForgotPasswordForm, ResetPasswordForm)
from wtforms.validators import DataRequired, Email, EqualTo, Length
from ..models import User


class CustomRegisterForm(ConfirmRegisterForm):
    """
    Form for users to create new accounts
    """
    email = StringField('Organization Email Address', validators=[
        DataRequired(),
        Email()
    ])

    first_name = StringField('First Name', validators=[
        DataRequired()
    ])

    last_name = StringField('Last Name', validators=[
        DataRequired()
    ])

    password = PasswordField('Password', validators=[
        DataRequired(),
        Length(min=7, message="Password field must be at least 7" +
                              " characters long.")
    ])

    password_confirm = PasswordField('Confirm Password', validators=[
        EqualTo(fieldname='password', message="Passwords must match.")
    ])

    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email is already in use.')


class CustomLoginForm(LoginForm):
    """
    Form for users to login
    """
    email = StringField('Email', validators=[
        DataRequired(), Email()
    ])

    password = PasswordField('Password', validators=[
        DataRequired()
    ])

    remember = BooleanField('Remember me')

    submit = SubmitField('Login')


class CustomForgotPasswordForm(ForgotPasswordForm):
    email = StringField('Email Address', validators=[
        DataRequired(),
        Email()
    ])

    def validate_email(self, field):
        if not User.query.filter_by(email=field.data).first():
            raise ValidationError('Email is not associated with' +
                                  ' any user account.')

    submit = SubmitField('Reset Password')


class CustomResetPasswordForm(ResetPasswordForm):
    current_password = PasswordField('Current Password', validators=[
        DataRequired(),
        Length(min=7)
    ])
