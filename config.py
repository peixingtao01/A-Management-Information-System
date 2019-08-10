#1
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class BaseConfig(object):
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = os.urandom(24)

class DebugConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(BASE_DIR,'WSW.sqlite')
