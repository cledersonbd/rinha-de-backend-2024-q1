import os 
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.pool import QueuePool

database = SQLAlchemy()

class Config():
    SECRET_KEY='dev'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_size': 30
    }
    
class DevConfig(Config):
    DB_URL='db'
    DB_NAME='rinha'
    DB_USER='admin'
    DB_PASSWORD='rinha2024q1'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{}:{}@{}:5432/{}'.format(DB_USER, DB_PASSWORD, DB_URL, DB_NAME)
    # SQLALCHEMY_DATABASE_URI = os.getenv('RINHA_DEV_DB_URL')
    JWT_SECRET_KEY = 'DontUseIt'
    JWT_BLACKLIST_ENABLED = True

