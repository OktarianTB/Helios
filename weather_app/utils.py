from csv import reader
from weather_app.config import Config
import requests
from ip2geotools.databases.noncommercial import DbIpCity


def get_all_countries():
    with open("weather_app/static/countries.csv") as csv_file:
        countries = [(row[1], row[0]) for row in reader(csv_file)]
    return countries


def get_country_from_id(country_id):
    countries = get_all_countries()
    for section in countries:
        if country_id in section:
            return section[1]


def get_host_country():
    ip_address = requests.get(Config.WHAT_IS_MY_IP).text
    response = DbIpCity.get(ip_address, api_key="free")
    return response.country
