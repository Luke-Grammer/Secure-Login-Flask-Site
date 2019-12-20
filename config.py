# config.py
# Written by Luke Grammer (12/19/19)


class Config(object):
    """ Common Configurations """
    # Location for configurations common across environments
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    """ Development Configurations """
    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    """ Production Configurations """
    DEBUG = False


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
