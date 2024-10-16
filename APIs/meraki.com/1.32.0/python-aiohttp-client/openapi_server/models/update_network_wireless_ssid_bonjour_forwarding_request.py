# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.create_network_group_policy_request_bonjour_forwarding_rules_inner import CreateNetworkGroupPolicyRequestBonjourForwardingRulesInner
from openapi_server import util


class UpdateNetworkWirelessSsidBonjourForwardingRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, enabled: bool=None, rules: List[CreateNetworkGroupPolicyRequestBonjourForwardingRulesInner]=None):
        """UpdateNetworkWirelessSsidBonjourForwardingRequest - a model defined in OpenAPI

        :param enabled: The enabled of this UpdateNetworkWirelessSsidBonjourForwardingRequest.
        :param rules: The rules of this UpdateNetworkWirelessSsidBonjourForwardingRequest.
        """
        self.openapi_types = {
            'enabled': bool,
            'rules': List[CreateNetworkGroupPolicyRequestBonjourForwardingRulesInner]
        }

        self.attribute_map = {
            'enabled': 'enabled',
            'rules': 'rules'
        }

        self._enabled = enabled
        self._rules = rules

    @classmethod
    def from_dict(cls, dikt: dict) -> 'UpdateNetworkWirelessSsidBonjourForwardingRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The updateNetworkWirelessSsidBonjourForwarding_request of this UpdateNetworkWirelessSsidBonjourForwardingRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def enabled(self):
        """Gets the enabled of this UpdateNetworkWirelessSsidBonjourForwardingRequest.

        If true, Bonjour forwarding is enabled on this SSID.

        :return: The enabled of this UpdateNetworkWirelessSsidBonjourForwardingRequest.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this UpdateNetworkWirelessSsidBonjourForwardingRequest.

        If true, Bonjour forwarding is enabled on this SSID.

        :param enabled: The enabled of this UpdateNetworkWirelessSsidBonjourForwardingRequest.
        :type enabled: bool
        """

        self._enabled = enabled

    @property
    def rules(self):
        """Gets the rules of this UpdateNetworkWirelessSsidBonjourForwardingRequest.

        List of bonjour forwarding rules.

        :return: The rules of this UpdateNetworkWirelessSsidBonjourForwardingRequest.
        :rtype: List[CreateNetworkGroupPolicyRequestBonjourForwardingRulesInner]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this UpdateNetworkWirelessSsidBonjourForwardingRequest.

        List of bonjour forwarding rules.

        :param rules: The rules of this UpdateNetworkWirelessSsidBonjourForwardingRequest.
        :type rules: List[CreateNetworkGroupPolicyRequestBonjourForwardingRulesInner]
        """

        self._rules = rules
