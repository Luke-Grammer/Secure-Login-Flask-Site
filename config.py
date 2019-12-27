# config.py
# Written by Luke Grammer (12/19/19)


class Config(object):
    """ Common Configurations """
    # Location for configurations common across environments
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECURITY_REGISTERABLE = True
    MAIL_SERVER = 'smtp-mail.outlook.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False,
    MAIL_USE_SSL = True,


class DevelopmentConfig(Config):
    """ Development Configurations """
    DEBUG = True
    SQLALCHEMY_ECHO = True
    MAIL_DEBUG = True
    MAIL_USERNAME = 'luke.grammer@hotmail.com',


class ProductionConfig(Config):
    """ Production Configurations """
    DEBUG = False
    MAIL_DEBUG = False


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
