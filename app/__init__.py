from flask import Flask
from config.config import app_config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.json.sort_keys = False
    app.config.from_object(app_config[config_name])

    db.init_app(app)

    from app.views.home import home_blueprint
    from app.views.quem_somos import quem_somos_blueprint
    from app.views.contato import contato_blueprint

    app.register_blueprint(home_blueprint)
    app.register_blueprint(quem_somos_blueprint)
    app.register_blueprint(contato_blueprint)

    return app

