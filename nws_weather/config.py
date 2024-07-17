
import configparser
import os
from textwrap import dedent

from nws_weather.geocoder import geocode_census
from nws_weather.sample_data import BETHEL_CT

DEFAULT_CONFIG_FILE_PATH="~/.nws-py.config"

def get_lat_lon(section="default", config_file_path=DEFAULT_CONFIG_FILE_PATH):

    """Load lat on from config file. Default to Bethel, CT as a location if
    none is specified."""

    try:

        config = configparser.ConfigParser()
        config.read(os.path.expanduser(config_file_path))

        lat = config[section]['latitude']
        lon = config[section]['longitude']

        return {
            "latitude": lat,
            "longitude": lon
        }

    except:
        return BETHEL_CT
    
def add_place_wizard(*args):
    print(dedent(
        """
        Add place wizard not implemented. For now, create a file
        at ~/.nws-py.config like this:

        [default]
        latitude = 41.3717
        longitude = -73.4074

        [somewhere-else]
        latitude = 42.3717
        longitude = -73.4074
        """
        ))
    

def add_place_wizard_auto():

    if not os.path.exists(os.path.expanduser(DEFAULT_CONFIG_FILE_PATH)):
        print(f"Could not find default config file at {DEFAULT_CONFIG_FILE_PATH}. File will be created by this wizard.")
        with open(os.path.expanduser(DEFAULT_CONFIG_FILE_PATH), "w") as fh:
            pass

    print("We need to add a default location. Please enter your location.")
    print("NOTE: Data will be sent to a U.S. Census Bureau API for geocoding.")
    print()
    
    print("type 'q' to quit")

    street = input("Street: ")
    if street.strip() == "q": return
    city = input("City: ")
    if city.strip() == "q": return
    state = input("State: ")
    if state.strip() == "q": return

    data = geocode_census(street, city, state)

    if "errors" in data:
        for error in data["errors"]:
            print(error)
        return

    matches = data["result"]["addressMatches"]

    if len(matches) < 1:
        print("Found no matches. Try again.")
        return add_place_wizard_auto()

    print()
    print(f"Found {len(matches)} matches. Choose one:")

    for idx, match in enumerate(matches):
        lat = match["coordinates"]["y"]
        lon = match["coordinates"]["x"]
        print(str(idx) + ": " + match["matchedAddress"] + f"({lat}, {lon})")

    print(f"{idx + 1}: None of the above")
    print()
    print("Choose one of the addresses above")

    selection = int(input("Selection: "))
    if selection >= 0 and selection < len(matches):
        choice = matches[selection]
    elif selection == (idx + 1):
        print("You chose none of the above. Goodbye!")
        return
    else:
        print("Invalid selection. Goodbye!")

    print(f"You chose: {choice['matchedAddress']}")
    print("Let's set up your config file")

    config = configparser.ConfigParser()
    config.read(os.path.expanduser(DEFAULT_CONFIG_FILE_PATH))

    sections = config.sections()
    if len(sections) > 0:
        print()
        print("Found the following places in your config file:")
        print("\n".join(sections))

    default = input("Do you want to make this the default location? (y/Y) ").lower() == "y"

    latitude = choice["coordinates"]["y"]
    longitude = choice["coordinates"]["x"]

    if default:
        section_name = "default"
    else:
        print()
        section_name = input("Please enter a name for this location: ")

    config[section_name] = {
        "latitude": latitude,
        "longitude": longitude,
        "address": match["matchedAddress"]
    }

    with open(os.path.expanduser(DEFAULT_CONFIG_FILE_PATH), "w") as fh:
        config.write(fh)

    print("Choices saved!")