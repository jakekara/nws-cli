import requests


def geocode_census(street, city, state):

    url = "https://geocoding.geo.census.gov/geocoder/locations/address"
    return requests.get(
        url,
        params={
            "street": street,
            "city": city,
            "state": state,
            "benchmark": "Public_AR_Current",
            "format": "json"

        }
    ).json()