# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class CreateNetworkSwitchStackRoutingInterfaceRequestIpv6(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, address: str=None, assignment_mode: str=None, gateway: str=None, prefix: str=None):
        """CreateNetworkSwitchStackRoutingInterfaceRequestIpv6 - a model defined in OpenAPI

        :param address: The address of this CreateNetworkSwitchStackRoutingInterfaceRequestIpv6.
        :param assignment_mode: The assignment_mode of this CreateNetworkSwitchStackRoutingInterfaceRequestIpv6.
        :param gateway: The gateway of this CreateNetworkSwitchStackRoutingInterfaceRequestIpv6.
        :param prefix: The prefix of this CreateNetworkSwitchStackRoutingInterfaceRequestIpv6.
        """
        self.openapi_types = {
            'address': str,
            'assignment_mode': str,
            'gateway': str,
            'prefix': str
        }

        self.attribute_map = {
            'address': 'address',
            'assignment_mode': 'assignmentMode',
            'gateway': 'gateway',
            'prefix': 'prefix'
        }

        self._address = address
        self._assignment_mode = assignment_mode
        self._gateway = gateway
        self._prefix = prefix

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CreateNetworkSwitchStackRoutingInterfaceRequestIpv6':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The createNetworkSwitchStackRoutingInterface_request_ipv6 of this CreateNetworkSwitchStackRoutingInterfaceRequestIpv6.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def address(self):
        """Gets the address of this CreateNetworkSwitchStackRoutingInterfaceRequestIpv6.

        The IPv6 address of the interface. Required if assignmentMode is 'static'. Must not be included if assignmentMode is 'eui-64'.

        :return: The address of this CreateNetworkSwitchStackRoutingInterfaceRequestIpv6.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this CreateNetworkSwitchStackRoutingInterfaceRequestIpv6.

        The IPv6 address of the interface. Required if assignmentMode is 'static'. Must not be included if assignmentMode is 'eui-64'.

        :param address: The address of this CreateNetworkSwitchStackRoutingInterfaceRequestIpv6.
        :type address: str
        """

        self._address = address

    @property
    def assignment_mode(self):
        """Gets the assignment_mode of this CreateNetworkSwitchStackRoutingInterfaceRequestIpv6.

        The IPv6 assignment mode for the interface. Can be either 'eui-64' or 'static'.

        :return: The assignment_mode of this CreateNetworkSwitchStackRoutingInterfaceRequestIpv6.
        :rtype: str
        """
        return self._assignment_mode

    @assignment_mode.setter
    def assignment_mode(self, assignment_mode):
        """Sets the assignment_mode of this CreateNetworkSwitchStackRoutingInterfaceRequestIpv6.

        The IPv6 assignment mode for the interface. Can be either 'eui-64' or 'static'.

        :param assignment_mode: The assignment_mode of this CreateNetworkSwitchStackRoutingInterfaceRequestIpv6.
        :type assignment_mode: str
        """

        self._assignment_mode = assignment_mode

    @property
    def gateway(self):
        """Gets the gateway of this CreateNetworkSwitchStackRoutingInterfaceRequestIpv6.

        The IPv6 default gateway of the interface. Required if prefix is defined and this is the first interface with IPv6 configured for the stack.

        :return: The gateway of this CreateNetworkSwitchStackRoutingInterfaceRequestIpv6.
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """Sets the gateway of this CreateNetworkSwitchStackRoutingInterfaceRequestIpv6.

        The IPv6 default gateway of the interface. Required if prefix is defined and this is the first interface with IPv6 configured for the stack.

        :param gateway: The gateway of this CreateNetworkSwitchStackRoutingInterfaceRequestIpv6.
        :type gateway: str
        """

        self._gateway = gateway

    @property
    def prefix(self):
        """Gets the prefix of this CreateNetworkSwitchStackRoutingInterfaceRequestIpv6.

        The IPv6 prefix of the interface. Required if IPv6 object is included.

        :return: The prefix of this CreateNetworkSwitchStackRoutingInterfaceRequestIpv6.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """Sets the prefix of this CreateNetworkSwitchStackRoutingInterfaceRequestIpv6.

        The IPv6 prefix of the interface. Required if IPv6 object is included.

        :param prefix: The prefix of this CreateNetworkSwitchStackRoutingInterfaceRequestIpv6.
        :type prefix: str
        """

        self._prefix = prefix
