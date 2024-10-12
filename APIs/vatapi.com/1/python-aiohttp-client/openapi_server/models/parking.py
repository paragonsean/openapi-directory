# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Parking(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, applies_to: str=None, value: int=None):
        """Parking - a model defined in OpenAPI

        :param applies_to: The applies_to of this Parking.
        :param value: The value of this Parking.
        """
        self.openapi_types = {
            'applies_to': str,
            'value': int
        }

        self.attribute_map = {
            'applies_to': 'applies_to',
            'value': 'value'
        }

        self._applies_to = applies_to
        self._value = value

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Parking':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The parking of this Parking.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def applies_to(self):
        """Gets the applies_to of this Parking.

        The type of goods the rate applies to

        :return: The applies_to of this Parking.
        :rtype: str
        """
        return self._applies_to

    @applies_to.setter
    def applies_to(self, applies_to):
        """Sets the applies_to of this Parking.

        The type of goods the rate applies to

        :param applies_to: The applies_to of this Parking.
        :type applies_to: str
        """
        if applies_to is None:
            raise ValueError("Invalid value for `applies_to`, must not be `None`")

        self._applies_to = applies_to

    @property
    def value(self):
        """Gets the value of this Parking.

        The % VAT rate

        :return: The value of this Parking.
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Parking.

        The % VAT rate

        :param value: The value of this Parking.
        :type value: int
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")

        self._value = value
