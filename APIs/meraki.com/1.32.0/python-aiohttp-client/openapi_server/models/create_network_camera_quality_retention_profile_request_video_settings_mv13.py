# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class CreateNetworkCameraQualityRetentionProfileRequestVideoSettingsMV13(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, quality: str=None, resolution: str=None):
        """CreateNetworkCameraQualityRetentionProfileRequestVideoSettingsMV13 - a model defined in OpenAPI

        :param quality: The quality of this CreateNetworkCameraQualityRetentionProfileRequestVideoSettingsMV13.
        :param resolution: The resolution of this CreateNetworkCameraQualityRetentionProfileRequestVideoSettingsMV13.
        """
        self.openapi_types = {
            'quality': str,
            'resolution': str
        }

        self.attribute_map = {
            'quality': 'quality',
            'resolution': 'resolution'
        }

        self._quality = quality
        self._resolution = resolution

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CreateNetworkCameraQualityRetentionProfileRequestVideoSettingsMV13':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The createNetworkCameraQualityRetentionProfile_request_videoSettings_MV13 of this CreateNetworkCameraQualityRetentionProfileRequestVideoSettingsMV13.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def quality(self):
        """Gets the quality of this CreateNetworkCameraQualityRetentionProfileRequestVideoSettingsMV13.

        Quality of the camera. Can be one of 'Standard', 'Enhanced' or 'High'.

        :return: The quality of this CreateNetworkCameraQualityRetentionProfileRequestVideoSettingsMV13.
        :rtype: str
        """
        return self._quality

    @quality.setter
    def quality(self, quality):
        """Sets the quality of this CreateNetworkCameraQualityRetentionProfileRequestVideoSettingsMV13.

        Quality of the camera. Can be one of 'Standard', 'Enhanced' or 'High'.

        :param quality: The quality of this CreateNetworkCameraQualityRetentionProfileRequestVideoSettingsMV13.
        :type quality: str
        """
        allowed_values = ["Enhanced", "High", "Standard"]  # noqa: E501
        if quality not in allowed_values:
            raise ValueError(
                "Invalid value for `quality` ({0}), must be one of {1}"
                .format(quality, allowed_values)
            )

        self._quality = quality

    @property
    def resolution(self):
        """Gets the resolution of this CreateNetworkCameraQualityRetentionProfileRequestVideoSettingsMV13.

        Resolution of the camera. Can be one of '1080x1080' or '2688x1512'.

        :return: The resolution of this CreateNetworkCameraQualityRetentionProfileRequestVideoSettingsMV13.
        :rtype: str
        """
        return self._resolution

    @resolution.setter
    def resolution(self, resolution):
        """Sets the resolution of this CreateNetworkCameraQualityRetentionProfileRequestVideoSettingsMV13.

        Resolution of the camera. Can be one of '1080x1080' or '2688x1512'.

        :param resolution: The resolution of this CreateNetworkCameraQualityRetentionProfileRequestVideoSettingsMV13.
        :type resolution: str
        """
        allowed_values = ["1080x1080", "2688x1512"]  # noqa: E501
        if resolution not in allowed_values:
            raise ValueError(
                "Invalid value for `resolution` ({0}), must be one of {1}"
                .format(resolution, allowed_values)
            )

        self._resolution = resolution
