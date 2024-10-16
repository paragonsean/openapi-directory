# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Net(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, ethernet_connected: bool=None, ip_address: str=None, online: bool=None):
        """Net - a model defined in OpenAPI

        :param ethernet_connected: The ethernet_connected of this Net.
        :param ip_address: The ip_address of this Net.
        :param online: The online of this Net.
        """
        self.openapi_types = {
            'ethernet_connected': bool,
            'ip_address': str,
            'online': bool
        }

        self.attribute_map = {
            'ethernet_connected': 'ethernet_connected',
            'ip_address': 'ip_address',
            'online': 'online'
        }

        self._ethernet_connected = ethernet_connected
        self._ip_address = ip_address
        self._online = online

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Net':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Net of this Net.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ethernet_connected(self):
        """Gets the ethernet_connected of this Net.


        :return: The ethernet_connected of this Net.
        :rtype: bool
        """
        return self._ethernet_connected

    @ethernet_connected.setter
    def ethernet_connected(self, ethernet_connected):
        """Sets the ethernet_connected of this Net.


        :param ethernet_connected: The ethernet_connected of this Net.
        :type ethernet_connected: bool
        """
        if ethernet_connected is None:
            raise ValueError("Invalid value for `ethernet_connected`, must not be `None`")

        self._ethernet_connected = ethernet_connected

    @property
    def ip_address(self):
        """Gets the ip_address of this Net.


        :return: The ip_address of this Net.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this Net.


        :param ip_address: The ip_address of this Net.
        :type ip_address: str
        """
        if ip_address is None:
            raise ValueError("Invalid value for `ip_address`, must not be `None`")

        self._ip_address = ip_address

    @property
    def online(self):
        """Gets the online of this Net.


        :return: The online of this Net.
        :rtype: bool
        """
        return self._online

    @online.setter
    def online(self, online):
        """Sets the online of this Net.


        :param online: The online of this Net.
        :type online: bool
        """
        if online is None:
            raise ValueError("Invalid value for `online`, must not be `None`")

        self._online = online
