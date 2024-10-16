# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.update_network_appliance_firewall_port_forwarding_rules_request_rules_inner import UpdateNetworkApplianceFirewallPortForwardingRulesRequestRulesInner
from openapi_server import util


class UpdateNetworkApplianceFirewallPortForwardingRulesRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, rules: List[UpdateNetworkApplianceFirewallPortForwardingRulesRequestRulesInner]=None):
        """UpdateNetworkApplianceFirewallPortForwardingRulesRequest - a model defined in OpenAPI

        :param rules: The rules of this UpdateNetworkApplianceFirewallPortForwardingRulesRequest.
        """
        self.openapi_types = {
            'rules': List[UpdateNetworkApplianceFirewallPortForwardingRulesRequestRulesInner]
        }

        self.attribute_map = {
            'rules': 'rules'
        }

        self._rules = rules

    @classmethod
    def from_dict(cls, dikt: dict) -> 'UpdateNetworkApplianceFirewallPortForwardingRulesRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The updateNetworkApplianceFirewallPortForwardingRules_request of this UpdateNetworkApplianceFirewallPortForwardingRulesRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def rules(self):
        """Gets the rules of this UpdateNetworkApplianceFirewallPortForwardingRulesRequest.

        An array of port forwarding params

        :return: The rules of this UpdateNetworkApplianceFirewallPortForwardingRulesRequest.
        :rtype: List[UpdateNetworkApplianceFirewallPortForwardingRulesRequestRulesInner]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this UpdateNetworkApplianceFirewallPortForwardingRulesRequest.

        An array of port forwarding params

        :param rules: The rules of this UpdateNetworkApplianceFirewallPortForwardingRulesRequest.
        :type rules: List[UpdateNetworkApplianceFirewallPortForwardingRulesRequestRulesInner]
        """
        if rules is None:
            raise ValueError("Invalid value for `rules`, must not be `None`")

        self._rules = rules
