# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class NotificationGetDefaultResponseDetailsInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, code: str=None, message: str=None, target: str=None):
        """NotificationGetDefaultResponseDetailsInner - a model defined in OpenAPI

        :param code: The code of this NotificationGetDefaultResponseDetailsInner.
        :param message: The message of this NotificationGetDefaultResponseDetailsInner.
        :param target: The target of this NotificationGetDefaultResponseDetailsInner.
        """
        self.openapi_types = {
            'code': str,
            'message': str,
            'target': str
        }

        self.attribute_map = {
            'code': 'code',
            'message': 'message',
            'target': 'target'
        }

        self._code = code
        self._message = message
        self._target = target

    @classmethod
    def from_dict(cls, dikt: dict) -> 'NotificationGetDefaultResponseDetailsInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Notification_Get_default_response_details_inner of this NotificationGetDefaultResponseDetailsInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self):
        """Gets the code of this NotificationGetDefaultResponseDetailsInner.

        Property level error code.

        :return: The code of this NotificationGetDefaultResponseDetailsInner.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this NotificationGetDefaultResponseDetailsInner.

        Property level error code.

        :param code: The code of this NotificationGetDefaultResponseDetailsInner.
        :type code: str
        """

        self._code = code

    @property
    def message(self):
        """Gets the message of this NotificationGetDefaultResponseDetailsInner.

        Human-readable representation of property-level error.

        :return: The message of this NotificationGetDefaultResponseDetailsInner.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this NotificationGetDefaultResponseDetailsInner.

        Human-readable representation of property-level error.

        :param message: The message of this NotificationGetDefaultResponseDetailsInner.
        :type message: str
        """

        self._message = message

    @property
    def target(self):
        """Gets the target of this NotificationGetDefaultResponseDetailsInner.

        Property name.

        :return: The target of this NotificationGetDefaultResponseDetailsInner.
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this NotificationGetDefaultResponseDetailsInner.

        Property name.

        :param target: The target of this NotificationGetDefaultResponseDetailsInner.
        :type target: str
        """

        self._target = target
