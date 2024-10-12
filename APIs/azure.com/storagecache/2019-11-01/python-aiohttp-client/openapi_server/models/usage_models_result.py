# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.usage_model import UsageModel
from openapi_server import util


class UsageModelsResult(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, next_link: str=None, value: List[UsageModel]=None):
        """UsageModelsResult - a model defined in OpenAPI

        :param next_link: The next_link of this UsageModelsResult.
        :param value: The value of this UsageModelsResult.
        """
        self.openapi_types = {
            'next_link': str,
            'value': List[UsageModel]
        }

        self.attribute_map = {
            'next_link': 'nextLink',
            'value': 'value'
        }

        self._next_link = next_link
        self._value = value

    @classmethod
    def from_dict(cls, dikt: dict) -> 'UsageModelsResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The UsageModelsResult of this UsageModelsResult.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def next_link(self):
        """Gets the next_link of this UsageModelsResult.

        The URI to fetch the next page of Cache usage models.

        :return: The next_link of this UsageModelsResult.
        :rtype: str
        """
        return self._next_link

    @next_link.setter
    def next_link(self, next_link):
        """Sets the next_link of this UsageModelsResult.

        The URI to fetch the next page of Cache usage models.

        :param next_link: The next_link of this UsageModelsResult.
        :type next_link: str
        """

        self._next_link = next_link

    @property
    def value(self):
        """Gets the value of this UsageModelsResult.

        The list of usage models available for the subscription.

        :return: The value of this UsageModelsResult.
        :rtype: List[UsageModel]
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this UsageModelsResult.

        The list of usage models available for the subscription.

        :param value: The value of this UsageModelsResult.
        :type value: List[UsageModel]
        """

        self._value = value
