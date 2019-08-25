from flask import Flask, redirect, url_for
from weather_app.config import Config


def page_not_found(e):
    return redirect(url_for("weather.home"))


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    from weather_app.routes import weather
    app.register_blueprint(weather)

    app.register_error_handler(404, page_not_found)
    
    return app

