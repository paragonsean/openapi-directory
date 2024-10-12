# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.database_usage import DatabaseUsage
from openapi_server import util


class DatabaseUsageListResult(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, value: List[DatabaseUsage]=None):
        """DatabaseUsageListResult - a model defined in OpenAPI

        :param value: The value of this DatabaseUsageListResult.
        """
        self.openapi_types = {
            'value': List[DatabaseUsage]
        }

        self.attribute_map = {
            'value': 'value'
        }

        self._value = value

    @classmethod
    def from_dict(cls, dikt: dict) -> 'DatabaseUsageListResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The DatabaseUsageListResult of this DatabaseUsageListResult.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def value(self):
        """Gets the value of this DatabaseUsageListResult.

        The list of database usages for the database.

        :return: The value of this DatabaseUsageListResult.
        :rtype: List[DatabaseUsage]
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this DatabaseUsageListResult.

        The list of database usages for the database.

        :param value: The value of this DatabaseUsageListResult.
        :type value: List[DatabaseUsage]
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")

        self._value = value
