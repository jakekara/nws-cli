
import configparser
import os
from textwrap import dedent

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