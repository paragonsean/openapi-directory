# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.metadatum import Metadatum
from openapi_server import util


class Instance(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, host: str=None, metadata: List[Metadatum]=None, port: int=None):
        """Instance - a model defined in OpenAPI

        :param host: The host of this Instance.
        :param metadata: The metadata of this Instance.
        :param port: The port of this Instance.
        """
        self.openapi_types = {
            'host': str,
            'metadata': List[Metadatum],
            'port': int
        }

        self.attribute_map = {
            'host': 'host',
            'metadata': 'metadata',
            'port': 'port'
        }

        self._host = host
        self._metadata = metadata
        self._port = port

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Instance':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Instance of this Instance.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def host(self):
        """Gets the host of this Instance.


        :return: The host of this Instance.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this Instance.


        :param host: The host of this Instance.
        :type host: str
        """

        self._host = host

    @property
    def metadata(self):
        """Gets the metadata of this Instance.


        :return: The metadata of this Instance.
        :rtype: List[Metadatum]
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this Instance.


        :param metadata: The metadata of this Instance.
        :type metadata: List[Metadatum]
        """

        self._metadata = metadata

    @property
    def port(self):
        """Gets the port of this Instance.


        :return: The port of this Instance.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this Instance.


        :param port: The port of this Instance.
        :type port: int
        """

        self._port = port
