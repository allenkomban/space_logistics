import os

"this is the relative path to our database"

local_db = 'sqlite:///sqlite_db/spaceship_location.db'

basedir = os.path.abspath(os.path.dirname(__file__))

class DevelopmentConfig():
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = local_db
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config_by_name = dict(development=DevelopmentConfig)

