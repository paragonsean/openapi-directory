# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class UpdateNetworkApplianceTrafficShapingCustomPerformanceClassRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, max_jitter: int=None, max_latency: int=None, max_loss_percentage: int=None, name: str=None):
        """UpdateNetworkApplianceTrafficShapingCustomPerformanceClassRequest - a model defined in OpenAPI

        :param max_jitter: The max_jitter of this UpdateNetworkApplianceTrafficShapingCustomPerformanceClassRequest.
        :param max_latency: The max_latency of this UpdateNetworkApplianceTrafficShapingCustomPerformanceClassRequest.
        :param max_loss_percentage: The max_loss_percentage of this UpdateNetworkApplianceTrafficShapingCustomPerformanceClassRequest.
        :param name: The name of this UpdateNetworkApplianceTrafficShapingCustomPerformanceClassRequest.
        """
        self.openapi_types = {
            'max_jitter': int,
            'max_latency': int,
            'max_loss_percentage': int,
            'name': str
        }

        self.attribute_map = {
            'max_jitter': 'maxJitter',
            'max_latency': 'maxLatency',
            'max_loss_percentage': 'maxLossPercentage',
            'name': 'name'
        }

        self._max_jitter = max_jitter
        self._max_latency = max_latency
        self._max_loss_percentage = max_loss_percentage
        self._name = name

    @classmethod
    def from_dict(cls, dikt: dict) -> 'UpdateNetworkApplianceTrafficShapingCustomPerformanceClassRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The updateNetworkApplianceTrafficShapingCustomPerformanceClass_request of this UpdateNetworkApplianceTrafficShapingCustomPerformanceClassRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def max_jitter(self):
        """Gets the max_jitter of this UpdateNetworkApplianceTrafficShapingCustomPerformanceClassRequest.

        Maximum jitter in milliseconds

        :return: The max_jitter of this UpdateNetworkApplianceTrafficShapingCustomPerformanceClassRequest.
        :rtype: int
        """
        return self._max_jitter

    @max_jitter.setter
    def max_jitter(self, max_jitter):
        """Sets the max_jitter of this UpdateNetworkApplianceTrafficShapingCustomPerformanceClassRequest.

        Maximum jitter in milliseconds

        :param max_jitter: The max_jitter of this UpdateNetworkApplianceTrafficShapingCustomPerformanceClassRequest.
        :type max_jitter: int
        """

        self._max_jitter = max_jitter

    @property
    def max_latency(self):
        """Gets the max_latency of this UpdateNetworkApplianceTrafficShapingCustomPerformanceClassRequest.

        Maximum latency in milliseconds

        :return: The max_latency of this UpdateNetworkApplianceTrafficShapingCustomPerformanceClassRequest.
        :rtype: int
        """
        return self._max_latency

    @max_latency.setter
    def max_latency(self, max_latency):
        """Sets the max_latency of this UpdateNetworkApplianceTrafficShapingCustomPerformanceClassRequest.

        Maximum latency in milliseconds

        :param max_latency: The max_latency of this UpdateNetworkApplianceTrafficShapingCustomPerformanceClassRequest.
        :type max_latency: int
        """

        self._max_latency = max_latency

    @property
    def max_loss_percentage(self):
        """Gets the max_loss_percentage of this UpdateNetworkApplianceTrafficShapingCustomPerformanceClassRequest.

        Maximum percentage of packet loss

        :return: The max_loss_percentage of this UpdateNetworkApplianceTrafficShapingCustomPerformanceClassRequest.
        :rtype: int
        """
        return self._max_loss_percentage

    @max_loss_percentage.setter
    def max_loss_percentage(self, max_loss_percentage):
        """Sets the max_loss_percentage of this UpdateNetworkApplianceTrafficShapingCustomPerformanceClassRequest.

        Maximum percentage of packet loss

        :param max_loss_percentage: The max_loss_percentage of this UpdateNetworkApplianceTrafficShapingCustomPerformanceClassRequest.
        :type max_loss_percentage: int
        """

        self._max_loss_percentage = max_loss_percentage

    @property
    def name(self):
        """Gets the name of this UpdateNetworkApplianceTrafficShapingCustomPerformanceClassRequest.

        Name of the custom performance class

        :return: The name of this UpdateNetworkApplianceTrafficShapingCustomPerformanceClassRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateNetworkApplianceTrafficShapingCustomPerformanceClassRequest.

        Name of the custom performance class

        :param name: The name of this UpdateNetworkApplianceTrafficShapingCustomPerformanceClassRequest.
        :type name: str
        """

        self._name = name
