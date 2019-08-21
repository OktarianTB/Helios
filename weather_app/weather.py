import requests
from weather_app.config import Config


def get_weather(city, country=None):
    response = requests.get(Config.WEATHER_API_URL.format(f"{city},{country}", Config.WEATHER_API_KEY)).json()
    return response

