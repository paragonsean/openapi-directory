# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ConfigSYSLOG(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, client: str=None, hostname: str=None, localport: int=None, separator: str=None, sequence: int=None, server: str=None, serverport: int=None, timestamp: str=None):
        """ConfigSYSLOG - a model defined in OpenAPI

        :param client: The client of this ConfigSYSLOG.
        :param hostname: The hostname of this ConfigSYSLOG.
        :param localport: The localport of this ConfigSYSLOG.
        :param separator: The separator of this ConfigSYSLOG.
        :param sequence: The sequence of this ConfigSYSLOG.
        :param server: The server of this ConfigSYSLOG.
        :param serverport: The serverport of this ConfigSYSLOG.
        :param timestamp: The timestamp of this ConfigSYSLOG.
        """
        self.openapi_types = {
            'client': str,
            'hostname': str,
            'localport': int,
            'separator': str,
            'sequence': int,
            'server': str,
            'serverport': int,
            'timestamp': str
        }

        self.attribute_map = {
            'client': 'client',
            'hostname': 'hostname',
            'localport': 'localport',
            'separator': 'separator',
            'sequence': 'sequence',
            'server': 'server',
            'serverport': 'serverport',
            'timestamp': 'timestamp'
        }

        self._client = client
        self._hostname = hostname
        self._localport = localport
        self._separator = separator
        self._sequence = sequence
        self._server = server
        self._serverport = serverport
        self._timestamp = timestamp

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ConfigSYSLOG':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ConfigSYSLOG of this ConfigSYSLOG.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def client(self):
        """Gets the client of this ConfigSYSLOG.


        :return: The client of this ConfigSYSLOG.
        :rtype: str
        """
        return self._client

    @client.setter
    def client(self, client):
        """Sets the client of this ConfigSYSLOG.


        :param client: The client of this ConfigSYSLOG.
        :type client: str
        """

        self._client = client

    @property
    def hostname(self):
        """Gets the hostname of this ConfigSYSLOG.


        :return: The hostname of this ConfigSYSLOG.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this ConfigSYSLOG.


        :param hostname: The hostname of this ConfigSYSLOG.
        :type hostname: str
        """

        self._hostname = hostname

    @property
    def localport(self):
        """Gets the localport of this ConfigSYSLOG.


        :return: The localport of this ConfigSYSLOG.
        :rtype: int
        """
        return self._localport

    @localport.setter
    def localport(self, localport):
        """Sets the localport of this ConfigSYSLOG.


        :param localport: The localport of this ConfigSYSLOG.
        :type localport: int
        """

        self._localport = localport

    @property
    def separator(self):
        """Gets the separator of this ConfigSYSLOG.


        :return: The separator of this ConfigSYSLOG.
        :rtype: str
        """
        return self._separator

    @separator.setter
    def separator(self, separator):
        """Sets the separator of this ConfigSYSLOG.


        :param separator: The separator of this ConfigSYSLOG.
        :type separator: str
        """

        self._separator = separator

    @property
    def sequence(self):
        """Gets the sequence of this ConfigSYSLOG.


        :return: The sequence of this ConfigSYSLOG.
        :rtype: int
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        """Sets the sequence of this ConfigSYSLOG.


        :param sequence: The sequence of this ConfigSYSLOG.
        :type sequence: int
        """

        self._sequence = sequence

    @property
    def server(self):
        """Gets the server of this ConfigSYSLOG.


        :return: The server of this ConfigSYSLOG.
        :rtype: str
        """
        return self._server

    @server.setter
    def server(self, server):
        """Sets the server of this ConfigSYSLOG.


        :param server: The server of this ConfigSYSLOG.
        :type server: str
        """

        self._server = server

    @property
    def serverport(self):
        """Gets the serverport of this ConfigSYSLOG.


        :return: The serverport of this ConfigSYSLOG.
        :rtype: int
        """
        return self._serverport

    @serverport.setter
    def serverport(self, serverport):
        """Sets the serverport of this ConfigSYSLOG.


        :param serverport: The serverport of this ConfigSYSLOG.
        :type serverport: int
        """

        self._serverport = serverport

    @property
    def timestamp(self):
        """Gets the timestamp of this ConfigSYSLOG.


        :return: The timestamp of this ConfigSYSLOG.
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this ConfigSYSLOG.


        :param timestamp: The timestamp of this ConfigSYSLOG.
        :type timestamp: str
        """

        self._timestamp = timestamp
