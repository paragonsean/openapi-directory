# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.redis_firewall_rule import RedisFirewallRule
from openapi_server import util


class RedisFirewallRuleListResult(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, next_link: str=None, value: List[RedisFirewallRule]=None):
        """RedisFirewallRuleListResult - a model defined in OpenAPI

        :param next_link: The next_link of this RedisFirewallRuleListResult.
        :param value: The value of this RedisFirewallRuleListResult.
        """
        self.openapi_types = {
            'next_link': str,
            'value': List[RedisFirewallRule]
        }

        self.attribute_map = {
            'next_link': 'nextLink',
            'value': 'value'
        }

        self._next_link = next_link
        self._value = value

    @classmethod
    def from_dict(cls, dikt: dict) -> 'RedisFirewallRuleListResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The RedisFirewallRuleListResult of this RedisFirewallRuleListResult.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def next_link(self):
        """Gets the next_link of this RedisFirewallRuleListResult.

        Link for next set of locations.

        :return: The next_link of this RedisFirewallRuleListResult.
        :rtype: str
        """
        return self._next_link

    @next_link.setter
    def next_link(self, next_link):
        """Sets the next_link of this RedisFirewallRuleListResult.

        Link for next set of locations.

        :param next_link: The next_link of this RedisFirewallRuleListResult.
        :type next_link: str
        """

        self._next_link = next_link

    @property
    def value(self):
        """Gets the value of this RedisFirewallRuleListResult.

        Results of the list firewall rules operation.

        :return: The value of this RedisFirewallRuleListResult.
        :rtype: List[RedisFirewallRule]
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this RedisFirewallRuleListResult.

        Results of the list firewall rules operation.

        :param value: The value of this RedisFirewallRuleListResult.
        :type value: List[RedisFirewallRule]
        """

        self._value = value
