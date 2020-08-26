from flask_migrate import Migrate
from flask_script import Manager
from flask import Flask
import config

from app import create_app
from app.database import db

app = create_app()
app.config.from_object(config.Config)
manager = Manager(app)
# migrate = Migrate(app, db)


# @app.route('/')
# def index():
#     return 'Hello World'


if __name__ == '__main__':
    manager.run()
