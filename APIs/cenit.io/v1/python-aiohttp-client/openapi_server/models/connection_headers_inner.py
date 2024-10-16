# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ConnectionHeadersInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, key: str=None, value: str=None):
        """ConnectionHeadersInner - a model defined in OpenAPI

        :param key: The key of this ConnectionHeadersInner.
        :param value: The value of this ConnectionHeadersInner.
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
    def from_dict(cls, dikt: dict) -> 'ConnectionHeadersInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The connection_headers_inner of this ConnectionHeadersInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def key(self):
        """Gets the key of this ConnectionHeadersInner.


        :return: The key of this ConnectionHeadersInner.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this ConnectionHeadersInner.


        :param key: The key of this ConnectionHeadersInner.
        :type key: str
        """

        self._key = key

    @property
    def value(self):
        """Gets the value of this ConnectionHeadersInner.


        :return: The value of this ConnectionHeadersInner.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ConnectionHeadersInner.


        :param value: The value of this ConnectionHeadersInner.
        :type value: str
        """

        self._value = value
