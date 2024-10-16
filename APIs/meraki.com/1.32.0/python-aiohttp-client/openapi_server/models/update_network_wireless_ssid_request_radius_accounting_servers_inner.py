# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class UpdateNetworkWirelessSsidRequestRadiusAccountingServersInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, ca_certificate: str=None, host: str=None, port: int=None, radsec_enabled: bool=None, secret: str=None):
        """UpdateNetworkWirelessSsidRequestRadiusAccountingServersInner - a model defined in OpenAPI

        :param ca_certificate: The ca_certificate of this UpdateNetworkWirelessSsidRequestRadiusAccountingServersInner.
        :param host: The host of this UpdateNetworkWirelessSsidRequestRadiusAccountingServersInner.
        :param port: The port of this UpdateNetworkWirelessSsidRequestRadiusAccountingServersInner.
        :param radsec_enabled: The radsec_enabled of this UpdateNetworkWirelessSsidRequestRadiusAccountingServersInner.
        :param secret: The secret of this UpdateNetworkWirelessSsidRequestRadiusAccountingServersInner.
        """
        self.openapi_types = {
            'ca_certificate': str,
            'host': str,
            'port': int,
            'radsec_enabled': bool,
            'secret': str
        }

        self.attribute_map = {
            'ca_certificate': 'caCertificate',
            'host': 'host',
            'port': 'port',
            'radsec_enabled': 'radsecEnabled',
            'secret': 'secret'
        }

        self._ca_certificate = ca_certificate
        self._host = host
        self._port = port
        self._radsec_enabled = radsec_enabled
        self._secret = secret

    @classmethod
    def from_dict(cls, dikt: dict) -> 'UpdateNetworkWirelessSsidRequestRadiusAccountingServersInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The updateNetworkWirelessSsid_request_radiusAccountingServers_inner of this UpdateNetworkWirelessSsidRequestRadiusAccountingServersInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ca_certificate(self):
        """Gets the ca_certificate of this UpdateNetworkWirelessSsidRequestRadiusAccountingServersInner.

        Certificate used for authorization for the RADSEC Server

        :return: The ca_certificate of this UpdateNetworkWirelessSsidRequestRadiusAccountingServersInner.
        :rtype: str
        """
        return self._ca_certificate

    @ca_certificate.setter
    def ca_certificate(self, ca_certificate):
        """Sets the ca_certificate of this UpdateNetworkWirelessSsidRequestRadiusAccountingServersInner.

        Certificate used for authorization for the RADSEC Server

        :param ca_certificate: The ca_certificate of this UpdateNetworkWirelessSsidRequestRadiusAccountingServersInner.
        :type ca_certificate: str
        """

        self._ca_certificate = ca_certificate

    @property
    def host(self):
        """Gets the host of this UpdateNetworkWirelessSsidRequestRadiusAccountingServersInner.

        IP address to which the APs will send RADIUS accounting messages

        :return: The host of this UpdateNetworkWirelessSsidRequestRadiusAccountingServersInner.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this UpdateNetworkWirelessSsidRequestRadiusAccountingServersInner.

        IP address to which the APs will send RADIUS accounting messages

        :param host: The host of this UpdateNetworkWirelessSsidRequestRadiusAccountingServersInner.
        :type host: str
        """
        if host is None:
            raise ValueError("Invalid value for `host`, must not be `None`")

        self._host = host

    @property
    def port(self):
        """Gets the port of this UpdateNetworkWirelessSsidRequestRadiusAccountingServersInner.

        Port on the RADIUS server that is listening for accounting messages

        :return: The port of this UpdateNetworkWirelessSsidRequestRadiusAccountingServersInner.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this UpdateNetworkWirelessSsidRequestRadiusAccountingServersInner.

        Port on the RADIUS server that is listening for accounting messages

        :param port: The port of this UpdateNetworkWirelessSsidRequestRadiusAccountingServersInner.
        :type port: int
        """

        self._port = port

    @property
    def radsec_enabled(self):
        """Gets the radsec_enabled of this UpdateNetworkWirelessSsidRequestRadiusAccountingServersInner.

        Use RADSEC (TLS over TCP) to connect to this RADIUS accounting server. Requires radiusProxyEnabled.

        :return: The radsec_enabled of this UpdateNetworkWirelessSsidRequestRadiusAccountingServersInner.
        :rtype: bool
        """
        return self._radsec_enabled

    @radsec_enabled.setter
    def radsec_enabled(self, radsec_enabled):
        """Sets the radsec_enabled of this UpdateNetworkWirelessSsidRequestRadiusAccountingServersInner.

        Use RADSEC (TLS over TCP) to connect to this RADIUS accounting server. Requires radiusProxyEnabled.

        :param radsec_enabled: The radsec_enabled of this UpdateNetworkWirelessSsidRequestRadiusAccountingServersInner.
        :type radsec_enabled: bool
        """

        self._radsec_enabled = radsec_enabled

    @property
    def secret(self):
        """Gets the secret of this UpdateNetworkWirelessSsidRequestRadiusAccountingServersInner.

        Shared key used to authenticate messages between the APs and RADIUS server

        :return: The secret of this UpdateNetworkWirelessSsidRequestRadiusAccountingServersInner.
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this UpdateNetworkWirelessSsidRequestRadiusAccountingServersInner.

        Shared key used to authenticate messages between the APs and RADIUS server

        :param secret: The secret of this UpdateNetworkWirelessSsidRequestRadiusAccountingServersInner.
        :type secret: str
        """

        self._secret = secret
