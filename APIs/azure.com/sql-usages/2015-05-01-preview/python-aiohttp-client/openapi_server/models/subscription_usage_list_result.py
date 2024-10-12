# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.subscription_usage import SubscriptionUsage
from openapi_server import util


class SubscriptionUsageListResult(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, next_link: str=None, value: List[SubscriptionUsage]=None):
        """SubscriptionUsageListResult - a model defined in OpenAPI

        :param next_link: The next_link of this SubscriptionUsageListResult.
        :param value: The value of this SubscriptionUsageListResult.
        """
        self.openapi_types = {
            'next_link': str,
            'value': List[SubscriptionUsage]
        }

        self.attribute_map = {
            'next_link': 'nextLink',
            'value': 'value'
        }

        self._next_link = next_link
        self._value = value

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SubscriptionUsageListResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The SubscriptionUsageListResult of this SubscriptionUsageListResult.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def next_link(self):
        """Gets the next_link of this SubscriptionUsageListResult.

        Link to retrieve next page of results.

        :return: The next_link of this SubscriptionUsageListResult.
        :rtype: str
        """
        return self._next_link

    @next_link.setter
    def next_link(self, next_link):
        """Sets the next_link of this SubscriptionUsageListResult.

        Link to retrieve next page of results.

        :param next_link: The next_link of this SubscriptionUsageListResult.
        :type next_link: str
        """

        self._next_link = next_link

    @property
    def value(self):
        """Gets the value of this SubscriptionUsageListResult.

        Array of results.

        :return: The value of this SubscriptionUsageListResult.
        :rtype: List[SubscriptionUsage]
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this SubscriptionUsageListResult.

        Array of results.

        :param value: The value of this SubscriptionUsageListResult.
        :type value: List[SubscriptionUsage]
        """

        self._value = value
