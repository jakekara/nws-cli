
"""Command-line utility"""

import json
from nws_weather.api import discussion_for_point, forecast_for_point, index_for_point, hourly_forecast_for_point
from nws_weather.config import add_place_wizard, get_config, get_lat_lon

import argparse

from nws_weather.geocoder import geocode_census

def main():
   
   """Entrypoint for `nws` package script
   
   Sets up argument parser, subcommands
   """

   parser = argparse.ArgumentParser(
      description="National Weather Service Command Line Interface"
   )

   parser.add_argument("--location", default="default")
   parser.set_defaults(func=parser.print_help)

   subparsers = parser.add_subparsers(help="subcommand help")

   hourly = subparsers.add_parser("hourly")
   hourly.set_defaults(func=hourly_forecast)

   detailed = subparsers.add_parser("detailed")
   detailed.set_defaults(func=detailed_text_forecast)

   discussion = subparsers.add_parser("discussion")
   discussion.set_defaults(func=discussion_text)

   discussion = subparsers.add_parser("wizard")
   discussion.set_defaults(func=call_the_wizard)

   list_config = subparsers.add_parser("ls")
   list_config.set_defaults(func=list_places)


   geocode = subparsers.add_parser("geocode")
   geocode.add_argument("street")
   geocode.add_argument("city")
   geocode.add_argument("state")
   geocode.set_defaults(func=location_lookup)

   args = parser.parse_args()
   args.func(vars(args))


def list_places(args):
   """nws ls subcommand"""

   config = get_config()

   for section in config.sections():
      print(f"{section}")


def call_the_wizard(args):
   """nws wizard subcommand"""

   add_place_wizard()


def location_lookup(args):
   """nws geocode subcommand"""

   print(json.dumps(geocode_census(**args), indent=2))


def hourly_forecast(args):
   """nws hourly subcommand"""

   data = hourly_forecast_for_point(**get_lat_lon(**args))

   for period in data["properties"]["periods"][:24]:
      print(period["startTime"] + ": " + period["shortForecast"] + " T:" + str(period["temperature"]) + "F " + "H:" + str(period["relativeHumidity"]["value"]) + "%")


def detailed_text_forecast(args):
   """nws detailed subcommand"""

   data = forecast_for_point(**get_lat_lon(**args))
   for period in data["properties"]["periods"]:
      print(period["name"])
      print(period["detailedForecast"])
      print()

def discussion_text(args):
   """nws discussion subcommand"""
   
   data = discussion_for_point(**get_lat_lon(**args))
   print(data["productName"])
   print(data["issuanceTime"])
   print(data["@id"])
   print(data["productText"])

