# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigLimits(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, max_disk_size_in_mb: int=None, max_memory_in_mb: int=None, max_percentage_cpu: float=None):
        """AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigLimits - a model defined in OpenAPI

        :param max_disk_size_in_mb: The max_disk_size_in_mb of this AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigLimits.
        :param max_memory_in_mb: The max_memory_in_mb of this AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigLimits.
        :param max_percentage_cpu: The max_percentage_cpu of this AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigLimits.
        """
        self.openapi_types = {
            'max_disk_size_in_mb': int,
            'max_memory_in_mb': int,
            'max_percentage_cpu': float
        }

        self.attribute_map = {
            'max_disk_size_in_mb': 'maxDiskSizeInMb',
            'max_memory_in_mb': 'maxMemoryInMb',
            'max_percentage_cpu': 'maxPercentageCpu'
        }

        self._max_disk_size_in_mb = max_disk_size_in_mb
        self._max_memory_in_mb = max_memory_in_mb
        self._max_percentage_cpu = max_percentage_cpu

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigLimits':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The AppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_limits of this AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigLimits.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def max_disk_size_in_mb(self):
        """Gets the max_disk_size_in_mb of this AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigLimits.

        Maximum allowed disk size usage in MB.

        :return: The max_disk_size_in_mb of this AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigLimits.
        :rtype: int
        """
        return self._max_disk_size_in_mb

    @max_disk_size_in_mb.setter
    def max_disk_size_in_mb(self, max_disk_size_in_mb):
        """Sets the max_disk_size_in_mb of this AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigLimits.

        Maximum allowed disk size usage in MB.

        :param max_disk_size_in_mb: The max_disk_size_in_mb of this AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigLimits.
        :type max_disk_size_in_mb: int
        """

        self._max_disk_size_in_mb = max_disk_size_in_mb

    @property
    def max_memory_in_mb(self):
        """Gets the max_memory_in_mb of this AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigLimits.

        Maximum allowed memory usage in MB.

        :return: The max_memory_in_mb of this AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigLimits.
        :rtype: int
        """
        return self._max_memory_in_mb

    @max_memory_in_mb.setter
    def max_memory_in_mb(self, max_memory_in_mb):
        """Sets the max_memory_in_mb of this AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigLimits.

        Maximum allowed memory usage in MB.

        :param max_memory_in_mb: The max_memory_in_mb of this AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigLimits.
        :type max_memory_in_mb: int
        """

        self._max_memory_in_mb = max_memory_in_mb

    @property
    def max_percentage_cpu(self):
        """Gets the max_percentage_cpu of this AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigLimits.

        Maximum allowed CPU usage percentage.

        :return: The max_percentage_cpu of this AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigLimits.
        :rtype: float
        """
        return self._max_percentage_cpu

    @max_percentage_cpu.setter
    def max_percentage_cpu(self, max_percentage_cpu):
        """Sets the max_percentage_cpu of this AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigLimits.

        Maximum allowed CPU usage percentage.

        :param max_percentage_cpu: The max_percentage_cpu of this AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigLimits.
        :type max_percentage_cpu: float
        """

        self._max_percentage_cpu = max_percentage_cpu
