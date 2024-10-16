# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class CreateNetworkFloorPlanRequestBottomRightCorner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, lat: float=None, lng: float=None):
        """CreateNetworkFloorPlanRequestBottomRightCorner - a model defined in OpenAPI

        :param lat: The lat of this CreateNetworkFloorPlanRequestBottomRightCorner.
        :param lng: The lng of this CreateNetworkFloorPlanRequestBottomRightCorner.
        """
        self.openapi_types = {
            'lat': float,
            'lng': float
        }

        self.attribute_map = {
            'lat': 'lat',
            'lng': 'lng'
        }

        self._lat = lat
        self._lng = lng

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CreateNetworkFloorPlanRequestBottomRightCorner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The createNetworkFloorPlan_request_bottomRightCorner of this CreateNetworkFloorPlanRequestBottomRightCorner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def lat(self):
        """Gets the lat of this CreateNetworkFloorPlanRequestBottomRightCorner.

        Latitude

        :return: The lat of this CreateNetworkFloorPlanRequestBottomRightCorner.
        :rtype: float
        """
        return self._lat

    @lat.setter
    def lat(self, lat):
        """Sets the lat of this CreateNetworkFloorPlanRequestBottomRightCorner.

        Latitude

        :param lat: The lat of this CreateNetworkFloorPlanRequestBottomRightCorner.
        :type lat: float
        """

        self._lat = lat

    @property
    def lng(self):
        """Gets the lng of this CreateNetworkFloorPlanRequestBottomRightCorner.

        Longitude

        :return: The lng of this CreateNetworkFloorPlanRequestBottomRightCorner.
        :rtype: float
        """
        return self._lng

    @lng.setter
    def lng(self, lng):
        """Sets the lng of this CreateNetworkFloorPlanRequestBottomRightCorner.

        Longitude

        :param lng: The lng of this CreateNetworkFloorPlanRequestBottomRightCorner.
        :type lng: float
        """

        self._lng = lng
