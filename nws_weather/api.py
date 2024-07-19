"""Utilities for the National Weather Service API"""

import requests

def index_for_point(latitude, longitude):

    """This has links to other data"""
    
    url = f"https://api.weather.gov/points/{latitude},{longitude}"

    return requests.get(
        url
    ).json()


def forecast_for_point(latitude, longitude):

    """Forecast endpoint data"""

    index_data = index_for_point(latitude, longitude)

    url = index_data["properties"]["forecast"]

    return requests.get(
        url
    ).json()


def hourly_forecast_for_point(latitude, longitude):

    """Hourly forecast endpoint data"""

    index_data = index_for_point(latitude, longitude)

    url = index_data["properties"]["forecastHourly"]

    return requests.get(
        url
    ).json()


def discussion_for_point(latitude, longitude):

    """Discussion endpoint data"""
    
    index_data = index_for_point(latitude, longitude)

    grid_id = index_data["properties"]["gridId"]
    url = f"https://api.weather.gov/products/types/AFD/locations/{grid_id}"
    
    discussion_index = requests.get(
        url
    ).json()

    latest_discussion_url = discussion_index["@graph"][0]["@id"]

    discussion_data = requests.get(
        latest_discussion_url
    ).json()

    return discussion_data

