# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class LivenessProbeRequirements(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, failure_threshold: int=None, initial_delay_seconds: int=None, period_seconds: int=None, success_threshold: int=None, timeout_seconds: int=None):
        """LivenessProbeRequirements - a model defined in OpenAPI

        :param failure_threshold: The failure_threshold of this LivenessProbeRequirements.
        :param initial_delay_seconds: The initial_delay_seconds of this LivenessProbeRequirements.
        :param period_seconds: The period_seconds of this LivenessProbeRequirements.
        :param success_threshold: The success_threshold of this LivenessProbeRequirements.
        :param timeout_seconds: The timeout_seconds of this LivenessProbeRequirements.
        """
        self.openapi_types = {
            'failure_threshold': int,
            'initial_delay_seconds': int,
            'period_seconds': int,
            'success_threshold': int,
            'timeout_seconds': int
        }

        self.attribute_map = {
            'failure_threshold': 'failureThreshold',
            'initial_delay_seconds': 'initialDelaySeconds',
            'period_seconds': 'periodSeconds',
            'success_threshold': 'successThreshold',
            'timeout_seconds': 'timeoutSeconds'
        }

        self._failure_threshold = failure_threshold
        self._initial_delay_seconds = initial_delay_seconds
        self._period_seconds = period_seconds
        self._success_threshold = success_threshold
        self._timeout_seconds = timeout_seconds

    @classmethod
    def from_dict(cls, dikt: dict) -> 'LivenessProbeRequirements':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The LivenessProbeRequirements of this LivenessProbeRequirements.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def failure_threshold(self):
        """Gets the failure_threshold of this LivenessProbeRequirements.

        The number of failures to allow before returning an unhealthy status.

        :return: The failure_threshold of this LivenessProbeRequirements.
        :rtype: int
        """
        return self._failure_threshold

    @failure_threshold.setter
    def failure_threshold(self, failure_threshold):
        """Sets the failure_threshold of this LivenessProbeRequirements.

        The number of failures to allow before returning an unhealthy status.

        :param failure_threshold: The failure_threshold of this LivenessProbeRequirements.
        :type failure_threshold: int
        """

        self._failure_threshold = failure_threshold

    @property
    def initial_delay_seconds(self):
        """Gets the initial_delay_seconds of this LivenessProbeRequirements.

        The delay before the first probe in seconds.

        :return: The initial_delay_seconds of this LivenessProbeRequirements.
        :rtype: int
        """
        return self._initial_delay_seconds

    @initial_delay_seconds.setter
    def initial_delay_seconds(self, initial_delay_seconds):
        """Sets the initial_delay_seconds of this LivenessProbeRequirements.

        The delay before the first probe in seconds.

        :param initial_delay_seconds: The initial_delay_seconds of this LivenessProbeRequirements.
        :type initial_delay_seconds: int
        """

        self._initial_delay_seconds = initial_delay_seconds

    @property
    def period_seconds(self):
        """Gets the period_seconds of this LivenessProbeRequirements.

        The length of time between probes in seconds.

        :return: The period_seconds of this LivenessProbeRequirements.
        :rtype: int
        """
        return self._period_seconds

    @period_seconds.setter
    def period_seconds(self, period_seconds):
        """Sets the period_seconds of this LivenessProbeRequirements.

        The length of time between probes in seconds.

        :param period_seconds: The period_seconds of this LivenessProbeRequirements.
        :type period_seconds: int
        """

        self._period_seconds = period_seconds

    @property
    def success_threshold(self):
        """Gets the success_threshold of this LivenessProbeRequirements.

        The number of successful probes before returning a healthy status.

        :return: The success_threshold of this LivenessProbeRequirements.
        :rtype: int
        """
        return self._success_threshold

    @success_threshold.setter
    def success_threshold(self, success_threshold):
        """Sets the success_threshold of this LivenessProbeRequirements.

        The number of successful probes before returning a healthy status.

        :param success_threshold: The success_threshold of this LivenessProbeRequirements.
        :type success_threshold: int
        """

        self._success_threshold = success_threshold

    @property
    def timeout_seconds(self):
        """Gets the timeout_seconds of this LivenessProbeRequirements.

        The probe timeout in seconds.

        :return: The timeout_seconds of this LivenessProbeRequirements.
        :rtype: int
        """
        return self._timeout_seconds

    @timeout_seconds.setter
    def timeout_seconds(self, timeout_seconds):
        """Sets the timeout_seconds of this LivenessProbeRequirements.

        The probe timeout in seconds.

        :param timeout_seconds: The timeout_seconds of this LivenessProbeRequirements.
        :type timeout_seconds: int
        """

        self._timeout_seconds = timeout_seconds
