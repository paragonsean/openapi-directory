# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.analytics_operating_system_counts200_response_oses_inner import AnalyticsOperatingSystemCounts200ResponseOsesInner
from openapi_server import util


class OSes(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, oses: List[AnalyticsOperatingSystemCounts200ResponseOsesInner]=None, total: int=None):
        """OSes - a model defined in OpenAPI

        :param oses: The oses of this OSes.
        :param total: The total of this OSes.
        """
        self.openapi_types = {
            'oses': List[AnalyticsOperatingSystemCounts200ResponseOsesInner],
            'total': int
        }

        self.attribute_map = {
            'oses': 'oses',
            'total': 'total'
        }

        self._oses = oses
        self._total = total

    @classmethod
    def from_dict(cls, dikt: dict) -> 'OSes':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The OSes of this OSes.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def oses(self):
        """Gets the oses of this OSes.


        :return: The oses of this OSes.
        :rtype: List[AnalyticsOperatingSystemCounts200ResponseOsesInner]
        """
        return self._oses

    @oses.setter
    def oses(self, oses):
        """Sets the oses of this OSes.


        :param oses: The oses of this OSes.
        :type oses: List[AnalyticsOperatingSystemCounts200ResponseOsesInner]
        """

        self._oses = oses

    @property
    def total(self):
        """Gets the total of this OSes.


        :return: The total of this OSes.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this OSes.


        :param total: The total of this OSes.
        :type total: int
        """

        self._total = total
