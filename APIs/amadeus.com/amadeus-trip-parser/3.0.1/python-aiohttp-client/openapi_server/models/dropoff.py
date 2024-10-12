# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.location import Location
from openapi_server import util


class Dropoff(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, local_date_time: str=None, location: Location=None):
        """Dropoff - a model defined in OpenAPI

        :param local_date_time: The local_date_time of this Dropoff.
        :param location: The location of this Dropoff.
        """
        self.openapi_types = {
            'local_date_time': str,
            'location': Location
        }

        self.attribute_map = {
            'local_date_time': 'localDateTime',
            'location': 'location'
        }

        self._local_date_time = local_date_time
        self._location = location

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Dropoff':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The dropoff of this Dropoff.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def local_date_time(self):
        """Gets the local_date_time of this Dropoff.

        local date and time compliant with ISO8601.

        :return: The local_date_time of this Dropoff.
        :rtype: str
        """
        return self._local_date_time

    @local_date_time.setter
    def local_date_time(self, local_date_time):
        """Sets the local_date_time of this Dropoff.

        local date and time compliant with ISO8601.

        :param local_date_time: The local_date_time of this Dropoff.
        :type local_date_time: str
        """

        self._local_date_time = local_date_time

    @property
    def location(self):
        """Gets the location of this Dropoff.


        :return: The location of this Dropoff.
        :rtype: Location
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this Dropoff.


        :param location: The location of this Dropoff.
        :type location: Location
        """

        self._location = location
