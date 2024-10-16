# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketEthernet(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, type: str=None):
        """GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketEthernet - a model defined in OpenAPI

        :param type: The type of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketEthernet.
        """
        self.openapi_types = {
            'type': str
        }

        self.attribute_map = {
            'type': 'type'
        }

        self._type = type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketEthernet':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The getNetworkSwitchDhcpV4ServersSeen_200_response_inner_lastPacket_ethernet of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketEthernet.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self):
        """Gets the type of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketEthernet.

        Ethernet type of the packet.

        :return: The type of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketEthernet.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketEthernet.

        Ethernet type of the packet.

        :param type: The type of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketEthernet.
        :type type: str
        """

        self._type = type
