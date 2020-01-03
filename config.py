# config.py
# Written by Luke Grammer (12/19/19)


class Config(object):
    """ Common Configurations """
    # Location for configurations common across environments
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECURITY_REGISTERABLE = True
    SECURITY_RECOVERABLE = True
    SECURITY_CONFIRMABLE = True
    SECURITY_EMAIL_SUBJECT_REGISTER = 'Welcome to the LLDB!'
    SECURITY_TOKEN_MAX_AGE = 3600
    SECURITY_MSG_PASSWORD_CHANGE = ('Your password has been changed ' +
                                    'successfully.', 'info')

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True


class DevelopmentConfig(Config):
    """ Development Configurations """
    DEBUG = True
    SQLALCHEMY_ECHO = True
    MAIL_DEBUG = True
    MAIL_USERNAME = 'lukeagrammer@gmail.com'
    MAIL_DEFAULT_SENDER = '"Lessons Learned Database" <noreply@gmail.com>'


class ProductionConfig(Config):
    """ Production Configurations """
    DEBUG = False
    MAIL_DEBUG = False


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
