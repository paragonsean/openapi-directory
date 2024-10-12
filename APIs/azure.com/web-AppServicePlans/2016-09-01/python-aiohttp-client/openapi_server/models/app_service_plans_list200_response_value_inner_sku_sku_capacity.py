# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class AppServicePlansList200ResponseValueInnerSkuSkuCapacity(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, default: int=None, maximum: int=None, minimum: int=None, scale_type: str=None):
        """AppServicePlansList200ResponseValueInnerSkuSkuCapacity - a model defined in OpenAPI

        :param default: The default of this AppServicePlansList200ResponseValueInnerSkuSkuCapacity.
        :param maximum: The maximum of this AppServicePlansList200ResponseValueInnerSkuSkuCapacity.
        :param minimum: The minimum of this AppServicePlansList200ResponseValueInnerSkuSkuCapacity.
        :param scale_type: The scale_type of this AppServicePlansList200ResponseValueInnerSkuSkuCapacity.
        """
        self.openapi_types = {
            'default': int,
            'maximum': int,
            'minimum': int,
            'scale_type': str
        }

        self.attribute_map = {
            'default': 'default',
            'maximum': 'maximum',
            'minimum': 'minimum',
            'scale_type': 'scaleType'
        }

        self._default = default
        self._maximum = maximum
        self._minimum = minimum
        self._scale_type = scale_type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AppServicePlansList200ResponseValueInnerSkuSkuCapacity':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The AppServicePlans_List_200_response_value_inner_sku_skuCapacity of this AppServicePlansList200ResponseValueInnerSkuSkuCapacity.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def default(self):
        """Gets the default of this AppServicePlansList200ResponseValueInnerSkuSkuCapacity.

        Default number of workers for this App Service plan SKU.

        :return: The default of this AppServicePlansList200ResponseValueInnerSkuSkuCapacity.
        :rtype: int
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this AppServicePlansList200ResponseValueInnerSkuSkuCapacity.

        Default number of workers for this App Service plan SKU.

        :param default: The default of this AppServicePlansList200ResponseValueInnerSkuSkuCapacity.
        :type default: int
        """

        self._default = default

    @property
    def maximum(self):
        """Gets the maximum of this AppServicePlansList200ResponseValueInnerSkuSkuCapacity.

        Maximum number of workers for this App Service plan SKU.

        :return: The maximum of this AppServicePlansList200ResponseValueInnerSkuSkuCapacity.
        :rtype: int
        """
        return self._maximum

    @maximum.setter
    def maximum(self, maximum):
        """Sets the maximum of this AppServicePlansList200ResponseValueInnerSkuSkuCapacity.

        Maximum number of workers for this App Service plan SKU.

        :param maximum: The maximum of this AppServicePlansList200ResponseValueInnerSkuSkuCapacity.
        :type maximum: int
        """

        self._maximum = maximum

    @property
    def minimum(self):
        """Gets the minimum of this AppServicePlansList200ResponseValueInnerSkuSkuCapacity.

        Minimum number of workers for this App Service plan SKU.

        :return: The minimum of this AppServicePlansList200ResponseValueInnerSkuSkuCapacity.
        :rtype: int
        """
        return self._minimum

    @minimum.setter
    def minimum(self, minimum):
        """Sets the minimum of this AppServicePlansList200ResponseValueInnerSkuSkuCapacity.

        Minimum number of workers for this App Service plan SKU.

        :param minimum: The minimum of this AppServicePlansList200ResponseValueInnerSkuSkuCapacity.
        :type minimum: int
        """

        self._minimum = minimum

    @property
    def scale_type(self):
        """Gets the scale_type of this AppServicePlansList200ResponseValueInnerSkuSkuCapacity.

        Available scale configurations for an App Service plan.

        :return: The scale_type of this AppServicePlansList200ResponseValueInnerSkuSkuCapacity.
        :rtype: str
        """
        return self._scale_type

    @scale_type.setter
    def scale_type(self, scale_type):
        """Sets the scale_type of this AppServicePlansList200ResponseValueInnerSkuSkuCapacity.

        Available scale configurations for an App Service plan.

        :param scale_type: The scale_type of this AppServicePlansList200ResponseValueInnerSkuSkuCapacity.
        :type scale_type: str
        """

        self._scale_type = scale_type
