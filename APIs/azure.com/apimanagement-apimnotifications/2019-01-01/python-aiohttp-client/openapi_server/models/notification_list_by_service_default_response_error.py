# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.notification_list_by_service_default_response_error_details_inner import NotificationListByServiceDefaultResponseErrorDetailsInner
from openapi_server import util


class NotificationListByServiceDefaultResponseError(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, code: str=None, details: List[NotificationListByServiceDefaultResponseErrorDetailsInner]=None, message: str=None):
        """NotificationListByServiceDefaultResponseError - a model defined in OpenAPI

        :param code: The code of this NotificationListByServiceDefaultResponseError.
        :param details: The details of this NotificationListByServiceDefaultResponseError.
        :param message: The message of this NotificationListByServiceDefaultResponseError.
        """
        self.openapi_types = {
            'code': str,
            'details': List[NotificationListByServiceDefaultResponseErrorDetailsInner],
            'message': str
        }

        self.attribute_map = {
            'code': 'code',
            'details': 'details',
            'message': 'message'
        }

        self._code = code
        self._details = details
        self._message = message

    @classmethod
    def from_dict(cls, dikt: dict) -> 'NotificationListByServiceDefaultResponseError':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Notification_ListByService_default_response_error of this NotificationListByServiceDefaultResponseError.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self):
        """Gets the code of this NotificationListByServiceDefaultResponseError.

        Service-defined error code. This code serves as a sub-status for the HTTP error code specified in the response.

        :return: The code of this NotificationListByServiceDefaultResponseError.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this NotificationListByServiceDefaultResponseError.

        Service-defined error code. This code serves as a sub-status for the HTTP error code specified in the response.

        :param code: The code of this NotificationListByServiceDefaultResponseError.
        :type code: str
        """

        self._code = code

    @property
    def details(self):
        """Gets the details of this NotificationListByServiceDefaultResponseError.

        The list of invalid fields send in request, in case of validation error.

        :return: The details of this NotificationListByServiceDefaultResponseError.
        :rtype: List[NotificationListByServiceDefaultResponseErrorDetailsInner]
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this NotificationListByServiceDefaultResponseError.

        The list of invalid fields send in request, in case of validation error.

        :param details: The details of this NotificationListByServiceDefaultResponseError.
        :type details: List[NotificationListByServiceDefaultResponseErrorDetailsInner]
        """

        self._details = details

    @property
    def message(self):
        """Gets the message of this NotificationListByServiceDefaultResponseError.

        Human-readable representation of the error.

        :return: The message of this NotificationListByServiceDefaultResponseError.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this NotificationListByServiceDefaultResponseError.

        Human-readable representation of the error.

        :param message: The message of this NotificationListByServiceDefaultResponseError.
        :type message: str
        """

        self._message = message
