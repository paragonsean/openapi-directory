# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, access_policy_type: str=None, allowed_vlans: str=None, enabled: bool=None, link_negotiation: str=None, name: str=None, poe_enabled: bool=None, port_id: str=None, rstp_enabled: bool=None, sticky_mac_allow_list: List[str]=None, sticky_mac_allow_list_limit: int=None, stp_guard: str=None, tags: List[str]=None, type: str=None, vlan: int=None, voice_vlan: int=None):
        """GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner - a model defined in OpenAPI

        :param access_policy_type: The access_policy_type of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.
        :param allowed_vlans: The allowed_vlans of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.
        :param enabled: The enabled of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.
        :param link_negotiation: The link_negotiation of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.
        :param name: The name of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.
        :param poe_enabled: The poe_enabled of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.
        :param port_id: The port_id of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.
        :param rstp_enabled: The rstp_enabled of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.
        :param sticky_mac_allow_list: The sticky_mac_allow_list of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.
        :param sticky_mac_allow_list_limit: The sticky_mac_allow_list_limit of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.
        :param stp_guard: The stp_guard of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.
        :param tags: The tags of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.
        :param type: The type of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.
        :param vlan: The vlan of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.
        :param voice_vlan: The voice_vlan of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.
        """
        self.openapi_types = {
            'access_policy_type': str,
            'allowed_vlans': str,
            'enabled': bool,
            'link_negotiation': str,
            'name': str,
            'poe_enabled': bool,
            'port_id': str,
            'rstp_enabled': bool,
            'sticky_mac_allow_list': List[str],
            'sticky_mac_allow_list_limit': int,
            'stp_guard': str,
            'tags': List[str],
            'type': str,
            'vlan': int,
            'voice_vlan': int
        }

        self.attribute_map = {
            'access_policy_type': 'accessPolicyType',
            'allowed_vlans': 'allowedVlans',
            'enabled': 'enabled',
            'link_negotiation': 'linkNegotiation',
            'name': 'name',
            'poe_enabled': 'poeEnabled',
            'port_id': 'portId',
            'rstp_enabled': 'rstpEnabled',
            'sticky_mac_allow_list': 'stickyMacAllowList',
            'sticky_mac_allow_list_limit': 'stickyMacAllowListLimit',
            'stp_guard': 'stpGuard',
            'tags': 'tags',
            'type': 'type',
            'vlan': 'vlan',
            'voice_vlan': 'voiceVlan'
        }

        self._access_policy_type = access_policy_type
        self._allowed_vlans = allowed_vlans
        self._enabled = enabled
        self._link_negotiation = link_negotiation
        self._name = name
        self._poe_enabled = poe_enabled
        self._port_id = port_id
        self._rstp_enabled = rstp_enabled
        self._sticky_mac_allow_list = sticky_mac_allow_list
        self._sticky_mac_allow_list_limit = sticky_mac_allow_list_limit
        self._stp_guard = stp_guard
        self._tags = tags
        self._type = type
        self._vlan = vlan
        self._voice_vlan = voice_vlan

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The getOrganizationSwitchPortsBySwitch_200_response_inner_ports_inner of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def access_policy_type(self):
        """Gets the access_policy_type of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.

        The type of the access policy of the switch port. Only applicable to access ports. Can be one of 'Open', 'Custom access policy', 'MAC allow list' or 'Sticky MAC allow list'.

        :return: The access_policy_type of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.
        :rtype: str
        """
        return self._access_policy_type

    @access_policy_type.setter
    def access_policy_type(self, access_policy_type):
        """Sets the access_policy_type of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.

        The type of the access policy of the switch port. Only applicable to access ports. Can be one of 'Open', 'Custom access policy', 'MAC allow list' or 'Sticky MAC allow list'.

        :param access_policy_type: The access_policy_type of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.
        :type access_policy_type: str
        """
        allowed_values = ["Custom access policy", "MAC allow list", "Open", "Sticky MAC allow list"]  # noqa: E501
        if access_policy_type not in allowed_values:
            raise ValueError(
                "Invalid value for `access_policy_type` ({0}), must be one of {1}"
                .format(access_policy_type, allowed_values)
            )

        self._access_policy_type = access_policy_type

    @property
    def allowed_vlans(self):
        """Gets the allowed_vlans of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.

        The VLANs allowed on the switch port. Only applicable to trunk ports.

        :return: The allowed_vlans of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.
        :rtype: str
        """
        return self._allowed_vlans

    @allowed_vlans.setter
    def allowed_vlans(self, allowed_vlans):
        """Sets the allowed_vlans of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.

        The VLANs allowed on the switch port. Only applicable to trunk ports.

        :param allowed_vlans: The allowed_vlans of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.
        :type allowed_vlans: str
        """

        self._allowed_vlans = allowed_vlans

    @property
    def enabled(self):
        """Gets the enabled of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.

        The status of the switch port.

        :return: The enabled of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.

        The status of the switch port.

        :param enabled: The enabled of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.
        :type enabled: bool
        """

        self._enabled = enabled

    @property
    def link_negotiation(self):
        """Gets the link_negotiation of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.

        The link speed for the switch port.

        :return: The link_negotiation of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.
        :rtype: str
        """
        return self._link_negotiation

    @link_negotiation.setter
    def link_negotiation(self, link_negotiation):
        """Sets the link_negotiation of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.

        The link speed for the switch port.

        :param link_negotiation: The link_negotiation of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.
        :type link_negotiation: str
        """

        self._link_negotiation = link_negotiation

    @property
    def name(self):
        """Gets the name of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.

        The name of the switch port.

        :return: The name of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.

        The name of the switch port.

        :param name: The name of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.
        :type name: str
        """

        self._name = name

    @property
    def poe_enabled(self):
        """Gets the poe_enabled of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.

        The PoE status of the switch port.

        :return: The poe_enabled of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.
        :rtype: bool
        """
        return self._poe_enabled

    @poe_enabled.setter
    def poe_enabled(self, poe_enabled):
        """Sets the poe_enabled of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.

        The PoE status of the switch port.

        :param poe_enabled: The poe_enabled of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.
        :type poe_enabled: bool
        """

        self._poe_enabled = poe_enabled

    @property
    def port_id(self):
        """Gets the port_id of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.

        The identifier of the switch port.

        :return: The port_id of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.
        :rtype: str
        """
        return self._port_id

    @port_id.setter
    def port_id(self, port_id):
        """Sets the port_id of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.

        The identifier of the switch port.

        :param port_id: The port_id of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.
        :type port_id: str
        """

        self._port_id = port_id

    @property
    def rstp_enabled(self):
        """Gets the rstp_enabled of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.

        The rapid spanning tree protocol status.

        :return: The rstp_enabled of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.
        :rtype: bool
        """
        return self._rstp_enabled

    @rstp_enabled.setter
    def rstp_enabled(self, rstp_enabled):
        """Sets the rstp_enabled of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.

        The rapid spanning tree protocol status.

        :param rstp_enabled: The rstp_enabled of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.
        :type rstp_enabled: bool
        """

        self._rstp_enabled = rstp_enabled

    @property
    def sticky_mac_allow_list(self):
        """Gets the sticky_mac_allow_list of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.

        The initial list of MAC addresses for sticky Mac allow list. Only applicable when 'accessPolicyType' is 'Sticky MAC allow list'.

        :return: The sticky_mac_allow_list of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.
        :rtype: List[str]
        """
        return self._sticky_mac_allow_list

    @sticky_mac_allow_list.setter
    def sticky_mac_allow_list(self, sticky_mac_allow_list):
        """Sets the sticky_mac_allow_list of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.

        The initial list of MAC addresses for sticky Mac allow list. Only applicable when 'accessPolicyType' is 'Sticky MAC allow list'.

        :param sticky_mac_allow_list: The sticky_mac_allow_list of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.
        :type sticky_mac_allow_list: List[str]
        """

        self._sticky_mac_allow_list = sticky_mac_allow_list

    @property
    def sticky_mac_allow_list_limit(self):
        """Gets the sticky_mac_allow_list_limit of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.

        The maximum number of MAC addresses for sticky MAC allow list. Only applicable when 'accessPolicyType' is 'Sticky MAC allow list'.

        :return: The sticky_mac_allow_list_limit of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.
        :rtype: int
        """
        return self._sticky_mac_allow_list_limit

    @sticky_mac_allow_list_limit.setter
    def sticky_mac_allow_list_limit(self, sticky_mac_allow_list_limit):
        """Sets the sticky_mac_allow_list_limit of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.

        The maximum number of MAC addresses for sticky MAC allow list. Only applicable when 'accessPolicyType' is 'Sticky MAC allow list'.

        :param sticky_mac_allow_list_limit: The sticky_mac_allow_list_limit of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.
        :type sticky_mac_allow_list_limit: int
        """

        self._sticky_mac_allow_list_limit = sticky_mac_allow_list_limit

    @property
    def stp_guard(self):
        """Gets the stp_guard of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.

        The state of the STP guard ('disabled', 'root guard', 'bpdu guard' or 'loop guard').

        :return: The stp_guard of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.
        :rtype: str
        """
        return self._stp_guard

    @stp_guard.setter
    def stp_guard(self, stp_guard):
        """Sets the stp_guard of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.

        The state of the STP guard ('disabled', 'root guard', 'bpdu guard' or 'loop guard').

        :param stp_guard: The stp_guard of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.
        :type stp_guard: str
        """
        allowed_values = ["bpdu guard", "disabled", "loop guard", "root guard"]  # noqa: E501
        if stp_guard not in allowed_values:
            raise ValueError(
                "Invalid value for `stp_guard` ({0}), must be one of {1}"
                .format(stp_guard, allowed_values)
            )

        self._stp_guard = stp_guard

    @property
    def tags(self):
        """Gets the tags of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.

        The list of tags of the switch port.

        :return: The tags of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.
        :rtype: List[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.

        The list of tags of the switch port.

        :param tags: The tags of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.
        :type tags: List[str]
        """

        self._tags = tags

    @property
    def type(self):
        """Gets the type of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.

        The type of the switch port ('trunk' or 'access').

        :return: The type of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.

        The type of the switch port ('trunk' or 'access').

        :param type: The type of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.
        :type type: str
        """
        allowed_values = ["access", "trunk"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def vlan(self):
        """Gets the vlan of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.

        The VLAN of the switch port. A null value will clear the value set for trunk ports.

        :return: The vlan of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.
        :rtype: int
        """
        return self._vlan

    @vlan.setter
    def vlan(self, vlan):
        """Sets the vlan of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.

        The VLAN of the switch port. A null value will clear the value set for trunk ports.

        :param vlan: The vlan of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.
        :type vlan: int
        """

        self._vlan = vlan

    @property
    def voice_vlan(self):
        """Gets the voice_vlan of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.

        The voice VLAN of the switch port. Only applicable to access ports.

        :return: The voice_vlan of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.
        :rtype: int
        """
        return self._voice_vlan

    @voice_vlan.setter
    def voice_vlan(self, voice_vlan):
        """Sets the voice_vlan of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.

        The voice VLAN of the switch port. Only applicable to access ports.

        :param voice_vlan: The voice_vlan of this GetOrganizationSwitchPortsBySwitch200ResponseInnerPortsInner.
        :type voice_vlan: int
        """

        self._voice_vlan = voice_vlan
