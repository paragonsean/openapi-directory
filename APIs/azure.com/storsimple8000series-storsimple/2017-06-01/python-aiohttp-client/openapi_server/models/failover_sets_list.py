# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.failover_set import FailoverSet
from openapi_server import util


class FailoverSetsList(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, value: List[FailoverSet]=None):
        """FailoverSetsList - a model defined in OpenAPI

        :param value: The value of this FailoverSetsList.
        """
        self.openapi_types = {
            'value': List[FailoverSet]
        }

        self.attribute_map = {
            'value': 'value'
        }

        self._value = value

    @classmethod
    def from_dict(cls, dikt: dict) -> 'FailoverSetsList':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The FailoverSetsList of this FailoverSetsList.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def value(self):
        """Gets the value of this FailoverSetsList.

        The list of failover sets.

        :return: The value of this FailoverSetsList.
        :rtype: List[FailoverSet]
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this FailoverSetsList.

        The list of failover sets.

        :param value: The value of this FailoverSetsList.
        :type value: List[FailoverSet]
        """

        self._value = value
