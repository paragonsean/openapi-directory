# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class SecondaryDNSSettings(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, secondary_dns_servers: List[str]=None):
        """SecondaryDNSSettings - a model defined in OpenAPI

        :param secondary_dns_servers: The secondary_dns_servers of this SecondaryDNSSettings.
        """
        self.openapi_types = {
            'secondary_dns_servers': List[str]
        }

        self.attribute_map = {
            'secondary_dns_servers': 'secondaryDnsServers'
        }

        self._secondary_dns_servers = secondary_dns_servers

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SecondaryDNSSettings':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The SecondaryDNSSettings of this SecondaryDNSSettings.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def secondary_dns_servers(self):
        """Gets the secondary_dns_servers of this SecondaryDNSSettings.

        The list of secondary DNS Server IP addresses.

        :return: The secondary_dns_servers of this SecondaryDNSSettings.
        :rtype: List[str]
        """
        return self._secondary_dns_servers

    @secondary_dns_servers.setter
    def secondary_dns_servers(self, secondary_dns_servers):
        """Sets the secondary_dns_servers of this SecondaryDNSSettings.

        The list of secondary DNS Server IP addresses.

        :param secondary_dns_servers: The secondary_dns_servers of this SecondaryDNSSettings.
        :type secondary_dns_servers: List[str]
        """

        self._secondary_dns_servers = secondary_dns_servers
