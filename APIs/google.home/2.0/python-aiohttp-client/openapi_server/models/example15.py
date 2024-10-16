# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Example15(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, display_string: str=None, locale: str=None):
        """Example15 - a model defined in OpenAPI

        :param display_string: The display_string of this Example15.
        :param locale: The locale of this Example15.
        """
        self.openapi_types = {
            'display_string': str,
            'locale': str
        }

        self.attribute_map = {
            'display_string': 'display_string',
            'locale': 'locale'
        }

        self._display_string = display_string
        self._locale = locale

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Example15':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Example15 of this Example15.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def display_string(self):
        """Gets the display_string of this Example15.


        :return: The display_string of this Example15.
        :rtype: str
        """
        return self._display_string

    @display_string.setter
    def display_string(self, display_string):
        """Sets the display_string of this Example15.


        :param display_string: The display_string of this Example15.
        :type display_string: str
        """
        if display_string is None:
            raise ValueError("Invalid value for `display_string`, must not be `None`")

        self._display_string = display_string

    @property
    def locale(self):
        """Gets the locale of this Example15.


        :return: The locale of this Example15.
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this Example15.


        :param locale: The locale of this Example15.
        :type locale: str
        """
        if locale is None:
            raise ValueError("Invalid value for `locale`, must not be `None`")

        self._locale = locale
