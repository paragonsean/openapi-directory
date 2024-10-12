# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.notification_contract import NotificationContract
from openapi_server import util


class NotificationCollection(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, next_link: str=None, value: List[NotificationContract]=None):
        """NotificationCollection - a model defined in OpenAPI

        :param next_link: The next_link of this NotificationCollection.
        :param value: The value of this NotificationCollection.
        """
        self.openapi_types = {
            'next_link': str,
            'value': List[NotificationContract]
        }

        self.attribute_map = {
            'next_link': 'nextLink',
            'value': 'value'
        }

        self._next_link = next_link
        self._value = value

    @classmethod
    def from_dict(cls, dikt: dict) -> 'NotificationCollection':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The NotificationCollection of this NotificationCollection.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def next_link(self):
        """Gets the next_link of this NotificationCollection.

        Next page link if any.

        :return: The next_link of this NotificationCollection.
        :rtype: str
        """
        return self._next_link

    @next_link.setter
    def next_link(self, next_link):
        """Sets the next_link of this NotificationCollection.

        Next page link if any.

        :param next_link: The next_link of this NotificationCollection.
        :type next_link: str
        """

        self._next_link = next_link

    @property
    def value(self):
        """Gets the value of this NotificationCollection.

        Page values.

        :return: The value of this NotificationCollection.
        :rtype: List[NotificationContract]
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this NotificationCollection.

        Page values.

        :param value: The value of this NotificationCollection.
        :type value: List[NotificationContract]
        """

        self._value = value
