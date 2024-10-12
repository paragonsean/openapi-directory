# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class HealthProbeSettingsUpdateParameters(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, interval_in_seconds: int=None, path: str=None, protocol: str=None):
        """HealthProbeSettingsUpdateParameters - a model defined in OpenAPI

        :param interval_in_seconds: The interval_in_seconds of this HealthProbeSettingsUpdateParameters.
        :param path: The path of this HealthProbeSettingsUpdateParameters.
        :param protocol: The protocol of this HealthProbeSettingsUpdateParameters.
        """
        self.openapi_types = {
            'interval_in_seconds': int,
            'path': str,
            'protocol': str
        }

        self.attribute_map = {
            'interval_in_seconds': 'intervalInSeconds',
            'path': 'path',
            'protocol': 'protocol'
        }

        self._interval_in_seconds = interval_in_seconds
        self._path = path
        self._protocol = protocol

    @classmethod
    def from_dict(cls, dikt: dict) -> 'HealthProbeSettingsUpdateParameters':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The HealthProbeSettingsUpdateParameters of this HealthProbeSettingsUpdateParameters.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def interval_in_seconds(self):
        """Gets the interval_in_seconds of this HealthProbeSettingsUpdateParameters.

        The number of seconds between health probes.

        :return: The interval_in_seconds of this HealthProbeSettingsUpdateParameters.
        :rtype: int
        """
        return self._interval_in_seconds

    @interval_in_seconds.setter
    def interval_in_seconds(self, interval_in_seconds):
        """Sets the interval_in_seconds of this HealthProbeSettingsUpdateParameters.

        The number of seconds between health probes.

        :param interval_in_seconds: The interval_in_seconds of this HealthProbeSettingsUpdateParameters.
        :type interval_in_seconds: int
        """

        self._interval_in_seconds = interval_in_seconds

    @property
    def path(self):
        """Gets the path of this HealthProbeSettingsUpdateParameters.

        The path to use for the health probe. Default is /

        :return: The path of this HealthProbeSettingsUpdateParameters.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this HealthProbeSettingsUpdateParameters.

        The path to use for the health probe. Default is /

        :param path: The path of this HealthProbeSettingsUpdateParameters.
        :type path: str
        """

        self._path = path

    @property
    def protocol(self):
        """Gets the protocol of this HealthProbeSettingsUpdateParameters.

        Protocol scheme to use for this probe

        :return: The protocol of this HealthProbeSettingsUpdateParameters.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this HealthProbeSettingsUpdateParameters.

        Protocol scheme to use for this probe

        :param protocol: The protocol of this HealthProbeSettingsUpdateParameters.
        :type protocol: str
        """
        allowed_values = ["Http", "Https"]  # noqa: E501
        if protocol not in allowed_values:
            raise ValueError(
                "Invalid value for `protocol` ({0}), must be one of {1}"
                .format(protocol, allowed_values)
            )

        self._protocol = protocol
