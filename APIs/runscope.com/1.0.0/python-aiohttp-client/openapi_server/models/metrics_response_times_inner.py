# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class MetricsResponseTimesInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, avg_response_time_ms: int=None, success_ratio: int=None, timestamp: int=None):
        """MetricsResponseTimesInner - a model defined in OpenAPI

        :param avg_response_time_ms: The avg_response_time_ms of this MetricsResponseTimesInner.
        :param success_ratio: The success_ratio of this MetricsResponseTimesInner.
        :param timestamp: The timestamp of this MetricsResponseTimesInner.
        """
        self.openapi_types = {
            'avg_response_time_ms': int,
            'success_ratio': int,
            'timestamp': int
        }

        self.attribute_map = {
            'avg_response_time_ms': 'avg_response_time_ms',
            'success_ratio': 'success_ratio',
            'timestamp': 'timestamp'
        }

        self._avg_response_time_ms = avg_response_time_ms
        self._success_ratio = success_ratio
        self._timestamp = timestamp

    @classmethod
    def from_dict(cls, dikt: dict) -> 'MetricsResponseTimesInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Metrics_response_times_inner of this MetricsResponseTimesInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def avg_response_time_ms(self):
        """Gets the avg_response_time_ms of this MetricsResponseTimesInner.

        The average response time in miliseconds for all the requests for this test in this time interval.

        :return: The avg_response_time_ms of this MetricsResponseTimesInner.
        :rtype: int
        """
        return self._avg_response_time_ms

    @avg_response_time_ms.setter
    def avg_response_time_ms(self, avg_response_time_ms):
        """Sets the avg_response_time_ms of this MetricsResponseTimesInner.

        The average response time in miliseconds for all the requests for this test in this time interval.

        :param avg_response_time_ms: The avg_response_time_ms of this MetricsResponseTimesInner.
        :type avg_response_time_ms: int
        """

        self._avg_response_time_ms = avg_response_time_ms

    @property
    def success_ratio(self):
        """Gets the success_ratio of this MetricsResponseTimesInner.

        1 if there's a successful request in this time interval, or 0 if there isn't.

        :return: The success_ratio of this MetricsResponseTimesInner.
        :rtype: int
        """
        return self._success_ratio

    @success_ratio.setter
    def success_ratio(self, success_ratio):
        """Sets the success_ratio of this MetricsResponseTimesInner.

        1 if there's a successful request in this time interval, or 0 if there isn't.

        :param success_ratio: The success_ratio of this MetricsResponseTimesInner.
        :type success_ratio: int
        """

        self._success_ratio = success_ratio

    @property
    def timestamp(self):
        """Gets the timestamp of this MetricsResponseTimesInner.

        The timestamp in Unix format for the specified timeframe.

        :return: The timestamp of this MetricsResponseTimesInner.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this MetricsResponseTimesInner.

        The timestamp in Unix format for the specified timeframe.

        :param timestamp: The timestamp of this MetricsResponseTimesInner.
        :type timestamp: int
        """

        self._timestamp = timestamp
