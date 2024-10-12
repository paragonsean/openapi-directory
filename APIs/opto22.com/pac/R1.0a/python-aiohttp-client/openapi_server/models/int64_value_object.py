# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Int64ValueObject(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, value: int=None):
        """Int64ValueObject - a model defined in OpenAPI

        :param value: The value of this Int64ValueObject.
        """
        self.openapi_types = {
            'value': int
        }

        self.attribute_map = {
            'value': 'value'
        }

        self._value = value

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Int64ValueObject':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Int64ValueObject of this Int64ValueObject.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def value(self):
        """Gets the value of this Int64ValueObject.

        Value of the integer64 variable

        :return: The value of this Int64ValueObject.
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Int64ValueObject.

        Value of the integer64 variable

        :param value: The value of this Int64ValueObject.
        :type value: int
        """

        self._value = value
