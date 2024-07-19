"""Geocoding utilities"""

import requests


def geocode_census(street, city, state, *args, **kwargs):

    """Geocode a street address via the U.S. Census Bureau API"""

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