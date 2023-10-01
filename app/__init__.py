from flask import Flask
from config.config import app_config


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])

    from app.routes.home import home_blueprint
    from app.routes.quem_somos import quem_somos_blueprint
    from app.routes.contato import contato_blueprint

    app.register_blueprint(home_blueprint)
    app.register_blueprint(quem_somos_blueprint)
    app.register_blueprint(contato_blueprint)

    return app
