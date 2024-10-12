# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Location(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, location: str=None):
        """Location - a model defined in OpenAPI

        :param location: The location of this Location.
        """
        self.openapi_types = {
            'location': str
        }

        self.attribute_map = {
            'location': 'location'
        }

        self._location = location

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Location':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Location of this Location.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def location(self):
        """Gets the location of this Location.

        Url for item

        :return: The location of this Location.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this Location.

        Url for item

        :param location: The location of this Location.
        :type location: str
        """
        if location is None:
            raise ValueError("Invalid value for `location`, must not be `None`")

        self._location = location
