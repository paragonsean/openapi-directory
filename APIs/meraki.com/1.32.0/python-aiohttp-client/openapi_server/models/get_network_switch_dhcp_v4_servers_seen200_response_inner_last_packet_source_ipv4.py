# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketSourceIpv4(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, address: str=None):
        """GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketSourceIpv4 - a model defined in OpenAPI

        :param address: The address of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketSourceIpv4.
        """
        self.openapi_types = {
            'address': str
        }

        self.attribute_map = {
            'address': 'address'
        }

        self._address = address

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketSourceIpv4':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The getNetworkSwitchDhcpV4ServersSeen_200_response_inner_lastPacket_source_ipv4 of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketSourceIpv4.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def address(self):
        """Gets the address of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketSourceIpv4.

        Source ipv4 address of the packet.

        :return: The address of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketSourceIpv4.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketSourceIpv4.

        Source ipv4 address of the packet.

        :param address: The address of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketSourceIpv4.
        :type address: str
        """

        self._address = address
