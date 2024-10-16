# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.get_network_switch_dhcp_v4_servers_seen200_response_inner_last_packet_destination import GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketDestination
from openapi_server.models.get_network_switch_dhcp_v4_servers_seen200_response_inner_last_packet_ethernet import GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketEthernet
from openapi_server.models.get_network_switch_dhcp_v4_servers_seen200_response_inner_last_packet_fields import GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketFields
from openapi_server.models.get_network_switch_dhcp_v4_servers_seen200_response_inner_last_packet_ip import GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketIp
from openapi_server.models.get_network_switch_dhcp_v4_servers_seen200_response_inner_last_packet_source import GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketSource
from openapi_server.models.get_network_switch_dhcp_v4_servers_seen200_response_inner_last_packet_udp import GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketUdp
from openapi_server import util


class GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacket(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, destination: GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketDestination=None, ethernet: GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketEthernet=None, fields: GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketFields=None, ip: GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketIp=None, source: GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketSource=None, type: str=None, udp: GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketUdp=None):
        """GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacket - a model defined in OpenAPI

        :param destination: The destination of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacket.
        :param ethernet: The ethernet of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacket.
        :param fields: The fields of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacket.
        :param ip: The ip of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacket.
        :param source: The source of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacket.
        :param type: The type of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacket.
        :param udp: The udp of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacket.
        """
        self.openapi_types = {
            'destination': GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketDestination,
            'ethernet': GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketEthernet,
            'fields': GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketFields,
            'ip': GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketIp,
            'source': GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketSource,
            'type': str,
            'udp': GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketUdp
        }

        self.attribute_map = {
            'destination': 'destination',
            'ethernet': 'ethernet',
            'fields': 'fields',
            'ip': 'ip',
            'source': 'source',
            'type': 'type',
            'udp': 'udp'
        }

        self._destination = destination
        self._ethernet = ethernet
        self._fields = fields
        self._ip = ip
        self._source = source
        self._type = type
        self._udp = udp

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacket':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The getNetworkSwitchDhcpV4ServersSeen_200_response_inner_lastPacket of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacket.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def destination(self):
        """Gets the destination of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacket.


        :return: The destination of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacket.
        :rtype: GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketDestination
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacket.


        :param destination: The destination of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacket.
        :type destination: GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketDestination
        """

        self._destination = destination

    @property
    def ethernet(self):
        """Gets the ethernet of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacket.


        :return: The ethernet of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacket.
        :rtype: GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketEthernet
        """
        return self._ethernet

    @ethernet.setter
    def ethernet(self, ethernet):
        """Sets the ethernet of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacket.


        :param ethernet: The ethernet of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacket.
        :type ethernet: GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketEthernet
        """

        self._ethernet = ethernet

    @property
    def fields(self):
        """Gets the fields of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacket.


        :return: The fields of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacket.
        :rtype: GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketFields
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacket.


        :param fields: The fields of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacket.
        :type fields: GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketFields
        """

        self._fields = fields

    @property
    def ip(self):
        """Gets the ip of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacket.


        :return: The ip of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacket.
        :rtype: GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketIp
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacket.


        :param ip: The ip of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacket.
        :type ip: GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketIp
        """

        self._ip = ip

    @property
    def source(self):
        """Gets the source of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacket.


        :return: The source of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacket.
        :rtype: GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketSource
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacket.


        :param source: The source of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacket.
        :type source: GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketSource
        """

        self._source = source

    @property
    def type(self):
        """Gets the type of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacket.

        Packet type.

        :return: The type of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacket.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacket.

        Packet type.

        :param type: The type of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacket.
        :type type: str
        """

        self._type = type

    @property
    def udp(self):
        """Gets the udp of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacket.


        :return: The udp of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacket.
        :rtype: GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketUdp
        """
        return self._udp

    @udp.setter
    def udp(self, udp):
        """Sets the udp of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacket.


        :param udp: The udp of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacket.
        :type udp: GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketUdp
        """

        self._udp = udp
