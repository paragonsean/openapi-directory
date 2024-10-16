# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class EditNameServers(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, domain_name: str=None, name_servers: List[str]=None):
        """EditNameServers - a model defined in OpenAPI

        :param domain_name: The domain_name of this EditNameServers.
        :param name_servers: The name_servers of this EditNameServers.
        """
        self.openapi_types = {
            'domain_name': str,
            'name_servers': List[str]
        }

        self.attribute_map = {
            'domain_name': 'domain_name',
            'name_servers': 'name_servers'
        }

        self._domain_name = domain_name
        self._name_servers = name_servers

    @classmethod
    def from_dict(cls, dikt: dict) -> 'EditNameServers':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The EditNameServers of this EditNameServers.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def domain_name(self):
        """Gets the domain_name of this EditNameServers.

        The domain name to register.

        :return: The domain_name of this EditNameServers.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this EditNameServers.

        The domain name to register.

        :param domain_name: The domain_name of this EditNameServers.
        :type domain_name: str
        """

        self._domain_name = domain_name

    @property
    def name_servers(self):
        """Gets the name_servers of this EditNameServers.

        List of name servers.

        :return: The name_servers of this EditNameServers.
        :rtype: List[str]
        """
        return self._name_servers

    @name_servers.setter
    def name_servers(self, name_servers):
        """Sets the name_servers of this EditNameServers.

        List of name servers.

        :param name_servers: The name_servers of this EditNameServers.
        :type name_servers: List[str]
        """

        self._name_servers = name_servers
