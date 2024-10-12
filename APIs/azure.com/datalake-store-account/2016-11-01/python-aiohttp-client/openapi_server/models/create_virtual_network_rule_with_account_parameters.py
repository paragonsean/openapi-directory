# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.create_or_update_virtual_network_rule_properties import CreateOrUpdateVirtualNetworkRuleProperties
from openapi_server import util


class CreateVirtualNetworkRuleWithAccountParameters(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name: str=None, properties: CreateOrUpdateVirtualNetworkRuleProperties=None):
        """CreateVirtualNetworkRuleWithAccountParameters - a model defined in OpenAPI

        :param name: The name of this CreateVirtualNetworkRuleWithAccountParameters.
        :param properties: The properties of this CreateVirtualNetworkRuleWithAccountParameters.
        """
        self.openapi_types = {
            'name': str,
            'properties': CreateOrUpdateVirtualNetworkRuleProperties
        }

        self.attribute_map = {
            'name': 'name',
            'properties': 'properties'
        }

        self._name = name
        self._properties = properties

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CreateVirtualNetworkRuleWithAccountParameters':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The CreateVirtualNetworkRuleWithAccountParameters of this CreateVirtualNetworkRuleWithAccountParameters.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this CreateVirtualNetworkRuleWithAccountParameters.

        The unique name of the virtual network rule to create.

        :return: The name of this CreateVirtualNetworkRuleWithAccountParameters.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateVirtualNetworkRuleWithAccountParameters.

        The unique name of the virtual network rule to create.

        :param name: The name of this CreateVirtualNetworkRuleWithAccountParameters.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def properties(self):
        """Gets the properties of this CreateVirtualNetworkRuleWithAccountParameters.


        :return: The properties of this CreateVirtualNetworkRuleWithAccountParameters.
        :rtype: CreateOrUpdateVirtualNetworkRuleProperties
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this CreateVirtualNetworkRuleWithAccountParameters.


        :param properties: The properties of this CreateVirtualNetworkRuleWithAccountParameters.
        :type properties: CreateOrUpdateVirtualNetworkRuleProperties
        """
        if properties is None:
            raise ValueError("Invalid value for `properties`, must not be `None`")

        self._properties = properties
