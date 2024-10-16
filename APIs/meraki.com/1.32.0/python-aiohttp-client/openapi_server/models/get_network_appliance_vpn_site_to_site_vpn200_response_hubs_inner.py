# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class GetNetworkApplianceVpnSiteToSiteVpn200ResponseHubsInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, hub_id: str=None, use_default_route: bool=None):
        """GetNetworkApplianceVpnSiteToSiteVpn200ResponseHubsInner - a model defined in OpenAPI

        :param hub_id: The hub_id of this GetNetworkApplianceVpnSiteToSiteVpn200ResponseHubsInner.
        :param use_default_route: The use_default_route of this GetNetworkApplianceVpnSiteToSiteVpn200ResponseHubsInner.
        """
        self.openapi_types = {
            'hub_id': str,
            'use_default_route': bool
        }

        self.attribute_map = {
            'hub_id': 'hubId',
            'use_default_route': 'useDefaultRoute'
        }

        self._hub_id = hub_id
        self._use_default_route = use_default_route

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GetNetworkApplianceVpnSiteToSiteVpn200ResponseHubsInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The getNetworkApplianceVpnSiteToSiteVpn_200_response_hubs_inner of this GetNetworkApplianceVpnSiteToSiteVpn200ResponseHubsInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def hub_id(self):
        """Gets the hub_id of this GetNetworkApplianceVpnSiteToSiteVpn200ResponseHubsInner.

        The network ID of the hub.

        :return: The hub_id of this GetNetworkApplianceVpnSiteToSiteVpn200ResponseHubsInner.
        :rtype: str
        """
        return self._hub_id

    @hub_id.setter
    def hub_id(self, hub_id):
        """Sets the hub_id of this GetNetworkApplianceVpnSiteToSiteVpn200ResponseHubsInner.

        The network ID of the hub.

        :param hub_id: The hub_id of this GetNetworkApplianceVpnSiteToSiteVpn200ResponseHubsInner.
        :type hub_id: str
        """

        self._hub_id = hub_id

    @property
    def use_default_route(self):
        """Gets the use_default_route of this GetNetworkApplianceVpnSiteToSiteVpn200ResponseHubsInner.

        Indicates whether default route traffic should be sent to this hub.

        :return: The use_default_route of this GetNetworkApplianceVpnSiteToSiteVpn200ResponseHubsInner.
        :rtype: bool
        """
        return self._use_default_route

    @use_default_route.setter
    def use_default_route(self, use_default_route):
        """Sets the use_default_route of this GetNetworkApplianceVpnSiteToSiteVpn200ResponseHubsInner.

        Indicates whether default route traffic should be sent to this hub.

        :param use_default_route: The use_default_route of this GetNetworkApplianceVpnSiteToSiteVpn200ResponseHubsInner.
        :type use_default_route: bool
        """

        self._use_default_route = use_default_route
