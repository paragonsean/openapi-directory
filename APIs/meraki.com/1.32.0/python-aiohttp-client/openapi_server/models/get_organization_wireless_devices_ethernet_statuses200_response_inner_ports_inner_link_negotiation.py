# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerPortsInnerLinkNegotiation(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, duplex: str=None, speed: int=None):
        """GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerPortsInnerLinkNegotiation - a model defined in OpenAPI

        :param duplex: The duplex of this GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerPortsInnerLinkNegotiation.
        :param speed: The speed of this GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerPortsInnerLinkNegotiation.
        """
        self.openapi_types = {
            'duplex': str,
            'speed': int
        }

        self.attribute_map = {
            'duplex': 'duplex',
            'speed': 'speed'
        }

        self._duplex = duplex
        self._speed = speed

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerPortsInnerLinkNegotiation':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The getOrganizationWirelessDevicesEthernetStatuses_200_response_inner_ports_inner_linkNegotiation of this GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerPortsInnerLinkNegotiation.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def duplex(self):
        """Gets the duplex of this GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerPortsInnerLinkNegotiation.

        The duplex mode of the port. Can be 'full' or 'half'

        :return: The duplex of this GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerPortsInnerLinkNegotiation.
        :rtype: str
        """
        return self._duplex

    @duplex.setter
    def duplex(self, duplex):
        """Sets the duplex of this GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerPortsInnerLinkNegotiation.

        The duplex mode of the port. Can be 'full' or 'half'

        :param duplex: The duplex of this GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerPortsInnerLinkNegotiation.
        :type duplex: str
        """

        self._duplex = duplex

    @property
    def speed(self):
        """Gets the speed of this GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerPortsInnerLinkNegotiation.

        The speed of the port

        :return: The speed of this GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerPortsInnerLinkNegotiation.
        :rtype: int
        """
        return self._speed

    @speed.setter
    def speed(self, speed):
        """Sets the speed of this GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerPortsInnerLinkNegotiation.

        The speed of the port

        :param speed: The speed of this GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerPortsInnerLinkNegotiation.
        :type speed: int
        """

        self._speed = speed
