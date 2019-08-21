from flask import render_template, url_for, Blueprint, redirect
from weather_app.form import AccessWeather
from weather_app.utils import get_all_countries
from weather_app.weather import get_weather

weather = Blueprint("weather", __name__)


@weather.route("/", methods=["GET", "POST"])
def home():
    form = AccessWeather()
    form.country.choices = get_all_countries()
    if form.validate_on_submit():
        city = form.city.data
        country_id = form.country.data
        return redirect(url_for("weather.result", city=city, country_id=country_id))
    return render_template("home.html", title="Helios - Home", form=form)


@weather.route("/result/<city>+<country_id>", methods=["GET", "POST"])
def result(city, country_id):
    response = get_weather(city, country_id)
    return render_template("result.html", title="Helios - Weather", response=response)