# app/__init__.py
# Written by Luke Grammer (12/19/19)

# local imports
from config import app_config

# third-party imports
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore

# db variable initialization
db = SQLAlchemy()

# login manager variable initialization
login_manager = LoginManager()

from app import models
user_datastore = SQLAlchemyUserDatastore(db, models.User, models.Role)


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    Bootstrap(app)
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_message = 'You must be logged in to access this page.'
    login_manager.login_view = 'auth.login'
    migrate = Migrate(app, db)

    from instance.config import PASSWORD_SALT, MAIL_PASSWORD
    app.config['MAIL_PASSWORD'] = MAIL_PASSWORD

    mail = Mail(app)

    with app.app_context():
        db.create_all()

    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    from app.auth.forms import (CustomLoginForm, CustomRegisterForm,
                                CustomForgotPasswordForm,
                                CustomResetPasswordForm)
    app.config['SECURITY_PASSWORD_SALT'] = PASSWORD_SALT
    app.config['SECURITY_MSG_PASSWORD_CHANGE'] = ('Your password has been changed ' +
                                                  'successfully. \nYou may now log in.',
                                                  'success')
    security = Security(app, user_datastore,
                        confirm_register_form=CustomRegisterForm,
                        forgot_password_form=CustomForgotPasswordForm,
                        reset_password_form=CustomResetPasswordForm,
                        register_form=CustomRegisterForm,
                        login_form=CustomLoginForm)

    return app
