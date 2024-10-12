# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.notification_recipient_user_list_by_notification200_response_value_inner import NotificationRecipientUserListByNotification200ResponseValueInner
from openapi_server import util


class NotificationRecipientUserListByNotification200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, next_link: str=None, value: List[NotificationRecipientUserListByNotification200ResponseValueInner]=None):
        """NotificationRecipientUserListByNotification200Response - a model defined in OpenAPI

        :param next_link: The next_link of this NotificationRecipientUserListByNotification200Response.
        :param value: The value of this NotificationRecipientUserListByNotification200Response.
        """
        self.openapi_types = {
            'next_link': str,
            'value': List[NotificationRecipientUserListByNotification200ResponseValueInner]
        }

        self.attribute_map = {
            'next_link': 'nextLink',
            'value': 'value'
        }

        self._next_link = next_link
        self._value = value

    @classmethod
    def from_dict(cls, dikt: dict) -> 'NotificationRecipientUserListByNotification200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The NotificationRecipientUser_ListByNotification_200_response of this NotificationRecipientUserListByNotification200Response.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def next_link(self):
        """Gets the next_link of this NotificationRecipientUserListByNotification200Response.

        Next page link if any.

        :return: The next_link of this NotificationRecipientUserListByNotification200Response.
        :rtype: str
        """
        return self._next_link

    @next_link.setter
    def next_link(self, next_link):
        """Sets the next_link of this NotificationRecipientUserListByNotification200Response.

        Next page link if any.

        :param next_link: The next_link of this NotificationRecipientUserListByNotification200Response.
        :type next_link: str
        """

        self._next_link = next_link

    @property
    def value(self):
        """Gets the value of this NotificationRecipientUserListByNotification200Response.

        Page values.

        :return: The value of this NotificationRecipientUserListByNotification200Response.
        :rtype: List[NotificationRecipientUserListByNotification200ResponseValueInner]
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this NotificationRecipientUserListByNotification200Response.

        Page values.

        :param value: The value of this NotificationRecipientUserListByNotification200Response.
        :type value: List[NotificationRecipientUserListByNotification200ResponseValueInner]
        """

        self._value = value
