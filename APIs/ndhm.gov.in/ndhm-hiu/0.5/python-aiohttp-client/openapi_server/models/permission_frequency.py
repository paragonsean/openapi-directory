# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class PermissionFrequency(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, repeats: int=None, unit: str=None, value: int=None):
        """PermissionFrequency - a model defined in OpenAPI

        :param repeats: The repeats of this PermissionFrequency.
        :param unit: The unit of this PermissionFrequency.
        :param value: The value of this PermissionFrequency.
        """
        self.openapi_types = {
            'repeats': int,
            'unit': str,
            'value': int
        }

        self.attribute_map = {
            'repeats': 'repeats',
            'unit': 'unit',
            'value': 'value'
        }

        self._repeats = repeats
        self._unit = unit
        self._value = value

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PermissionFrequency':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Permission_frequency of this PermissionFrequency.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def repeats(self):
        """Gets the repeats of this PermissionFrequency.


        :return: The repeats of this PermissionFrequency.
        :rtype: int
        """
        return self._repeats

    @repeats.setter
    def repeats(self, repeats):
        """Sets the repeats of this PermissionFrequency.


        :param repeats: The repeats of this PermissionFrequency.
        :type repeats: int
        """
        if repeats is None:
            raise ValueError("Invalid value for `repeats`, must not be `None`")

        self._repeats = repeats

    @property
    def unit(self):
        """Gets the unit of this PermissionFrequency.


        :return: The unit of this PermissionFrequency.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this PermissionFrequency.


        :param unit: The unit of this PermissionFrequency.
        :type unit: str
        """
        allowed_values = ["HOUR", "WEEK", "DAY", "MONTH", "YEAR"]  # noqa: E501
        if unit not in allowed_values:
            raise ValueError(
                "Invalid value for `unit` ({0}), must be one of {1}"
                .format(unit, allowed_values)
            )

        self._unit = unit

    @property
    def value(self):
        """Gets the value of this PermissionFrequency.


        :return: The value of this PermissionFrequency.
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this PermissionFrequency.


        :param value: The value of this PermissionFrequency.
        :type value: int
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")

        self._value = value
