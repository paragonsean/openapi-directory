# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.redis_resource import RedisResource
from openapi_server import util


class RedisListResult(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, next_link: str=None, value: List[RedisResource]=None):
        """RedisListResult - a model defined in OpenAPI

        :param next_link: The next_link of this RedisListResult.
        :param value: The value of this RedisListResult.
        """
        self.openapi_types = {
            'next_link': str,
            'value': List[RedisResource]
        }

        self.attribute_map = {
            'next_link': 'nextLink',
            'value': 'value'
        }

        self._next_link = next_link
        self._value = value

    @classmethod
    def from_dict(cls, dikt: dict) -> 'RedisListResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The RedisListResult of this RedisListResult.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def next_link(self):
        """Gets the next_link of this RedisListResult.

        Link for next set of locations.

        :return: The next_link of this RedisListResult.
        :rtype: str
        """
        return self._next_link

    @next_link.setter
    def next_link(self, next_link):
        """Sets the next_link of this RedisListResult.

        Link for next set of locations.

        :param next_link: The next_link of this RedisListResult.
        :type next_link: str
        """

        self._next_link = next_link

    @property
    def value(self):
        """Gets the value of this RedisListResult.

        List of Redis cache instances.

        :return: The value of this RedisListResult.
        :rtype: List[RedisResource]
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this RedisListResult.

        List of Redis cache instances.

        :param value: The value of this RedisListResult.
        :type value: List[RedisResource]
        """

        self._value = value
