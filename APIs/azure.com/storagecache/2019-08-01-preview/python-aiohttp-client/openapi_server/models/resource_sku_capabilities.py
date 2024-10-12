# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ResourceSkuCapabilities(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name: str=None, value: str=None):
        """ResourceSkuCapabilities - a model defined in OpenAPI

        :param name: The name of this ResourceSkuCapabilities.
        :param value: The value of this ResourceSkuCapabilities.
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
    def from_dict(cls, dikt: dict) -> 'ResourceSkuCapabilities':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ResourceSkuCapabilities of this ResourceSkuCapabilities.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this ResourceSkuCapabilities.

        Name of a capability, such as ops/sec

        :return: The name of this ResourceSkuCapabilities.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ResourceSkuCapabilities.

        Name of a capability, such as ops/sec

        :param name: The name of this ResourceSkuCapabilities.
        :type name: str
        """

        self._name = name

    @property
    def value(self):
        """Gets the value of this ResourceSkuCapabilities.

        Quantity, if the capability is measured by quantity

        :return: The value of this ResourceSkuCapabilities.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ResourceSkuCapabilities.

        Quantity, if the capability is measured by quantity

        :param value: The value of this ResourceSkuCapabilities.
        :type value: str
        """

        self._value = value
