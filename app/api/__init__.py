from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    myapp = Flask(__name__)
    myapp.config.from_object(config_class)

    db.init_app(myapp)
    migrate.init_app(myapp, db)

    from app.api import routes, models

    return myapp



