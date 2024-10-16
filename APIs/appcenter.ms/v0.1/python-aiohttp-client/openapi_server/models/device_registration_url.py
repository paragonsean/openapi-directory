# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class DeviceRegistrationUrl(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, registration_url: str=None):
        """DeviceRegistrationUrl - a model defined in OpenAPI

        :param registration_url: The registration_url of this DeviceRegistrationUrl.
        """
        self.openapi_types = {
            'registration_url': str
        }

        self.attribute_map = {
            'registration_url': 'registration_url'
        }

        self._registration_url = registration_url

    @classmethod
    def from_dict(cls, dikt: dict) -> 'DeviceRegistrationUrl':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The DeviceRegistrationUrl of this DeviceRegistrationUrl.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def registration_url(self):
        """Gets the registration_url of this DeviceRegistrationUrl.

        The url that can be navigated to in order to start the device registration process.

        :return: The registration_url of this DeviceRegistrationUrl.
        :rtype: str
        """
        return self._registration_url

    @registration_url.setter
    def registration_url(self, registration_url):
        """Sets the registration_url of this DeviceRegistrationUrl.

        The url that can be navigated to in order to start the device registration process.

        :param registration_url: The registration_url of this DeviceRegistrationUrl.
        :type registration_url: str
        """
        if registration_url is None:
            raise ValueError("Invalid value for `registration_url`, must not be `None`")

        self._registration_url = registration_url
