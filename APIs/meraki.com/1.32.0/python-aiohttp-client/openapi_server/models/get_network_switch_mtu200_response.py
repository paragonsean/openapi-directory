# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.get_network_switch_mtu200_response_overrides_inner import GetNetworkSwitchMtu200ResponseOverridesInner
from openapi_server import util


class GetNetworkSwitchMtu200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, default_mtu_size: int=None, overrides: List[GetNetworkSwitchMtu200ResponseOverridesInner]=None):
        """GetNetworkSwitchMtu200Response - a model defined in OpenAPI

        :param default_mtu_size: The default_mtu_size of this GetNetworkSwitchMtu200Response.
        :param overrides: The overrides of this GetNetworkSwitchMtu200Response.
        """
        self.openapi_types = {
            'default_mtu_size': int,
            'overrides': List[GetNetworkSwitchMtu200ResponseOverridesInner]
        }

        self.attribute_map = {
            'default_mtu_size': 'defaultMtuSize',
            'overrides': 'overrides'
        }

        self._default_mtu_size = default_mtu_size
        self._overrides = overrides

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GetNetworkSwitchMtu200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The getNetworkSwitchMtu_200_response of this GetNetworkSwitchMtu200Response.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def default_mtu_size(self):
        """Gets the default_mtu_size of this GetNetworkSwitchMtu200Response.

        MTU size for the entire network. Default value is 9578.

        :return: The default_mtu_size of this GetNetworkSwitchMtu200Response.
        :rtype: int
        """
        return self._default_mtu_size

    @default_mtu_size.setter
    def default_mtu_size(self, default_mtu_size):
        """Sets the default_mtu_size of this GetNetworkSwitchMtu200Response.

        MTU size for the entire network. Default value is 9578.

        :param default_mtu_size: The default_mtu_size of this GetNetworkSwitchMtu200Response.
        :type default_mtu_size: int
        """

        self._default_mtu_size = default_mtu_size

    @property
    def overrides(self):
        """Gets the overrides of this GetNetworkSwitchMtu200Response.

        Override MTU size for individual switches or switch profiles.       An empty array will clear overrides.

        :return: The overrides of this GetNetworkSwitchMtu200Response.
        :rtype: List[GetNetworkSwitchMtu200ResponseOverridesInner]
        """
        return self._overrides

    @overrides.setter
    def overrides(self, overrides):
        """Sets the overrides of this GetNetworkSwitchMtu200Response.

        Override MTU size for individual switches or switch profiles.       An empty array will clear overrides.

        :param overrides: The overrides of this GetNetworkSwitchMtu200Response.
        :type overrides: List[GetNetworkSwitchMtu200ResponseOverridesInner]
        """

        self._overrides = overrides
