# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.update_virtual_network_rule_properties import UpdateVirtualNetworkRuleProperties
from openapi_server import util


class UpdateVirtualNetworkRuleParameters(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, properties: UpdateVirtualNetworkRuleProperties=None):
        """UpdateVirtualNetworkRuleParameters - a model defined in OpenAPI

        :param properties: The properties of this UpdateVirtualNetworkRuleParameters.
        """
        self.openapi_types = {
            'properties': UpdateVirtualNetworkRuleProperties
        }

        self.attribute_map = {
            'properties': 'properties'
        }

        self._properties = properties

    @classmethod
    def from_dict(cls, dikt: dict) -> 'UpdateVirtualNetworkRuleParameters':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The UpdateVirtualNetworkRuleParameters of this UpdateVirtualNetworkRuleParameters.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def properties(self):
        """Gets the properties of this UpdateVirtualNetworkRuleParameters.


        :return: The properties of this UpdateVirtualNetworkRuleParameters.
        :rtype: UpdateVirtualNetworkRuleProperties
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this UpdateVirtualNetworkRuleParameters.


        :param properties: The properties of this UpdateVirtualNetworkRuleParameters.
        :type properties: UpdateVirtualNetworkRuleProperties
        """

        self._properties = properties
