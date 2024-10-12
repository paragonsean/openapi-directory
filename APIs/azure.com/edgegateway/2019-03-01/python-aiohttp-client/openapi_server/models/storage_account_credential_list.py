# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.storage_account_credential import StorageAccountCredential
from openapi_server import util


class StorageAccountCredentialList(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, next_link: str=None, value: List[StorageAccountCredential]=None):
        """StorageAccountCredentialList - a model defined in OpenAPI

        :param next_link: The next_link of this StorageAccountCredentialList.
        :param value: The value of this StorageAccountCredentialList.
        """
        self.openapi_types = {
            'next_link': str,
            'value': List[StorageAccountCredential]
        }

        self.attribute_map = {
            'next_link': 'nextLink',
            'value': 'value'
        }

        self._next_link = next_link
        self._value = value

    @classmethod
    def from_dict(cls, dikt: dict) -> 'StorageAccountCredentialList':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The StorageAccountCredentialList of this StorageAccountCredentialList.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def next_link(self):
        """Gets the next_link of this StorageAccountCredentialList.

        Link to the next set of results.

        :return: The next_link of this StorageAccountCredentialList.
        :rtype: str
        """
        return self._next_link

    @next_link.setter
    def next_link(self, next_link):
        """Sets the next_link of this StorageAccountCredentialList.

        Link to the next set of results.

        :param next_link: The next_link of this StorageAccountCredentialList.
        :type next_link: str
        """

        self._next_link = next_link

    @property
    def value(self):
        """Gets the value of this StorageAccountCredentialList.

        The value.

        :return: The value of this StorageAccountCredentialList.
        :rtype: List[StorageAccountCredential]
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this StorageAccountCredentialList.

        The value.

        :param value: The value of this StorageAccountCredentialList.
        :type value: List[StorageAccountCredential]
        """

        self._value = value
