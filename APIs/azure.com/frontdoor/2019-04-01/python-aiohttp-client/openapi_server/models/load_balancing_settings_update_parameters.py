# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class LoadBalancingSettingsUpdateParameters(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, additional_latency_milliseconds: int=None, sample_size: int=None, successful_samples_required: int=None):
        """LoadBalancingSettingsUpdateParameters - a model defined in OpenAPI

        :param additional_latency_milliseconds: The additional_latency_milliseconds of this LoadBalancingSettingsUpdateParameters.
        :param sample_size: The sample_size of this LoadBalancingSettingsUpdateParameters.
        :param successful_samples_required: The successful_samples_required of this LoadBalancingSettingsUpdateParameters.
        """
        self.openapi_types = {
            'additional_latency_milliseconds': int,
            'sample_size': int,
            'successful_samples_required': int
        }

        self.attribute_map = {
            'additional_latency_milliseconds': 'additionalLatencyMilliseconds',
            'sample_size': 'sampleSize',
            'successful_samples_required': 'successfulSamplesRequired'
        }

        self._additional_latency_milliseconds = additional_latency_milliseconds
        self._sample_size = sample_size
        self._successful_samples_required = successful_samples_required

    @classmethod
    def from_dict(cls, dikt: dict) -> 'LoadBalancingSettingsUpdateParameters':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The LoadBalancingSettingsUpdateParameters of this LoadBalancingSettingsUpdateParameters.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def additional_latency_milliseconds(self):
        """Gets the additional_latency_milliseconds of this LoadBalancingSettingsUpdateParameters.

        The additional latency in milliseconds for probes to fall into the lowest latency bucket

        :return: The additional_latency_milliseconds of this LoadBalancingSettingsUpdateParameters.
        :rtype: int
        """
        return self._additional_latency_milliseconds

    @additional_latency_milliseconds.setter
    def additional_latency_milliseconds(self, additional_latency_milliseconds):
        """Sets the additional_latency_milliseconds of this LoadBalancingSettingsUpdateParameters.

        The additional latency in milliseconds for probes to fall into the lowest latency bucket

        :param additional_latency_milliseconds: The additional_latency_milliseconds of this LoadBalancingSettingsUpdateParameters.
        :type additional_latency_milliseconds: int
        """

        self._additional_latency_milliseconds = additional_latency_milliseconds

    @property
    def sample_size(self):
        """Gets the sample_size of this LoadBalancingSettingsUpdateParameters.

        The number of samples to consider for load balancing decisions

        :return: The sample_size of this LoadBalancingSettingsUpdateParameters.
        :rtype: int
        """
        return self._sample_size

    @sample_size.setter
    def sample_size(self, sample_size):
        """Sets the sample_size of this LoadBalancingSettingsUpdateParameters.

        The number of samples to consider for load balancing decisions

        :param sample_size: The sample_size of this LoadBalancingSettingsUpdateParameters.
        :type sample_size: int
        """

        self._sample_size = sample_size

    @property
    def successful_samples_required(self):
        """Gets the successful_samples_required of this LoadBalancingSettingsUpdateParameters.

        The number of samples within the sample period that must succeed

        :return: The successful_samples_required of this LoadBalancingSettingsUpdateParameters.
        :rtype: int
        """
        return self._successful_samples_required

    @successful_samples_required.setter
    def successful_samples_required(self, successful_samples_required):
        """Sets the successful_samples_required of this LoadBalancingSettingsUpdateParameters.

        The number of samples within the sample period that must succeed

        :param successful_samples_required: The successful_samples_required of this LoadBalancingSettingsUpdateParameters.
        :type successful_samples_required: int
        """

        self._successful_samples_required = successful_samples_required
