# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class UpdateNetworkWirelessSsidRequestLdapServersInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, host: str=None, port: int=None):
        """UpdateNetworkWirelessSsidRequestLdapServersInner - a model defined in OpenAPI

        :param host: The host of this UpdateNetworkWirelessSsidRequestLdapServersInner.
        :param port: The port of this UpdateNetworkWirelessSsidRequestLdapServersInner.
        """
        self.openapi_types = {
            'host': str,
            'port': int
        }

        self.attribute_map = {
            'host': 'host',
            'port': 'port'
        }

        self._host = host
        self._port = port

    @classmethod
    def from_dict(cls, dikt: dict) -> 'UpdateNetworkWirelessSsidRequestLdapServersInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The updateNetworkWirelessSsid_request_ldap_servers_inner of this UpdateNetworkWirelessSsidRequestLdapServersInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def host(self):
        """Gets the host of this UpdateNetworkWirelessSsidRequestLdapServersInner.

        IP address of your LDAP server.

        :return: The host of this UpdateNetworkWirelessSsidRequestLdapServersInner.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this UpdateNetworkWirelessSsidRequestLdapServersInner.

        IP address of your LDAP server.

        :param host: The host of this UpdateNetworkWirelessSsidRequestLdapServersInner.
        :type host: str
        """
        if host is None:
            raise ValueError("Invalid value for `host`, must not be `None`")

        self._host = host

    @property
    def port(self):
        """Gets the port of this UpdateNetworkWirelessSsidRequestLdapServersInner.

        UDP port the LDAP server listens on.

        :return: The port of this UpdateNetworkWirelessSsidRequestLdapServersInner.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this UpdateNetworkWirelessSsidRequestLdapServersInner.

        UDP port the LDAP server listens on.

        :param port: The port of this UpdateNetworkWirelessSsidRequestLdapServersInner.
        :type port: int
        """
        if port is None:
            raise ValueError("Invalid value for `port`, must not be `None`")

        self._port = port
