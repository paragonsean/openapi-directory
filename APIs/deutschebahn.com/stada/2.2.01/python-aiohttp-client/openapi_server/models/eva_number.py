# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.geographic_point import GeographicPoint
from openapi_server import util


class EVANumber(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, geographic_coordinate: GeographicPoint=None, is_main: bool=None, number: int=None):
        """EVANumber - a model defined in OpenAPI

        :param geographic_coordinate: The geographic_coordinate of this EVANumber.
        :param is_main: The is_main of this EVANumber.
        :param number: The number of this EVANumber.
        """
        self.openapi_types = {
            'geographic_coordinate': GeographicPoint,
            'is_main': bool,
            'number': int
        }

        self.attribute_map = {
            'geographic_coordinate': 'geographicCoordinate',
            'is_main': 'isMain',
            'number': 'number'
        }

        self._geographic_coordinate = geographic_coordinate
        self._is_main = is_main
        self._number = number

    @classmethod
    def from_dict(cls, dikt: dict) -> 'EVANumber':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The EVANumber of this EVANumber.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def geographic_coordinate(self):
        """Gets the geographic_coordinate of this EVANumber.


        :return: The geographic_coordinate of this EVANumber.
        :rtype: GeographicPoint
        """
        return self._geographic_coordinate

    @geographic_coordinate.setter
    def geographic_coordinate(self, geographic_coordinate):
        """Sets the geographic_coordinate of this EVANumber.


        :param geographic_coordinate: The geographic_coordinate of this EVANumber.
        :type geographic_coordinate: GeographicPoint
        """

        self._geographic_coordinate = geographic_coordinate

    @property
    def is_main(self):
        """Gets the is_main of this EVANumber.

        station related EVA-Numbers

        :return: The is_main of this EVANumber.
        :rtype: bool
        """
        return self._is_main

    @is_main.setter
    def is_main(self, is_main):
        """Sets the is_main of this EVANumber.

        station related EVA-Numbers

        :param is_main: The is_main of this EVANumber.
        :type is_main: bool
        """

        self._is_main = is_main

    @property
    def number(self):
        """Gets the number of this EVANumber.

        EVA identifier

        :return: The number of this EVANumber.
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this EVANumber.

        EVA identifier

        :param number: The number of this EVANumber.
        :type number: int
        """

        self._number = number
