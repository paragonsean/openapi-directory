# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class UpdateNetworkApplianceFirewallL7FirewallRulesRequestRulesInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, policy: str=None, type: str=None, value: str=None):
        """UpdateNetworkApplianceFirewallL7FirewallRulesRequestRulesInner - a model defined in OpenAPI

        :param policy: The policy of this UpdateNetworkApplianceFirewallL7FirewallRulesRequestRulesInner.
        :param type: The type of this UpdateNetworkApplianceFirewallL7FirewallRulesRequestRulesInner.
        :param value: The value of this UpdateNetworkApplianceFirewallL7FirewallRulesRequestRulesInner.
        """
        self.openapi_types = {
            'policy': str,
            'type': str,
            'value': str
        }

        self.attribute_map = {
            'policy': 'policy',
            'type': 'type',
            'value': 'value'
        }

        self._policy = policy
        self._type = type
        self._value = value

    @classmethod
    def from_dict(cls, dikt: dict) -> 'UpdateNetworkApplianceFirewallL7FirewallRulesRequestRulesInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The updateNetworkApplianceFirewallL7FirewallRules_request_rules_inner of this UpdateNetworkApplianceFirewallL7FirewallRulesRequestRulesInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def policy(self):
        """Gets the policy of this UpdateNetworkApplianceFirewallL7FirewallRulesRequestRulesInner.

        'Deny' traffic specified by this rule

        :return: The policy of this UpdateNetworkApplianceFirewallL7FirewallRulesRequestRulesInner.
        :rtype: str
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this UpdateNetworkApplianceFirewallL7FirewallRulesRequestRulesInner.

        'Deny' traffic specified by this rule

        :param policy: The policy of this UpdateNetworkApplianceFirewallL7FirewallRulesRequestRulesInner.
        :type policy: str
        """
        allowed_values = ["deny"]  # noqa: E501
        if policy not in allowed_values:
            raise ValueError(
                "Invalid value for `policy` ({0}), must be one of {1}"
                .format(policy, allowed_values)
            )

        self._policy = policy

    @property
    def type(self):
        """Gets the type of this UpdateNetworkApplianceFirewallL7FirewallRulesRequestRulesInner.

        Type of the L7 rule. One of: 'application', 'applicationCategory', 'host', 'port', 'ipRange'

        :return: The type of this UpdateNetworkApplianceFirewallL7FirewallRulesRequestRulesInner.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UpdateNetworkApplianceFirewallL7FirewallRulesRequestRulesInner.

        Type of the L7 rule. One of: 'application', 'applicationCategory', 'host', 'port', 'ipRange'

        :param type: The type of this UpdateNetworkApplianceFirewallL7FirewallRulesRequestRulesInner.
        :type type: str
        """
        allowed_values = ["application", "applicationCategory", "host", "ipRange", "port"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def value(self):
        """Gets the value of this UpdateNetworkApplianceFirewallL7FirewallRulesRequestRulesInner.

        The 'value' of what you want to block. Format of 'value' varies depending on type of the rule. The application categories and application ids can be retrieved from the the 'MX L7 application categories' endpoint. The countries follow the two-letter ISO 3166-1 alpha-2 format.

        :return: The value of this UpdateNetworkApplianceFirewallL7FirewallRulesRequestRulesInner.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this UpdateNetworkApplianceFirewallL7FirewallRulesRequestRulesInner.

        The 'value' of what you want to block. Format of 'value' varies depending on type of the rule. The application categories and application ids can be retrieved from the the 'MX L7 application categories' endpoint. The countries follow the two-letter ISO 3166-1 alpha-2 format.

        :param value: The value of this UpdateNetworkApplianceFirewallL7FirewallRulesRequestRulesInner.
        :type value: str
        """

        self._value = value
