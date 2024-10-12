# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class DevicePatchProperties(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, device_description: str=None):
        """DevicePatchProperties - a model defined in OpenAPI

        :param device_description: The device_description of this DevicePatchProperties.
        """
        self.openapi_types = {
            'device_description': str
        }

        self.attribute_map = {
            'device_description': 'deviceDescription'
        }

        self._device_description = device_description

    @classmethod
    def from_dict(cls, dikt: dict) -> 'DevicePatchProperties':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The DevicePatchProperties of this DevicePatchProperties.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def device_description(self):
        """Gets the device_description of this DevicePatchProperties.

        Short description given for the device

        :return: The device_description of this DevicePatchProperties.
        :rtype: str
        """
        return self._device_description

    @device_description.setter
    def device_description(self, device_description):
        """Sets the device_description of this DevicePatchProperties.

        Short description given for the device

        :param device_description: The device_description of this DevicePatchProperties.
        :type device_description: str
        """

        self._device_description = device_description
