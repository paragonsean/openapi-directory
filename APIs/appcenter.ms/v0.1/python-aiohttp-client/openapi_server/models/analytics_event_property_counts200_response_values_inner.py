# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class AnalyticsEventPropertyCounts200ResponseValuesInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, count: int=None, name: str=None, previous_count: int=None):
        """AnalyticsEventPropertyCounts200ResponseValuesInner - a model defined in OpenAPI

        :param count: The count of this AnalyticsEventPropertyCounts200ResponseValuesInner.
        :param name: The name of this AnalyticsEventPropertyCounts200ResponseValuesInner.
        :param previous_count: The previous_count of this AnalyticsEventPropertyCounts200ResponseValuesInner.
        """
        self.openapi_types = {
            'count': int,
            'name': str,
            'previous_count': int
        }

        self.attribute_map = {
            'count': 'count',
            'name': 'name',
            'previous_count': 'previous_count'
        }

        self._count = count
        self._name = name
        self._previous_count = previous_count

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AnalyticsEventPropertyCounts200ResponseValuesInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Analytics_EventPropertyCounts_200_response_values_inner of this AnalyticsEventPropertyCounts200ResponseValuesInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def count(self):
        """Gets the count of this AnalyticsEventPropertyCounts200ResponseValuesInner.

        The count of the the event property value.

        :return: The count of this AnalyticsEventPropertyCounts200ResponseValuesInner.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this AnalyticsEventPropertyCounts200ResponseValuesInner.

        The count of the the event property value.

        :param count: The count of this AnalyticsEventPropertyCounts200ResponseValuesInner.
        :type count: int
        """

        self._count = count

    @property
    def name(self):
        """Gets the name of this AnalyticsEventPropertyCounts200ResponseValuesInner.

        The event property value name.

        :return: The name of this AnalyticsEventPropertyCounts200ResponseValuesInner.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AnalyticsEventPropertyCounts200ResponseValuesInner.

        The event property value name.

        :param name: The name of this AnalyticsEventPropertyCounts200ResponseValuesInner.
        :type name: str
        """

        self._name = name

    @property
    def previous_count(self):
        """Gets the previous_count of this AnalyticsEventPropertyCounts200ResponseValuesInner.

        The count of previous time range of the event property value.

        :return: The previous_count of this AnalyticsEventPropertyCounts200ResponseValuesInner.
        :rtype: int
        """
        return self._previous_count

    @previous_count.setter
    def previous_count(self, previous_count):
        """Sets the previous_count of this AnalyticsEventPropertyCounts200ResponseValuesInner.

        The count of previous time range of the event property value.

        :param previous_count: The previous_count of this AnalyticsEventPropertyCounts200ResponseValuesInner.
        :type previous_count: int
        """

        self._previous_count = previous_count
