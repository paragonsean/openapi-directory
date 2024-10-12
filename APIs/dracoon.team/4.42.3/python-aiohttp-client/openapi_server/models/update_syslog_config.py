# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class UpdateSyslogConfig(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, enabled: bool=None, host: str=None, log_ip_enabled: bool=None, port: int=None, protocol: str=None):
        """UpdateSyslogConfig - a model defined in OpenAPI

        :param enabled: The enabled of this UpdateSyslogConfig.
        :param host: The host of this UpdateSyslogConfig.
        :param log_ip_enabled: The log_ip_enabled of this UpdateSyslogConfig.
        :param port: The port of this UpdateSyslogConfig.
        :param protocol: The protocol of this UpdateSyslogConfig.
        """
        self.openapi_types = {
            'enabled': bool,
            'host': str,
            'log_ip_enabled': bool,
            'port': int,
            'protocol': str
        }

        self.attribute_map = {
            'enabled': 'enabled',
            'host': 'host',
            'log_ip_enabled': 'logIpEnabled',
            'port': 'port',
            'protocol': 'protocol'
        }

        self._enabled = enabled
        self._host = host
        self._log_ip_enabled = log_ip_enabled
        self._port = port
        self._protocol = protocol

    @classmethod
    def from_dict(cls, dikt: dict) -> 'UpdateSyslogConfig':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The UpdateSyslogConfig of this UpdateSyslogConfig.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def enabled(self):
        """Gets the enabled of this UpdateSyslogConfig.

        Is syslog enabled?

        :return: The enabled of this UpdateSyslogConfig.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this UpdateSyslogConfig.

        Is syslog enabled?

        :param enabled: The enabled of this UpdateSyslogConfig.
        :type enabled: bool
        """

        self._enabled = enabled

    @property
    def host(self):
        """Gets the host of this UpdateSyslogConfig.

        Syslog server (IP or FQDN)

        :return: The host of this UpdateSyslogConfig.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this UpdateSyslogConfig.

        Syslog server (IP or FQDN)

        :param host: The host of this UpdateSyslogConfig.
        :type host: str
        """

        self._host = host

    @property
    def log_ip_enabled(self):
        """Gets the log_ip_enabled of this UpdateSyslogConfig.

        Determines whether user’s IP address is logged.

        :return: The log_ip_enabled of this UpdateSyslogConfig.
        :rtype: bool
        """
        return self._log_ip_enabled

    @log_ip_enabled.setter
    def log_ip_enabled(self, log_ip_enabled):
        """Sets the log_ip_enabled of this UpdateSyslogConfig.

        Determines whether user’s IP address is logged.

        :param log_ip_enabled: The log_ip_enabled of this UpdateSyslogConfig.
        :type log_ip_enabled: bool
        """

        self._log_ip_enabled = log_ip_enabled

    @property
    def port(self):
        """Gets the port of this UpdateSyslogConfig.

        Syslog server port

        :return: The port of this UpdateSyslogConfig.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this UpdateSyslogConfig.

        Syslog server port

        :param port: The port of this UpdateSyslogConfig.
        :type port: int
        """

        self._port = port

    @property
    def protocol(self):
        """Gets the protocol of this UpdateSyslogConfig.

        Protocol to connect to syslog server

        :return: The protocol of this UpdateSyslogConfig.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this UpdateSyslogConfig.

        Protocol to connect to syslog server

        :param protocol: The protocol of this UpdateSyslogConfig.
        :type protocol: str
        """
        allowed_values = ["TCP", "UDP"]  # noqa: E501
        if protocol not in allowed_values:
            raise ValueError(
                "Invalid value for `protocol` ({0}), must be one of {1}"
                .format(protocol, allowed_values)
            )

        self._protocol = protocol
