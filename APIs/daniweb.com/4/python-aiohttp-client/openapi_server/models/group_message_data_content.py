# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class GroupMessageDataContent(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, key: str=None, value: str=None):
        """GroupMessageDataContent - a model defined in OpenAPI

        :param key: The key of this GroupMessageDataContent.
        :param value: The value of this GroupMessageDataContent.
        """
        self.openapi_types = {
            'key': str,
            'value': str
        }

        self.attribute_map = {
            'key': 'key',
            'value': 'value'
        }

        self._key = key
        self._value = value

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GroupMessageDataContent':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Group_message_data_content of this GroupMessageDataContent.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def key(self):
        """Gets the key of this GroupMessageDataContent.


        :return: The key of this GroupMessageDataContent.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this GroupMessageDataContent.


        :param key: The key of this GroupMessageDataContent.
        :type key: str
        """

        self._key = key

    @property
    def value(self):
        """Gets the value of this GroupMessageDataContent.


        :return: The value of this GroupMessageDataContent.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this GroupMessageDataContent.


        :param value: The value of this GroupMessageDataContent.
        :type value: str
        """

        self._value = value
