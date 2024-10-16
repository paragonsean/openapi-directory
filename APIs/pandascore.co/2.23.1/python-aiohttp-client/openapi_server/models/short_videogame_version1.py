# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
import re
from openapi_server import util


class ShortVideogameVersion1(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, current: bool=None, name: str=None):
        """ShortVideogameVersion1 - a model defined in OpenAPI

        :param current: The current of this ShortVideogameVersion1.
        :param name: The name of this ShortVideogameVersion1.
        """
        self.openapi_types = {
            'current': bool,
            'name': str
        }

        self.attribute_map = {
            'current': 'current',
            'name': 'name'
        }

        self._current = current
        self._name = name

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ShortVideogameVersion1':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ShortVideogameVersion_1 of this ShortVideogameVersion1.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def current(self):
        """Gets the current of this ShortVideogameVersion1.

        Whether this videogame version is current

        :return: The current of this ShortVideogameVersion1.
        :rtype: bool
        """
        return self._current

    @current.setter
    def current(self, current):
        """Sets the current of this ShortVideogameVersion1.

        Whether this videogame version is current

        :param current: The current of this ShortVideogameVersion1.
        :type current: bool
        """
        if current is None:
            raise ValueError("Invalid value for `current`, must not be `None`")

        self._current = current

    @property
    def name(self):
        """Gets the name of this ShortVideogameVersion1.


        :return: The name of this ShortVideogameVersion1.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShortVideogameVersion1.


        :param name: The name of this ShortVideogameVersion1.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")
        if name is not None and not re.search(r'^[0-9]+\.[0-9]+\.[0-9]+$', name):
            raise ValueError("Invalid value for `name`, must be a follow pattern or equal to `/^[0-9]+\.[0-9]+\.[0-9]+$/`")

        self._name = name
