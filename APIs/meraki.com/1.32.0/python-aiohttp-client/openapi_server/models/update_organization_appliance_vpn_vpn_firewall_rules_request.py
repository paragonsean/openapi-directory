# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.update_organization_appliance_vpn_vpn_firewall_rules_request_rules_inner import UpdateOrganizationApplianceVpnVpnFirewallRulesRequestRulesInner
from openapi_server import util


class UpdateOrganizationApplianceVpnVpnFirewallRulesRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, rules: List[UpdateOrganizationApplianceVpnVpnFirewallRulesRequestRulesInner]=None, syslog_default_rule: bool=None):
        """UpdateOrganizationApplianceVpnVpnFirewallRulesRequest - a model defined in OpenAPI

        :param rules: The rules of this UpdateOrganizationApplianceVpnVpnFirewallRulesRequest.
        :param syslog_default_rule: The syslog_default_rule of this UpdateOrganizationApplianceVpnVpnFirewallRulesRequest.
        """
        self.openapi_types = {
            'rules': List[UpdateOrganizationApplianceVpnVpnFirewallRulesRequestRulesInner],
            'syslog_default_rule': bool
        }

        self.attribute_map = {
            'rules': 'rules',
            'syslog_default_rule': 'syslogDefaultRule'
        }

        self._rules = rules
        self._syslog_default_rule = syslog_default_rule

    @classmethod
    def from_dict(cls, dikt: dict) -> 'UpdateOrganizationApplianceVpnVpnFirewallRulesRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The updateOrganizationApplianceVpnVpnFirewallRules_request of this UpdateOrganizationApplianceVpnVpnFirewallRulesRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def rules(self):
        """Gets the rules of this UpdateOrganizationApplianceVpnVpnFirewallRulesRequest.

        An ordered array of the firewall rules (not including the default rule)

        :return: The rules of this UpdateOrganizationApplianceVpnVpnFirewallRulesRequest.
        :rtype: List[UpdateOrganizationApplianceVpnVpnFirewallRulesRequestRulesInner]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this UpdateOrganizationApplianceVpnVpnFirewallRulesRequest.

        An ordered array of the firewall rules (not including the default rule)

        :param rules: The rules of this UpdateOrganizationApplianceVpnVpnFirewallRulesRequest.
        :type rules: List[UpdateOrganizationApplianceVpnVpnFirewallRulesRequestRulesInner]
        """

        self._rules = rules

    @property
    def syslog_default_rule(self):
        """Gets the syslog_default_rule of this UpdateOrganizationApplianceVpnVpnFirewallRulesRequest.

        Log the special default rule (boolean value - enable only if you've configured a syslog server) (optional)

        :return: The syslog_default_rule of this UpdateOrganizationApplianceVpnVpnFirewallRulesRequest.
        :rtype: bool
        """
        return self._syslog_default_rule

    @syslog_default_rule.setter
    def syslog_default_rule(self, syslog_default_rule):
        """Sets the syslog_default_rule of this UpdateOrganizationApplianceVpnVpnFirewallRulesRequest.

        Log the special default rule (boolean value - enable only if you've configured a syslog server) (optional)

        :param syslog_default_rule: The syslog_default_rule of this UpdateOrganizationApplianceVpnVpnFirewallRulesRequest.
        :type syslog_default_rule: bool
        """

        self._syslog_default_rule = syslog_default_rule
