# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class StringVar(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name: str=None, value: str=None):
        """StringVar - a model defined in OpenAPI

        :param name: The name of this StringVar.
        :param value: The value of this StringVar.
        """
        self.openapi_types = {
            'name': str,
            'value': str
        }

        self.attribute_map = {
            'name': 'name',
            'value': 'value'
        }

        self._name = name
        self._value = value

    @classmethod
    def from_dict(cls, dikt: dict) -> 'StringVar':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The StringVar of this StringVar.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this StringVar.

        Name of the tag (strategy variable, i/o point, etc.)

        :return: The name of this StringVar.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StringVar.

        Name of the tag (strategy variable, i/o point, etc.)

        :param name: The name of this StringVar.
        :type name: str
        """
        if name is not None and len(name) > 50:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `50`")

        self._name = name

    @property
    def value(self):
        """Gets the value of this StringVar.

        The value of a string; string width (max length) for each string variable is defined in the strategy

        :return: The value of this StringVar.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this StringVar.

        The value of a string; string width (max length) for each string variable is defined in the strategy

        :param value: The value of this StringVar.
        :type value: str
        """
        if value is not None and len(value) > 1024:
            raise ValueError("Invalid value for `value`, length must be less than or equal to `1024`")

        self._value = value
