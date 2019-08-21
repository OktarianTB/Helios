from flask import Flask
from weather_app.config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    from weather_app.routes import weather
    app.register_blueprint(weather)
    
    return app

