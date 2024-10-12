# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.resource_operation import ResourceOperation
from openapi_server import util


class AvailableOperations(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, value: List[ResourceOperation]=None):
        """AvailableOperations - a model defined in OpenAPI

        :param value: The value of this AvailableOperations.
        """
        self.openapi_types = {
            'value': List[ResourceOperation]
        }

        self.attribute_map = {
            'value': 'value'
        }

        self._value = value

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AvailableOperations':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The AvailableOperations of this AvailableOperations.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def value(self):
        """Gets the value of this AvailableOperations.

        An array of available operations

        :return: The value of this AvailableOperations.
        :rtype: List[ResourceOperation]
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this AvailableOperations.

        An array of available operations

        :param value: The value of this AvailableOperations.
        :type value: List[ResourceOperation]
        """

        self._value = value
