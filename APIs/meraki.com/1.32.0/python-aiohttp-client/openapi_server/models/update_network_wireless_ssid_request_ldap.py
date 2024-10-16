# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.update_network_wireless_ssid_request_ldap_credentials import UpdateNetworkWirelessSsidRequestLdapCredentials
from openapi_server.models.update_network_wireless_ssid_request_ldap_server_ca_certificate import UpdateNetworkWirelessSsidRequestLdapServerCaCertificate
from openapi_server.models.update_network_wireless_ssid_request_ldap_servers_inner import UpdateNetworkWirelessSsidRequestLdapServersInner
from openapi_server import util


class UpdateNetworkWirelessSsidRequestLdap(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, base_distinguished_name: str=None, credentials: UpdateNetworkWirelessSsidRequestLdapCredentials=None, server_ca_certificate: UpdateNetworkWirelessSsidRequestLdapServerCaCertificate=None, servers: List[UpdateNetworkWirelessSsidRequestLdapServersInner]=None):
        """UpdateNetworkWirelessSsidRequestLdap - a model defined in OpenAPI

        :param base_distinguished_name: The base_distinguished_name of this UpdateNetworkWirelessSsidRequestLdap.
        :param credentials: The credentials of this UpdateNetworkWirelessSsidRequestLdap.
        :param server_ca_certificate: The server_ca_certificate of this UpdateNetworkWirelessSsidRequestLdap.
        :param servers: The servers of this UpdateNetworkWirelessSsidRequestLdap.
        """
        self.openapi_types = {
            'base_distinguished_name': str,
            'credentials': UpdateNetworkWirelessSsidRequestLdapCredentials,
            'server_ca_certificate': UpdateNetworkWirelessSsidRequestLdapServerCaCertificate,
            'servers': List[UpdateNetworkWirelessSsidRequestLdapServersInner]
        }

        self.attribute_map = {
            'base_distinguished_name': 'baseDistinguishedName',
            'credentials': 'credentials',
            'server_ca_certificate': 'serverCaCertificate',
            'servers': 'servers'
        }

        self._base_distinguished_name = base_distinguished_name
        self._credentials = credentials
        self._server_ca_certificate = server_ca_certificate
        self._servers = servers

    @classmethod
    def from_dict(cls, dikt: dict) -> 'UpdateNetworkWirelessSsidRequestLdap':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The updateNetworkWirelessSsid_request_ldap of this UpdateNetworkWirelessSsidRequestLdap.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def base_distinguished_name(self):
        """Gets the base_distinguished_name of this UpdateNetworkWirelessSsidRequestLdap.

        The base distinguished name of users on the LDAP server.

        :return: The base_distinguished_name of this UpdateNetworkWirelessSsidRequestLdap.
        :rtype: str
        """
        return self._base_distinguished_name

    @base_distinguished_name.setter
    def base_distinguished_name(self, base_distinguished_name):
        """Sets the base_distinguished_name of this UpdateNetworkWirelessSsidRequestLdap.

        The base distinguished name of users on the LDAP server.

        :param base_distinguished_name: The base_distinguished_name of this UpdateNetworkWirelessSsidRequestLdap.
        :type base_distinguished_name: str
        """

        self._base_distinguished_name = base_distinguished_name

    @property
    def credentials(self):
        """Gets the credentials of this UpdateNetworkWirelessSsidRequestLdap.


        :return: The credentials of this UpdateNetworkWirelessSsidRequestLdap.
        :rtype: UpdateNetworkWirelessSsidRequestLdapCredentials
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this UpdateNetworkWirelessSsidRequestLdap.


        :param credentials: The credentials of this UpdateNetworkWirelessSsidRequestLdap.
        :type credentials: UpdateNetworkWirelessSsidRequestLdapCredentials
        """

        self._credentials = credentials

    @property
    def server_ca_certificate(self):
        """Gets the server_ca_certificate of this UpdateNetworkWirelessSsidRequestLdap.


        :return: The server_ca_certificate of this UpdateNetworkWirelessSsidRequestLdap.
        :rtype: UpdateNetworkWirelessSsidRequestLdapServerCaCertificate
        """
        return self._server_ca_certificate

    @server_ca_certificate.setter
    def server_ca_certificate(self, server_ca_certificate):
        """Sets the server_ca_certificate of this UpdateNetworkWirelessSsidRequestLdap.


        :param server_ca_certificate: The server_ca_certificate of this UpdateNetworkWirelessSsidRequestLdap.
        :type server_ca_certificate: UpdateNetworkWirelessSsidRequestLdapServerCaCertificate
        """

        self._server_ca_certificate = server_ca_certificate

    @property
    def servers(self):
        """Gets the servers of this UpdateNetworkWirelessSsidRequestLdap.

        The LDAP servers to be used for authentication.

        :return: The servers of this UpdateNetworkWirelessSsidRequestLdap.
        :rtype: List[UpdateNetworkWirelessSsidRequestLdapServersInner]
        """
        return self._servers

    @servers.setter
    def servers(self, servers):
        """Sets the servers of this UpdateNetworkWirelessSsidRequestLdap.

        The LDAP servers to be used for authentication.

        :param servers: The servers of this UpdateNetworkWirelessSsidRequestLdap.
        :type servers: List[UpdateNetworkWirelessSsidRequestLdapServersInner]
        """

        self._servers = servers
