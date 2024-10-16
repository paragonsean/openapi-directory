# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.get_network_syslog_servers200_response_servers_inner import GetNetworkSyslogServers200ResponseServersInner
from openapi_server import util


class GetNetworkSyslogServers200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, servers: List[GetNetworkSyslogServers200ResponseServersInner]=None):
        """GetNetworkSyslogServers200Response - a model defined in OpenAPI

        :param servers: The servers of this GetNetworkSyslogServers200Response.
        """
        self.openapi_types = {
            'servers': List[GetNetworkSyslogServers200ResponseServersInner]
        }

        self.attribute_map = {
            'servers': 'servers'
        }

        self._servers = servers

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GetNetworkSyslogServers200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The getNetworkSyslogServers_200_response of this GetNetworkSyslogServers200Response.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def servers(self):
        """Gets the servers of this GetNetworkSyslogServers200Response.

        List of the syslog servers for this network

        :return: The servers of this GetNetworkSyslogServers200Response.
        :rtype: List[GetNetworkSyslogServers200ResponseServersInner]
        """
        return self._servers

    @servers.setter
    def servers(self, servers):
        """Sets the servers of this GetNetworkSyslogServers200Response.

        List of the syslog servers for this network

        :param servers: The servers of this GetNetworkSyslogServers200Response.
        :type servers: List[GetNetworkSyslogServers200ResponseServersInner]
        """

        self._servers = servers
