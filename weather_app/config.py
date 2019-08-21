import os


class Config:
    WEATHER_API_KEY = os.environ.get("WEATHER_API_KEY")
    WEATHER_API_URL = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&mode=json&appid={}"
    SECRET_KEY = os.environ.get("SECRET_KEY")