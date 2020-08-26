import os
from flask import Flask

import config
from .database import db
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(config.Config)

    db.init_app(app)
    with app.test_request_context():
        db.create_all()

    if app.debug == True:
        try:
            from flask_debugtoolbar import DebugToolbarExtension
            toolbar = DebugToolbarExtension(app)
        except:
            pass

    import app.firstmodule.controllers as firstmodule

    app.register_blueprint(firstmodule.module)

    return app
