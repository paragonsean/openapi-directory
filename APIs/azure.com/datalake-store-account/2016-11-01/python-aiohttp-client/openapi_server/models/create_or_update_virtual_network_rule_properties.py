# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class CreateOrUpdateVirtualNetworkRuleProperties(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, subnet_id: str=None):
        """CreateOrUpdateVirtualNetworkRuleProperties - a model defined in OpenAPI

        :param subnet_id: The subnet_id of this CreateOrUpdateVirtualNetworkRuleProperties.
        """
        self.openapi_types = {
            'subnet_id': str
        }

        self.attribute_map = {
            'subnet_id': 'subnetId'
        }

        self._subnet_id = subnet_id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CreateOrUpdateVirtualNetworkRuleProperties':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The CreateOrUpdateVirtualNetworkRuleProperties of this CreateOrUpdateVirtualNetworkRuleProperties.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def subnet_id(self):
        """Gets the subnet_id of this CreateOrUpdateVirtualNetworkRuleProperties.

        The resource identifier for the subnet.

        :return: The subnet_id of this CreateOrUpdateVirtualNetworkRuleProperties.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this CreateOrUpdateVirtualNetworkRuleProperties.

        The resource identifier for the subnet.

        :param subnet_id: The subnet_id of this CreateOrUpdateVirtualNetworkRuleProperties.
        :type subnet_id: str
        """
        if subnet_id is None:
            raise ValueError("Invalid value for `subnet_id`, must not be `None`")

        self._subnet_id = subnet_id
