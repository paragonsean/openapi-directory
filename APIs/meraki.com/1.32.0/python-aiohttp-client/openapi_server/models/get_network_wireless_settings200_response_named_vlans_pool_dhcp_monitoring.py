# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class GetNetworkWirelessSettings200ResponseNamedVlansPoolDhcpMonitoring(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, duration: int=None, enabled: bool=None):
        """GetNetworkWirelessSettings200ResponseNamedVlansPoolDhcpMonitoring - a model defined in OpenAPI

        :param duration: The duration of this GetNetworkWirelessSettings200ResponseNamedVlansPoolDhcpMonitoring.
        :param enabled: The enabled of this GetNetworkWirelessSettings200ResponseNamedVlansPoolDhcpMonitoring.
        """
        self.openapi_types = {
            'duration': int,
            'enabled': bool
        }

        self.attribute_map = {
            'duration': 'duration',
            'enabled': 'enabled'
        }

        self._duration = duration
        self._enabled = enabled

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GetNetworkWirelessSettings200ResponseNamedVlansPoolDhcpMonitoring':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The getNetworkWirelessSettings_200_response_namedVlans_poolDhcpMonitoring of this GetNetworkWirelessSettings200ResponseNamedVlansPoolDhcpMonitoring.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def duration(self):
        """Gets the duration of this GetNetworkWirelessSettings200ResponseNamedVlansPoolDhcpMonitoring.

        The duration in minutes that devices will refrain from using dirty VLANs before adding them back to the pool.

        :return: The duration of this GetNetworkWirelessSettings200ResponseNamedVlansPoolDhcpMonitoring.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this GetNetworkWirelessSettings200ResponseNamedVlansPoolDhcpMonitoring.

        The duration in minutes that devices will refrain from using dirty VLANs before adding them back to the pool.

        :param duration: The duration of this GetNetworkWirelessSettings200ResponseNamedVlansPoolDhcpMonitoring.
        :type duration: int
        """

        self._duration = duration

    @property
    def enabled(self):
        """Gets the enabled of this GetNetworkWirelessSettings200ResponseNamedVlansPoolDhcpMonitoring.

        Whether or not devices using named VLAN pools should remove dirty VLANs from the pool, thereby preventing clients from being assigned to VLANs where they would be unable to obtain an IP address via DHCP

        :return: The enabled of this GetNetworkWirelessSettings200ResponseNamedVlansPoolDhcpMonitoring.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this GetNetworkWirelessSettings200ResponseNamedVlansPoolDhcpMonitoring.

        Whether or not devices using named VLAN pools should remove dirty VLANs from the pool, thereby preventing clients from being assigned to VLANs where they would be unable to obtain an IP address via DHCP

        :param enabled: The enabled of this GetNetworkWirelessSettings200ResponseNamedVlansPoolDhcpMonitoring.
        :type enabled: bool
        """

        self._enabled = enabled
