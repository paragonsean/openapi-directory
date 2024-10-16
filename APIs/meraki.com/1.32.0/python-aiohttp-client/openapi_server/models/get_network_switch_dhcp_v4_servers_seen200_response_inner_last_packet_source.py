# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.get_network_switch_dhcp_v4_servers_seen200_response_inner_last_packet_source_ipv4 import GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketSourceIpv4
from openapi_server import util


class GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketSource(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, ipv4: GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketSourceIpv4=None, mac: str=None, port: int=None):
        """GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketSource - a model defined in OpenAPI

        :param ipv4: The ipv4 of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketSource.
        :param mac: The mac of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketSource.
        :param port: The port of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketSource.
        """
        self.openapi_types = {
            'ipv4': GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketSourceIpv4,
            'mac': str,
            'port': int
        }

        self.attribute_map = {
            'ipv4': 'ipv4',
            'mac': 'mac',
            'port': 'port'
        }

        self._ipv4 = ipv4
        self._mac = mac
        self._port = port

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketSource':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The getNetworkSwitchDhcpV4ServersSeen_200_response_inner_lastPacket_source of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketSource.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ipv4(self):
        """Gets the ipv4 of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketSource.


        :return: The ipv4 of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketSource.
        :rtype: GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketSourceIpv4
        """
        return self._ipv4

    @ipv4.setter
    def ipv4(self, ipv4):
        """Sets the ipv4 of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketSource.


        :param ipv4: The ipv4 of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketSource.
        :type ipv4: GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketSourceIpv4
        """

        self._ipv4 = ipv4

    @property
    def mac(self):
        """Gets the mac of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketSource.

        Source mac address of the packet.

        :return: The mac of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketSource.
        :rtype: str
        """
        return self._mac

    @mac.setter
    def mac(self, mac):
        """Sets the mac of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketSource.

        Source mac address of the packet.

        :param mac: The mac of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketSource.
        :type mac: str
        """

        self._mac = mac

    @property
    def port(self):
        """Gets the port of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketSource.

        Source port of the packet.

        :return: The port of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketSource.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketSource.

        Source port of the packet.

        :param port: The port of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketSource.
        :type port: int
        """

        self._port = port
