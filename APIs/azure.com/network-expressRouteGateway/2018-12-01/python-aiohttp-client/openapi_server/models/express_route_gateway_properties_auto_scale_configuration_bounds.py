# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, max: int=None, min: int=None):
        """ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds - a model defined in OpenAPI

        :param max: The max of this ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds.
        :param min: The min of this ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds.
        """
        self.openapi_types = {
            'max': int,
            'min': int
        }

        self.attribute_map = {
            'max': 'max',
            'min': 'min'
        }

        self._max = max
        self._min = min

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ExpressRouteGatewayProperties_autoScaleConfiguration_bounds of this ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def max(self):
        """Gets the max of this ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds.

        Maximum number of scale units deployed for ExpressRoute gateway.

        :return: The max of this ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds.
        :rtype: int
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds.

        Maximum number of scale units deployed for ExpressRoute gateway.

        :param max: The max of this ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds.
        :type max: int
        """

        self._max = max

    @property
    def min(self):
        """Gets the min of this ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds.

        Minimum number of scale units deployed for ExpressRoute gateway.

        :return: The min of this ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds.
        :rtype: int
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds.

        Minimum number of scale units deployed for ExpressRoute gateway.

        :param min: The min of this ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds.
        :type min: int
        """

        self._min = min
