# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.managed_network_group import ManagedNetworkGroup
from openapi_server.models.managed_network_peering_policy import ManagedNetworkPeeringPolicy
from openapi_server import util


class ConnectivityCollection(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, groups: List[ManagedNetworkGroup]=None, peerings: List[ManagedNetworkPeeringPolicy]=None):
        """ConnectivityCollection - a model defined in OpenAPI

        :param groups: The groups of this ConnectivityCollection.
        :param peerings: The peerings of this ConnectivityCollection.
        """
        self.openapi_types = {
            'groups': List[ManagedNetworkGroup],
            'peerings': List[ManagedNetworkPeeringPolicy]
        }

        self.attribute_map = {
            'groups': 'groups',
            'peerings': 'peerings'
        }

        self._groups = groups
        self._peerings = peerings

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ConnectivityCollection':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ConnectivityCollection of this ConnectivityCollection.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def groups(self):
        """Gets the groups of this ConnectivityCollection.

        The collection of connectivity related Managed Network Groups within the Managed Network

        :return: The groups of this ConnectivityCollection.
        :rtype: List[ManagedNetworkGroup]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this ConnectivityCollection.

        The collection of connectivity related Managed Network Groups within the Managed Network

        :param groups: The groups of this ConnectivityCollection.
        :type groups: List[ManagedNetworkGroup]
        """

        self._groups = groups

    @property
    def peerings(self):
        """Gets the peerings of this ConnectivityCollection.

        The collection of Managed Network Peering Policies within the Managed Network

        :return: The peerings of this ConnectivityCollection.
        :rtype: List[ManagedNetworkPeeringPolicy]
        """
        return self._peerings

    @peerings.setter
    def peerings(self, peerings):
        """Sets the peerings of this ConnectivityCollection.

        The collection of Managed Network Peering Policies within the Managed Network

        :param peerings: The peerings of this ConnectivityCollection.
        :type peerings: List[ManagedNetworkPeeringPolicy]
        """

        self._peerings = peerings
