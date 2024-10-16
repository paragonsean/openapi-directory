# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.get_network_switch_dhcp_v4_servers_seen200_response_inner_last_ack_ipv4 import GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastAckIpv4
from openapi_server import util


class GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastAck(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, ipv4: GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastAckIpv4=None, ts: datetime=None):
        """GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastAck - a model defined in OpenAPI

        :param ipv4: The ipv4 of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastAck.
        :param ts: The ts of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastAck.
        """
        self.openapi_types = {
            'ipv4': GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastAckIpv4,
            'ts': datetime
        }

        self.attribute_map = {
            'ipv4': 'ipv4',
            'ts': 'ts'
        }

        self._ipv4 = ipv4
        self._ts = ts

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastAck':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The getNetworkSwitchDhcpV4ServersSeen_200_response_inner_lastAck of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastAck.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ipv4(self):
        """Gets the ipv4 of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastAck.


        :return: The ipv4 of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastAck.
        :rtype: GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastAckIpv4
        """
        return self._ipv4

    @ipv4.setter
    def ipv4(self, ipv4):
        """Sets the ipv4 of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastAck.


        :param ipv4: The ipv4 of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastAck.
        :type ipv4: GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastAckIpv4
        """

        self._ipv4 = ipv4

    @property
    def ts(self):
        """Gets the ts of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastAck.

        Last time the server was acked.

        :return: The ts of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastAck.
        :rtype: datetime
        """
        return self._ts

    @ts.setter
    def ts(self, ts):
        """Sets the ts of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastAck.

        Last time the server was acked.

        :param ts: The ts of this GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastAck.
        :type ts: datetime
        """

        self._ts = ts
