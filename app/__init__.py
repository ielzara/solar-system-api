from flask import Flask
from .db import db, migrate
from .models import planet
from .routes.planets_routes import bp as planets_bp
from .routes.moons_routes import bp as moons_bp
import os

def create_app(config=None):
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')

    if config:
        # Merge `config` into the app's configuration
        # to override the app's default settings for testing
        app.config.update(config)

    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints here
    app.register_blueprint(planets_bp)
    app.register_blueprint(moons_bp)
    
    return app
