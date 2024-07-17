
import json
from nws_weather.api import discussion_for_point, forecast_for_point, forecast_index_for_point, hourly_forecast_for_point
from nws_weather.config import add_place_wizard, add_place_wizard_auto, get_lat_lon

import argparse

from nws_weather.geocoder import geocode_census

def main():
   parser = argparse.ArgumentParser(
      description="Simple NWS weather reader"
   )

   subparsers = parser.add_subparsers(help="subcommand help")

   hourly = subparsers.add_parser("hourly")
   hourly.set_defaults(func=hourly_forecast)

   detailed = subparsers.add_parser("detailed")
   detailed.set_defaults(func=detailed_text_forecast)

   discussion = subparsers.add_parser("discussion")
   discussion.set_defaults(func=discussion_text)


   discussion = subparsers.add_parser("wizard")
   discussion.set_defaults(func=call_the_wizard)

   geocode = subparsers.add_parser("geocode")
   geocode.add_argument("street")
   geocode.add_argument("city")
   geocode.add_argument("state")
   geocode.set_defaults(func=location_lookup)

   args = parser.parse_args()
   args.func(args)


def call_the_wizard(args):
   add_place_wizard_auto()


def location_lookup(args):
   print(json.dumps(geocode_census(args.street, args.city, args.state), indent=2))

def forecast_index():
  
  print(json.dumps(
        forecast_index_for_point(**get_lat_lon()),
        indent=2
        ))
  


def hourly_forecast(args):
   data = hourly_forecast_for_point(**get_lat_lon())

   for period in data["properties"]["periods"][:24]:
      print(period["startTime"] + ": " + period["shortForecast"] + " T:" + str(period["temperature"]) + "F " + "H:" + str(period["relativeHumidity"]["value"]) + "%")

def forecast():
   print(json.dumps(
      forecast_for_point(**get_lat_lon()),
      indent=2
   ))


def detailed_text_forecast(args):
   data = forecast_for_point(**get_lat_lon())
   for period in data["properties"]["periods"]:
      print(period["name"])
      print(period["detailedForecast"])
      print()

def discussion_text(args):
   data = discussion_for_point(**get_lat_lon())
   print(data["productName"])
   print(data["issuanceTime"])
   print(data["@id"])
   print(data["productText"])

