import requests
from weather_app.config import Config


def get_weather_with_id(city, country=None):
    try:
        response = requests.get(Config.WEATHER_API_URL.format(f"{city},{country}", Config.WEATHER_API_KEY)).json()
    except Exception:
        response = None
    return response
