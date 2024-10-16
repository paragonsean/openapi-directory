# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.create_network_group_policy_request_bandwidth import CreateNetworkGroupPolicyRequestBandwidth
from openapi_server.models.create_network_group_policy_request_bonjour_forwarding import CreateNetworkGroupPolicyRequestBonjourForwarding
from openapi_server.models.create_network_group_policy_request_content_filtering import CreateNetworkGroupPolicyRequestContentFiltering
from openapi_server.models.create_network_group_policy_request_firewall_and_traffic_shaping import CreateNetworkGroupPolicyRequestFirewallAndTrafficShaping
from openapi_server.models.create_network_group_policy_request_scheduling import CreateNetworkGroupPolicyRequestScheduling
from openapi_server.models.create_network_group_policy_request_vlan_tagging import CreateNetworkGroupPolicyRequestVlanTagging
from openapi_server import util


class CreateNetworkGroupPolicyRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, bandwidth: CreateNetworkGroupPolicyRequestBandwidth=None, bonjour_forwarding: CreateNetworkGroupPolicyRequestBonjourForwarding=None, content_filtering: CreateNetworkGroupPolicyRequestContentFiltering=None, firewall_and_traffic_shaping: CreateNetworkGroupPolicyRequestFirewallAndTrafficShaping=None, name: str=None, scheduling: CreateNetworkGroupPolicyRequestScheduling=None, splash_auth_settings: str=None, vlan_tagging: CreateNetworkGroupPolicyRequestVlanTagging=None):
        """CreateNetworkGroupPolicyRequest - a model defined in OpenAPI

        :param bandwidth: The bandwidth of this CreateNetworkGroupPolicyRequest.
        :param bonjour_forwarding: The bonjour_forwarding of this CreateNetworkGroupPolicyRequest.
        :param content_filtering: The content_filtering of this CreateNetworkGroupPolicyRequest.
        :param firewall_and_traffic_shaping: The firewall_and_traffic_shaping of this CreateNetworkGroupPolicyRequest.
        :param name: The name of this CreateNetworkGroupPolicyRequest.
        :param scheduling: The scheduling of this CreateNetworkGroupPolicyRequest.
        :param splash_auth_settings: The splash_auth_settings of this CreateNetworkGroupPolicyRequest.
        :param vlan_tagging: The vlan_tagging of this CreateNetworkGroupPolicyRequest.
        """
        self.openapi_types = {
            'bandwidth': CreateNetworkGroupPolicyRequestBandwidth,
            'bonjour_forwarding': CreateNetworkGroupPolicyRequestBonjourForwarding,
            'content_filtering': CreateNetworkGroupPolicyRequestContentFiltering,
            'firewall_and_traffic_shaping': CreateNetworkGroupPolicyRequestFirewallAndTrafficShaping,
            'name': str,
            'scheduling': CreateNetworkGroupPolicyRequestScheduling,
            'splash_auth_settings': str,
            'vlan_tagging': CreateNetworkGroupPolicyRequestVlanTagging
        }

        self.attribute_map = {
            'bandwidth': 'bandwidth',
            'bonjour_forwarding': 'bonjourForwarding',
            'content_filtering': 'contentFiltering',
            'firewall_and_traffic_shaping': 'firewallAndTrafficShaping',
            'name': 'name',
            'scheduling': 'scheduling',
            'splash_auth_settings': 'splashAuthSettings',
            'vlan_tagging': 'vlanTagging'
        }

        self._bandwidth = bandwidth
        self._bonjour_forwarding = bonjour_forwarding
        self._content_filtering = content_filtering
        self._firewall_and_traffic_shaping = firewall_and_traffic_shaping
        self._name = name
        self._scheduling = scheduling
        self._splash_auth_settings = splash_auth_settings
        self._vlan_tagging = vlan_tagging

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CreateNetworkGroupPolicyRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The createNetworkGroupPolicy_request of this CreateNetworkGroupPolicyRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def bandwidth(self):
        """Gets the bandwidth of this CreateNetworkGroupPolicyRequest.


        :return: The bandwidth of this CreateNetworkGroupPolicyRequest.
        :rtype: CreateNetworkGroupPolicyRequestBandwidth
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        """Sets the bandwidth of this CreateNetworkGroupPolicyRequest.


        :param bandwidth: The bandwidth of this CreateNetworkGroupPolicyRequest.
        :type bandwidth: CreateNetworkGroupPolicyRequestBandwidth
        """

        self._bandwidth = bandwidth

    @property
    def bonjour_forwarding(self):
        """Gets the bonjour_forwarding of this CreateNetworkGroupPolicyRequest.


        :return: The bonjour_forwarding of this CreateNetworkGroupPolicyRequest.
        :rtype: CreateNetworkGroupPolicyRequestBonjourForwarding
        """
        return self._bonjour_forwarding

    @bonjour_forwarding.setter
    def bonjour_forwarding(self, bonjour_forwarding):
        """Sets the bonjour_forwarding of this CreateNetworkGroupPolicyRequest.


        :param bonjour_forwarding: The bonjour_forwarding of this CreateNetworkGroupPolicyRequest.
        :type bonjour_forwarding: CreateNetworkGroupPolicyRequestBonjourForwarding
        """

        self._bonjour_forwarding = bonjour_forwarding

    @property
    def content_filtering(self):
        """Gets the content_filtering of this CreateNetworkGroupPolicyRequest.


        :return: The content_filtering of this CreateNetworkGroupPolicyRequest.
        :rtype: CreateNetworkGroupPolicyRequestContentFiltering
        """
        return self._content_filtering

    @content_filtering.setter
    def content_filtering(self, content_filtering):
        """Sets the content_filtering of this CreateNetworkGroupPolicyRequest.


        :param content_filtering: The content_filtering of this CreateNetworkGroupPolicyRequest.
        :type content_filtering: CreateNetworkGroupPolicyRequestContentFiltering
        """

        self._content_filtering = content_filtering

    @property
    def firewall_and_traffic_shaping(self):
        """Gets the firewall_and_traffic_shaping of this CreateNetworkGroupPolicyRequest.


        :return: The firewall_and_traffic_shaping of this CreateNetworkGroupPolicyRequest.
        :rtype: CreateNetworkGroupPolicyRequestFirewallAndTrafficShaping
        """
        return self._firewall_and_traffic_shaping

    @firewall_and_traffic_shaping.setter
    def firewall_and_traffic_shaping(self, firewall_and_traffic_shaping):
        """Sets the firewall_and_traffic_shaping of this CreateNetworkGroupPolicyRequest.


        :param firewall_and_traffic_shaping: The firewall_and_traffic_shaping of this CreateNetworkGroupPolicyRequest.
        :type firewall_and_traffic_shaping: CreateNetworkGroupPolicyRequestFirewallAndTrafficShaping
        """

        self._firewall_and_traffic_shaping = firewall_and_traffic_shaping

    @property
    def name(self):
        """Gets the name of this CreateNetworkGroupPolicyRequest.

        The name for your group policy. Required.

        :return: The name of this CreateNetworkGroupPolicyRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateNetworkGroupPolicyRequest.

        The name for your group policy. Required.

        :param name: The name of this CreateNetworkGroupPolicyRequest.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def scheduling(self):
        """Gets the scheduling of this CreateNetworkGroupPolicyRequest.


        :return: The scheduling of this CreateNetworkGroupPolicyRequest.
        :rtype: CreateNetworkGroupPolicyRequestScheduling
        """
        return self._scheduling

    @scheduling.setter
    def scheduling(self, scheduling):
        """Sets the scheduling of this CreateNetworkGroupPolicyRequest.


        :param scheduling: The scheduling of this CreateNetworkGroupPolicyRequest.
        :type scheduling: CreateNetworkGroupPolicyRequestScheduling
        """

        self._scheduling = scheduling

    @property
    def splash_auth_settings(self):
        """Gets the splash_auth_settings of this CreateNetworkGroupPolicyRequest.

        Whether clients bound to your policy will bypass splash authorization or behave according to the network's rules. Can be one of 'network default' or 'bypass'. Only available if your network has a wireless configuration.

        :return: The splash_auth_settings of this CreateNetworkGroupPolicyRequest.
        :rtype: str
        """
        return self._splash_auth_settings

    @splash_auth_settings.setter
    def splash_auth_settings(self, splash_auth_settings):
        """Sets the splash_auth_settings of this CreateNetworkGroupPolicyRequest.

        Whether clients bound to your policy will bypass splash authorization or behave according to the network's rules. Can be one of 'network default' or 'bypass'. Only available if your network has a wireless configuration.

        :param splash_auth_settings: The splash_auth_settings of this CreateNetworkGroupPolicyRequest.
        :type splash_auth_settings: str
        """
        allowed_values = ["bypass", "network default"]  # noqa: E501
        if splash_auth_settings not in allowed_values:
            raise ValueError(
                "Invalid value for `splash_auth_settings` ({0}), must be one of {1}"
                .format(splash_auth_settings, allowed_values)
            )

        self._splash_auth_settings = splash_auth_settings

    @property
    def vlan_tagging(self):
        """Gets the vlan_tagging of this CreateNetworkGroupPolicyRequest.


        :return: The vlan_tagging of this CreateNetworkGroupPolicyRequest.
        :rtype: CreateNetworkGroupPolicyRequestVlanTagging
        """
        return self._vlan_tagging

    @vlan_tagging.setter
    def vlan_tagging(self, vlan_tagging):
        """Sets the vlan_tagging of this CreateNetworkGroupPolicyRequest.


        :param vlan_tagging: The vlan_tagging of this CreateNetworkGroupPolicyRequest.
        :type vlan_tagging: CreateNetworkGroupPolicyRequestVlanTagging
        """

        self._vlan_tagging = vlan_tagging
