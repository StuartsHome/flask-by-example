"""
Often there are things that are going to be different between your local,
staging, and production setups. You'll want to connect different databases,
have different AWS keys, etc. 
A config file allows you to deal with the different environments.
"""

# Like Django, we'll have a base config class that other config classes inherit from

import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    # Add SQLALCHEMY_DATABASE_URI field to the Config() class in your config.py file
    # to set your app to use the newly created database in development (local), staging, and production:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

class ProductionConfig(Config):
    DEBUG = False

class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    TESTING = True


class sss(Config):
    TESTING = True