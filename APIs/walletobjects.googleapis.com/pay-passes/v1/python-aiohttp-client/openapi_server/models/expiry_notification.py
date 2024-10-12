# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ExpiryNotification(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, enable_notification: bool=None):
        """ExpiryNotification - a model defined in OpenAPI

        :param enable_notification: The enable_notification of this ExpiryNotification.
        """
        self.openapi_types = {
            'enable_notification': bool
        }

        self.attribute_map = {
            'enable_notification': 'enableNotification'
        }

        self._enable_notification = enable_notification

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ExpiryNotification':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ExpiryNotification of this ExpiryNotification.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def enable_notification(self):
        """Gets the enable_notification of this ExpiryNotification.

        Indicates if the object needs to have expiry notification enabled.

        :return: The enable_notification of this ExpiryNotification.
        :rtype: bool
        """
        return self._enable_notification

    @enable_notification.setter
    def enable_notification(self, enable_notification):
        """Sets the enable_notification of this ExpiryNotification.

        Indicates if the object needs to have expiry notification enabled.

        :param enable_notification: The enable_notification of this ExpiryNotification.
        :type enable_notification: bool
        """

        self._enable_notification = enable_notification
