import os

"""
    DB Connection URl
    To connect to db replace below local_db with your own db url
    'sqlite:///folder_name/database_name.db'
"""

local_db = 'sqlite:///sqlite_db/stomble.db'

basedir = os.path.abspath(os.path.dirname(__file__))

class DevelopmentConfig():
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = local_db
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config_by_name = dict(development=DevelopmentConfig)

