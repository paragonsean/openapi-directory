# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Regionalbereich(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name: str=None, number: int=None, short_name: str=None):
        """Regionalbereich - a model defined in OpenAPI

        :param name: The name of this Regionalbereich.
        :param number: The number of this Regionalbereich.
        :param short_name: The short_name of this Regionalbereich.
        """
        self.openapi_types = {
            'name': str,
            'number': int,
            'short_name': str
        }

        self.attribute_map = {
            'name': 'name',
            'number': 'number',
            'short_name': 'shortName'
        }

        self._name = name
        self._number = number
        self._short_name = short_name

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Regionalbereich':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Regionalbereich of this Regionalbereich.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this Regionalbereich.

        name of the regional department

        :return: The name of this Regionalbereich.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Regionalbereich.

        name of the regional department

        :param name: The name of this Regionalbereich.
        :type name: str
        """

        self._name = name

    @property
    def number(self):
        """Gets the number of this Regionalbereich.

        unique identifier of the regional department

        :return: The number of this Regionalbereich.
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this Regionalbereich.

        unique identifier of the regional department

        :param number: The number of this Regionalbereich.
        :type number: int
        """

        self._number = number

    @property
    def short_name(self):
        """Gets the short_name of this Regionalbereich.


        :return: The short_name of this Regionalbereich.
        :rtype: str
        """
        return self._short_name

    @short_name.setter
    def short_name(self, short_name):
        """Sets the short_name of this Regionalbereich.


        :param short_name: The short_name of this Regionalbereich.
        :type short_name: str
        """

        self._short_name = short_name
