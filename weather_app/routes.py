from flask import render_template, url_for, Blueprint, redirect, flash, request
from weather_app.form import AccessWeather
from weather_app.utils import get_all_countries, get_country_from_id, get_host_country
from weather_app.weather import get_weather_with_id

weather = Blueprint("weather", __name__)


@weather.route("/", methods=["GET", "POST"])
def home():
    form = AccessWeather()
    form.country.choices = get_all_countries()
    if request.method == 'GET':
        form.country.data = get_host_country()

    if form.validate_on_submit():
        city = form.city.data
        country_id = form.country.data
        return redirect(url_for("weather.result", city=city, country_id=country_id))
    return render_template("home.html", title="Helios - Home", form=form)


@weather.route("/result/<city>+<country_id>", methods=["GET", "POST"])
def result(city, country_id):
    response = get_weather_with_id(city, country_id)
    if not response:
        flash("Sorry! Our service is currently unavailable. Please try again later.", "danger")
        return redirect(url_for("weather.home"))
    elif response.get("cod") == "404":
        flash(f"Sorry! We can't find this location. Please try again. {country_id}", "danger")
        return redirect(url_for("weather.home"))
    country = get_country_from_id(country_id)
    return render_template("result.html", title="Helios - Weather", response=response, country_id=country_id, country=country)

