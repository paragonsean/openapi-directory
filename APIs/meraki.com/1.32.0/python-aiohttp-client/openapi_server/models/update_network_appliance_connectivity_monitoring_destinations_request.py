# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.update_network_appliance_connectivity_monitoring_destinations_request_destinations_inner import UpdateNetworkApplianceConnectivityMonitoringDestinationsRequestDestinationsInner
from openapi_server import util


class UpdateNetworkApplianceConnectivityMonitoringDestinationsRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, destinations: List[UpdateNetworkApplianceConnectivityMonitoringDestinationsRequestDestinationsInner]=None):
        """UpdateNetworkApplianceConnectivityMonitoringDestinationsRequest - a model defined in OpenAPI

        :param destinations: The destinations of this UpdateNetworkApplianceConnectivityMonitoringDestinationsRequest.
        """
        self.openapi_types = {
            'destinations': List[UpdateNetworkApplianceConnectivityMonitoringDestinationsRequestDestinationsInner]
        }

        self.attribute_map = {
            'destinations': 'destinations'
        }

        self._destinations = destinations

    @classmethod
    def from_dict(cls, dikt: dict) -> 'UpdateNetworkApplianceConnectivityMonitoringDestinationsRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The updateNetworkApplianceConnectivityMonitoringDestinations_request of this UpdateNetworkApplianceConnectivityMonitoringDestinationsRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def destinations(self):
        """Gets the destinations of this UpdateNetworkApplianceConnectivityMonitoringDestinationsRequest.

        The list of connectivity monitoring destinations

        :return: The destinations of this UpdateNetworkApplianceConnectivityMonitoringDestinationsRequest.
        :rtype: List[UpdateNetworkApplianceConnectivityMonitoringDestinationsRequestDestinationsInner]
        """
        return self._destinations

    @destinations.setter
    def destinations(self, destinations):
        """Sets the destinations of this UpdateNetworkApplianceConnectivityMonitoringDestinationsRequest.

        The list of connectivity monitoring destinations

        :param destinations: The destinations of this UpdateNetworkApplianceConnectivityMonitoringDestinationsRequest.
        :type destinations: List[UpdateNetworkApplianceConnectivityMonitoringDestinationsRequestDestinationsInner]
        """

        self._destinations = destinations
