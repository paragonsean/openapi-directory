# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Roadsegment(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, coordinates: List[List[float]]=None, type: str=None):
        """Roadsegment - a model defined in OpenAPI

        :param coordinates: The coordinates of this Roadsegment.
        :param type: The type of this Roadsegment.
        """
        self.openapi_types = {
            'coordinates': List[List[float]],
            'type': str
        }

        self.attribute_map = {
            'coordinates': 'coordinates',
            'type': 'type'
        }

        self._coordinates = coordinates
        self._type = type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Roadsegment':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Roadsegment of this Roadsegment.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def coordinates(self):
        """Gets the coordinates of this Roadsegment.


        :return: The coordinates of this Roadsegment.
        :rtype: List[List[float]]
        """
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        """Sets the coordinates of this Roadsegment.


        :param coordinates: The coordinates of this Roadsegment.
        :type coordinates: List[List[float]]
        """
        if coordinates is None:
            raise ValueError("Invalid value for `coordinates`, must not be `None`")

        self._coordinates = coordinates

    @property
    def type(self):
        """Gets the type of this Roadsegment.


        :return: The type of this Roadsegment.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Roadsegment.


        :param type: The type of this Roadsegment.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type
