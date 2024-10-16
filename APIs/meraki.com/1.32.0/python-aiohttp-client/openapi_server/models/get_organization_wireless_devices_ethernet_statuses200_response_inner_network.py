# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerNetwork(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id: str=None):
        """GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerNetwork - a model defined in OpenAPI

        :param id: The id of this GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerNetwork.
        """
        self.openapi_types = {
            'id': str
        }

        self.attribute_map = {
            'id': 'id'
        }

        self._id = id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerNetwork':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The getOrganizationWirelessDevicesEthernetStatuses_200_response_inner_network of this GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerNetwork.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerNetwork.

        The network ID the AP is associated to

        :return: The id of this GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerNetwork.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerNetwork.

        The network ID the AP is associated to

        :param id: The id of this GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerNetwork.
        :type id: str
        """

        self._id = id
