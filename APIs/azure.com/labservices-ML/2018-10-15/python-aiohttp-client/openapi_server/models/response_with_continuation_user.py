# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.user import User
from openapi_server import util


class ResponseWithContinuationUser(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, next_link: str=None, value: List[User]=None):
        """ResponseWithContinuationUser - a model defined in OpenAPI

        :param next_link: The next_link of this ResponseWithContinuationUser.
        :param value: The value of this ResponseWithContinuationUser.
        """
        self.openapi_types = {
            'next_link': str,
            'value': List[User]
        }

        self.attribute_map = {
            'next_link': 'nextLink',
            'value': 'value'
        }

        self._next_link = next_link
        self._value = value

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ResponseWithContinuationUser':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ResponseWithContinuation[User] of this ResponseWithContinuationUser.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def next_link(self):
        """Gets the next_link of this ResponseWithContinuationUser.

        Link for next set of results.

        :return: The next_link of this ResponseWithContinuationUser.
        :rtype: str
        """
        return self._next_link

    @next_link.setter
    def next_link(self, next_link):
        """Sets the next_link of this ResponseWithContinuationUser.

        Link for next set of results.

        :param next_link: The next_link of this ResponseWithContinuationUser.
        :type next_link: str
        """

        self._next_link = next_link

    @property
    def value(self):
        """Gets the value of this ResponseWithContinuationUser.

        Results of the list operation.

        :return: The value of this ResponseWithContinuationUser.
        :rtype: List[User]
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ResponseWithContinuationUser.

        Results of the list operation.

        :param value: The value of this ResponseWithContinuationUser.
        :type value: List[User]
        """

        self._value = value
