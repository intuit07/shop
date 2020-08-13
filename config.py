import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///shop.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True