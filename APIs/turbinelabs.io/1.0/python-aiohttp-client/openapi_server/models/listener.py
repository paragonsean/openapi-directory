# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.tracing_config import TracingConfig
from openapi_server import util


class Listener(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, domain_keys: List[str]=None, ip: str=None, name: str=None, port: int=None, protocol: str=None, tracing_config: TracingConfig=None, zone_key: str=None, checksum: str=None, listener_key: str=None):
        """Listener - a model defined in OpenAPI

        :param domain_keys: The domain_keys of this Listener.
        :param ip: The ip of this Listener.
        :param name: The name of this Listener.
        :param port: The port of this Listener.
        :param protocol: The protocol of this Listener.
        :param tracing_config: The tracing_config of this Listener.
        :param zone_key: The zone_key of this Listener.
        :param checksum: The checksum of this Listener.
        :param listener_key: The listener_key of this Listener.
        """
        self.openapi_types = {
            'domain_keys': List[str],
            'ip': str,
            'name': str,
            'port': int,
            'protocol': str,
            'tracing_config': TracingConfig,
            'zone_key': str,
            'checksum': str,
            'listener_key': str
        }

        self.attribute_map = {
            'domain_keys': 'domain_keys',
            'ip': 'ip',
            'name': 'name',
            'port': 'port',
            'protocol': 'protocol',
            'tracing_config': 'tracing_config',
            'zone_key': 'zone_key',
            'checksum': 'checksum',
            'listener_key': 'listener_key'
        }

        self._domain_keys = domain_keys
        self._ip = ip
        self._name = name
        self._port = port
        self._protocol = protocol
        self._tracing_config = tracing_config
        self._zone_key = zone_key
        self._checksum = checksum
        self._listener_key = listener_key

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Listener':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Listener of this Listener.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def domain_keys(self):
        """Gets the domain_keys of this Listener.


        :return: The domain_keys of this Listener.
        :rtype: List[str]
        """
        return self._domain_keys

    @domain_keys.setter
    def domain_keys(self, domain_keys):
        """Sets the domain_keys of this Listener.


        :param domain_keys: The domain_keys of this Listener.
        :type domain_keys: List[str]
        """

        self._domain_keys = domain_keys

    @property
    def ip(self):
        """Gets the ip of this Listener.

        the interface this listener should bind to.

        :return: The ip of this Listener.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this Listener.

        the interface this listener should bind to.

        :param ip: The ip of this Listener.
        :type ip: str
        """

        self._ip = ip

    @property
    def name(self):
        """Gets the name of this Listener.


        :return: The name of this Listener.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Listener.


        :param name: The name of this Listener.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def port(self):
        """Gets the port of this Listener.

        the port this listener should bind to.

        :return: The port of this Listener.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this Listener.

        the port this listener should bind to.

        :param port: The port of this Listener.
        :type port: int
        """
        if port is None:
            raise ValueError("Invalid value for `port`, must not be `None`")

        self._port = port

    @property
    def protocol(self):
        """Gets the protocol of this Listener.

        the protocol this listener will handle. http and http2 configure the listener to only process requests of that type. http_auto will adapt to HTTP/1.1 and HTTP/2 as needed. tcp configures the listener to be a tcp proxy 

        :return: The protocol of this Listener.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this Listener.

        the protocol this listener will handle. http and http2 configure the listener to only process requests of that type. http_auto will adapt to HTTP/1.1 and HTTP/2 as needed. tcp configures the listener to be a tcp proxy 

        :param protocol: The protocol of this Listener.
        :type protocol: str
        """
        allowed_values = ["http", "http2", "http_auto", "tcp"]  # noqa: E501
        if protocol not in allowed_values:
            raise ValueError(
                "Invalid value for `protocol` ({0}), must be one of {1}"
                .format(protocol, allowed_values)
            )

        self._protocol = protocol

    @property
    def tracing_config(self):
        """Gets the tracing_config of this Listener.


        :return: The tracing_config of this Listener.
        :rtype: TracingConfig
        """
        return self._tracing_config

    @tracing_config.setter
    def tracing_config(self, tracing_config):
        """Sets the tracing_config of this Listener.


        :param tracing_config: The tracing_config of this Listener.
        :type tracing_config: TracingConfig
        """

        self._tracing_config = tracing_config

    @property
    def zone_key(self):
        """Gets the zone_key of this Listener.


        :return: The zone_key of this Listener.
        :rtype: str
        """
        return self._zone_key

    @zone_key.setter
    def zone_key(self, zone_key):
        """Sets the zone_key of this Listener.


        :param zone_key: The zone_key of this Listener.
        :type zone_key: str
        """

        self._zone_key = zone_key

    @property
    def checksum(self):
        """Gets the checksum of this Listener.


        :return: The checksum of this Listener.
        :rtype: str
        """
        return self._checksum

    @checksum.setter
    def checksum(self, checksum):
        """Sets the checksum of this Listener.


        :param checksum: The checksum of this Listener.
        :type checksum: str
        """
        if checksum is None:
            raise ValueError("Invalid value for `checksum`, must not be `None`")

        self._checksum = checksum

    @property
    def listener_key(self):
        """Gets the listener_key of this Listener.


        :return: The listener_key of this Listener.
        :rtype: str
        """
        return self._listener_key

    @listener_key.setter
    def listener_key(self, listener_key):
        """Sets the listener_key of this Listener.


        :param listener_key: The listener_key of this Listener.
        :type listener_key: str
        """
        if listener_key is None:
            raise ValueError("Invalid value for `listener_key`, must not be `None`")

        self._listener_key = listener_key
