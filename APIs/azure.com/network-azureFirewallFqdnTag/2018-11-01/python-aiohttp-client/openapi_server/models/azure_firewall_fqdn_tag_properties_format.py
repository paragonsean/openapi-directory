# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class AzureFirewallFqdnTagPropertiesFormat(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, fqdn_tag_name: str=None, provisioning_state: str=None):
        """AzureFirewallFqdnTagPropertiesFormat - a model defined in OpenAPI

        :param fqdn_tag_name: The fqdn_tag_name of this AzureFirewallFqdnTagPropertiesFormat.
        :param provisioning_state: The provisioning_state of this AzureFirewallFqdnTagPropertiesFormat.
        """
        self.openapi_types = {
            'fqdn_tag_name': str,
            'provisioning_state': str
        }

        self.attribute_map = {
            'fqdn_tag_name': 'fqdnTagName',
            'provisioning_state': 'provisioningState'
        }

        self._fqdn_tag_name = fqdn_tag_name
        self._provisioning_state = provisioning_state

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AzureFirewallFqdnTagPropertiesFormat':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The AzureFirewallFqdnTagPropertiesFormat of this AzureFirewallFqdnTagPropertiesFormat.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def fqdn_tag_name(self):
        """Gets the fqdn_tag_name of this AzureFirewallFqdnTagPropertiesFormat.

        The name of this FQDN Tag.

        :return: The fqdn_tag_name of this AzureFirewallFqdnTagPropertiesFormat.
        :rtype: str
        """
        return self._fqdn_tag_name

    @fqdn_tag_name.setter
    def fqdn_tag_name(self, fqdn_tag_name):
        """Sets the fqdn_tag_name of this AzureFirewallFqdnTagPropertiesFormat.

        The name of this FQDN Tag.

        :param fqdn_tag_name: The fqdn_tag_name of this AzureFirewallFqdnTagPropertiesFormat.
        :type fqdn_tag_name: str
        """

        self._fqdn_tag_name = fqdn_tag_name

    @property
    def provisioning_state(self):
        """Gets the provisioning_state of this AzureFirewallFqdnTagPropertiesFormat.

        The provisioning state of the resource.

        :return: The provisioning_state of this AzureFirewallFqdnTagPropertiesFormat.
        :rtype: str
        """
        return self._provisioning_state

    @provisioning_state.setter
    def provisioning_state(self, provisioning_state):
        """Sets the provisioning_state of this AzureFirewallFqdnTagPropertiesFormat.

        The provisioning state of the resource.

        :param provisioning_state: The provisioning_state of this AzureFirewallFqdnTagPropertiesFormat.
        :type provisioning_state: str
        """

        self._provisioning_state = provisioning_state
