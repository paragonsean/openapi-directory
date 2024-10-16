# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.get_network_wireless_settings200_response_named_vlans_pool_dhcp_monitoring import GetNetworkWirelessSettings200ResponseNamedVlansPoolDhcpMonitoring
from openapi_server import util


class GetNetworkWirelessSettings200ResponseNamedVlans(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, pool_dhcp_monitoring: GetNetworkWirelessSettings200ResponseNamedVlansPoolDhcpMonitoring=None):
        """GetNetworkWirelessSettings200ResponseNamedVlans - a model defined in OpenAPI

        :param pool_dhcp_monitoring: The pool_dhcp_monitoring of this GetNetworkWirelessSettings200ResponseNamedVlans.
        """
        self.openapi_types = {
            'pool_dhcp_monitoring': GetNetworkWirelessSettings200ResponseNamedVlansPoolDhcpMonitoring
        }

        self.attribute_map = {
            'pool_dhcp_monitoring': 'poolDhcpMonitoring'
        }

        self._pool_dhcp_monitoring = pool_dhcp_monitoring

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GetNetworkWirelessSettings200ResponseNamedVlans':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The getNetworkWirelessSettings_200_response_namedVlans of this GetNetworkWirelessSettings200ResponseNamedVlans.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def pool_dhcp_monitoring(self):
        """Gets the pool_dhcp_monitoring of this GetNetworkWirelessSettings200ResponseNamedVlans.


        :return: The pool_dhcp_monitoring of this GetNetworkWirelessSettings200ResponseNamedVlans.
        :rtype: GetNetworkWirelessSettings200ResponseNamedVlansPoolDhcpMonitoring
        """
        return self._pool_dhcp_monitoring

    @pool_dhcp_monitoring.setter
    def pool_dhcp_monitoring(self, pool_dhcp_monitoring):
        """Sets the pool_dhcp_monitoring of this GetNetworkWirelessSettings200ResponseNamedVlans.


        :param pool_dhcp_monitoring: The pool_dhcp_monitoring of this GetNetworkWirelessSettings200ResponseNamedVlans.
        :type pool_dhcp_monitoring: GetNetworkWirelessSettings200ResponseNamedVlansPoolDhcpMonitoring
        """

        self._pool_dhcp_monitoring = pool_dhcp_monitoring
