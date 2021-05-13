import os


class Config(object):
    """Parent configuration class."""
    DEBUG = False
    SECRET = os.getenv('SECRET')
    MONGO_URI = 'mongodb://' + os.environ['MONGODB_USERNAME'] + ':' + \
                os.environ['MONGODB_PASSWORD'] + '@' + \
                os.environ['MONGODB_HOSTNAME'] + ':27017/' +\
                os.environ['MONGODB_DATABASE']
    CELERY_BROKER_URL = 'redis://localhost:6379',
    CELERY_RESULT_BACKEND = 'redis://localhost:6379'


class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True


class TestingConfig(Config):
    """Configurations for Testing"""
    TESTING = True
    DEBUG = True


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig
}
