# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.update_network_switch_stack_routing_interface_request_ipv6 import UpdateNetworkSwitchStackRoutingInterfaceRequestIpv6
from openapi_server.models.update_network_switch_stack_routing_interface_request_ospf_settings import UpdateNetworkSwitchStackRoutingInterfaceRequestOspfSettings
from openapi_server import util


class UpdateNetworkSwitchStackRoutingInterfaceRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, default_gateway: str=None, interface_ip: str=None, ipv6: UpdateNetworkSwitchStackRoutingInterfaceRequestIpv6=None, multicast_routing: str=None, name: str=None, ospf_settings: UpdateNetworkSwitchStackRoutingInterfaceRequestOspfSettings=None, subnet: str=None, vlan_id: int=None):
        """UpdateNetworkSwitchStackRoutingInterfaceRequest - a model defined in OpenAPI

        :param default_gateway: The default_gateway of this UpdateNetworkSwitchStackRoutingInterfaceRequest.
        :param interface_ip: The interface_ip of this UpdateNetworkSwitchStackRoutingInterfaceRequest.
        :param ipv6: The ipv6 of this UpdateNetworkSwitchStackRoutingInterfaceRequest.
        :param multicast_routing: The multicast_routing of this UpdateNetworkSwitchStackRoutingInterfaceRequest.
        :param name: The name of this UpdateNetworkSwitchStackRoutingInterfaceRequest.
        :param ospf_settings: The ospf_settings of this UpdateNetworkSwitchStackRoutingInterfaceRequest.
        :param subnet: The subnet of this UpdateNetworkSwitchStackRoutingInterfaceRequest.
        :param vlan_id: The vlan_id of this UpdateNetworkSwitchStackRoutingInterfaceRequest.
        """
        self.openapi_types = {
            'default_gateway': str,
            'interface_ip': str,
            'ipv6': UpdateNetworkSwitchStackRoutingInterfaceRequestIpv6,
            'multicast_routing': str,
            'name': str,
            'ospf_settings': UpdateNetworkSwitchStackRoutingInterfaceRequestOspfSettings,
            'subnet': str,
            'vlan_id': int
        }

        self.attribute_map = {
            'default_gateway': 'defaultGateway',
            'interface_ip': 'interfaceIp',
            'ipv6': 'ipv6',
            'multicast_routing': 'multicastRouting',
            'name': 'name',
            'ospf_settings': 'ospfSettings',
            'subnet': 'subnet',
            'vlan_id': 'vlanId'
        }

        self._default_gateway = default_gateway
        self._interface_ip = interface_ip
        self._ipv6 = ipv6
        self._multicast_routing = multicast_routing
        self._name = name
        self._ospf_settings = ospf_settings
        self._subnet = subnet
        self._vlan_id = vlan_id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'UpdateNetworkSwitchStackRoutingInterfaceRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The updateNetworkSwitchStackRoutingInterface_request of this UpdateNetworkSwitchStackRoutingInterfaceRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def default_gateway(self):
        """Gets the default_gateway of this UpdateNetworkSwitchStackRoutingInterfaceRequest.

        The next hop for any traffic that isn't going to a directly connected subnet or over a static route. This IP address must exist in a subnet with a routed interface.

        :return: The default_gateway of this UpdateNetworkSwitchStackRoutingInterfaceRequest.
        :rtype: str
        """
        return self._default_gateway

    @default_gateway.setter
    def default_gateway(self, default_gateway):
        """Sets the default_gateway of this UpdateNetworkSwitchStackRoutingInterfaceRequest.

        The next hop for any traffic that isn't going to a directly connected subnet or over a static route. This IP address must exist in a subnet with a routed interface.

        :param default_gateway: The default_gateway of this UpdateNetworkSwitchStackRoutingInterfaceRequest.
        :type default_gateway: str
        """

        self._default_gateway = default_gateway

    @property
    def interface_ip(self):
        """Gets the interface_ip of this UpdateNetworkSwitchStackRoutingInterfaceRequest.

        The IP address this switch stack will use for layer 3 routing on this VLAN or subnet. This cannot be the same as the switch's management IP.

        :return: The interface_ip of this UpdateNetworkSwitchStackRoutingInterfaceRequest.
        :rtype: str
        """
        return self._interface_ip

    @interface_ip.setter
    def interface_ip(self, interface_ip):
        """Sets the interface_ip of this UpdateNetworkSwitchStackRoutingInterfaceRequest.

        The IP address this switch stack will use for layer 3 routing on this VLAN or subnet. This cannot be the same as the switch's management IP.

        :param interface_ip: The interface_ip of this UpdateNetworkSwitchStackRoutingInterfaceRequest.
        :type interface_ip: str
        """

        self._interface_ip = interface_ip

    @property
    def ipv6(self):
        """Gets the ipv6 of this UpdateNetworkSwitchStackRoutingInterfaceRequest.


        :return: The ipv6 of this UpdateNetworkSwitchStackRoutingInterfaceRequest.
        :rtype: UpdateNetworkSwitchStackRoutingInterfaceRequestIpv6
        """
        return self._ipv6

    @ipv6.setter
    def ipv6(self, ipv6):
        """Sets the ipv6 of this UpdateNetworkSwitchStackRoutingInterfaceRequest.


        :param ipv6: The ipv6 of this UpdateNetworkSwitchStackRoutingInterfaceRequest.
        :type ipv6: UpdateNetworkSwitchStackRoutingInterfaceRequestIpv6
        """

        self._ipv6 = ipv6

    @property
    def multicast_routing(self):
        """Gets the multicast_routing of this UpdateNetworkSwitchStackRoutingInterfaceRequest.

        Enable multicast support if, multicast routing between VLANs is required. Options are, 'disabled', 'enabled' or 'IGMP snooping querier'.

        :return: The multicast_routing of this UpdateNetworkSwitchStackRoutingInterfaceRequest.
        :rtype: str
        """
        return self._multicast_routing

    @multicast_routing.setter
    def multicast_routing(self, multicast_routing):
        """Sets the multicast_routing of this UpdateNetworkSwitchStackRoutingInterfaceRequest.

        Enable multicast support if, multicast routing between VLANs is required. Options are, 'disabled', 'enabled' or 'IGMP snooping querier'.

        :param multicast_routing: The multicast_routing of this UpdateNetworkSwitchStackRoutingInterfaceRequest.
        :type multicast_routing: str
        """
        allowed_values = ["IGMP snooping querier", "disabled", "enabled"]  # noqa: E501
        if multicast_routing not in allowed_values:
            raise ValueError(
                "Invalid value for `multicast_routing` ({0}), must be one of {1}"
                .format(multicast_routing, allowed_values)
            )

        self._multicast_routing = multicast_routing

    @property
    def name(self):
        """Gets the name of this UpdateNetworkSwitchStackRoutingInterfaceRequest.

        A friendly name or description for the interface or VLAN.

        :return: The name of this UpdateNetworkSwitchStackRoutingInterfaceRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateNetworkSwitchStackRoutingInterfaceRequest.

        A friendly name or description for the interface or VLAN.

        :param name: The name of this UpdateNetworkSwitchStackRoutingInterfaceRequest.
        :type name: str
        """

        self._name = name

    @property
    def ospf_settings(self):
        """Gets the ospf_settings of this UpdateNetworkSwitchStackRoutingInterfaceRequest.


        :return: The ospf_settings of this UpdateNetworkSwitchStackRoutingInterfaceRequest.
        :rtype: UpdateNetworkSwitchStackRoutingInterfaceRequestOspfSettings
        """
        return self._ospf_settings

    @ospf_settings.setter
    def ospf_settings(self, ospf_settings):
        """Sets the ospf_settings of this UpdateNetworkSwitchStackRoutingInterfaceRequest.


        :param ospf_settings: The ospf_settings of this UpdateNetworkSwitchStackRoutingInterfaceRequest.
        :type ospf_settings: UpdateNetworkSwitchStackRoutingInterfaceRequestOspfSettings
        """

        self._ospf_settings = ospf_settings

    @property
    def subnet(self):
        """Gets the subnet of this UpdateNetworkSwitchStackRoutingInterfaceRequest.

        The network that this routed interface is on, in CIDR notation (ex. 10.1.1.0/24).

        :return: The subnet of this UpdateNetworkSwitchStackRoutingInterfaceRequest.
        :rtype: str
        """
        return self._subnet

    @subnet.setter
    def subnet(self, subnet):
        """Sets the subnet of this UpdateNetworkSwitchStackRoutingInterfaceRequest.

        The network that this routed interface is on, in CIDR notation (ex. 10.1.1.0/24).

        :param subnet: The subnet of this UpdateNetworkSwitchStackRoutingInterfaceRequest.
        :type subnet: str
        """

        self._subnet = subnet

    @property
    def vlan_id(self):
        """Gets the vlan_id of this UpdateNetworkSwitchStackRoutingInterfaceRequest.

        The VLAN this routed interface is on. VLAN must be between 1 and 4094.

        :return: The vlan_id of this UpdateNetworkSwitchStackRoutingInterfaceRequest.
        :rtype: int
        """
        return self._vlan_id

    @vlan_id.setter
    def vlan_id(self, vlan_id):
        """Sets the vlan_id of this UpdateNetworkSwitchStackRoutingInterfaceRequest.

        The VLAN this routed interface is on. VLAN must be between 1 and 4094.

        :param vlan_id: The vlan_id of this UpdateNetworkSwitchStackRoutingInterfaceRequest.
        :type vlan_id: int
        """

        self._vlan_id = vlan_id
