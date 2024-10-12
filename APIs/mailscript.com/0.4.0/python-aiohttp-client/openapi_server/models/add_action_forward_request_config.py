# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class AddActionForwardRequestConfig(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, forward: str=None, _from: str=None, key: str=None, type: str=None):
        """AddActionForwardRequestConfig - a model defined in OpenAPI

        :param forward: The forward of this AddActionForwardRequestConfig.
        :param _from: The _from of this AddActionForwardRequestConfig.
        :param key: The key of this AddActionForwardRequestConfig.
        :param type: The type of this AddActionForwardRequestConfig.
        """
        self.openapi_types = {
            'forward': str,
            '_from': str,
            'key': str,
            'type': str
        }

        self.attribute_map = {
            'forward': 'forward',
            '_from': 'from',
            'key': 'key',
            'type': 'type'
        }

        self._forward = forward
        self.__from = _from
        self._key = key
        self._type = type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AddActionForwardRequestConfig':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The AddActionForwardRequest_config of this AddActionForwardRequestConfig.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def forward(self):
        """Gets the forward of this AddActionForwardRequestConfig.


        :return: The forward of this AddActionForwardRequestConfig.
        :rtype: str
        """
        return self._forward

    @forward.setter
    def forward(self, forward):
        """Sets the forward of this AddActionForwardRequestConfig.


        :param forward: The forward of this AddActionForwardRequestConfig.
        :type forward: str
        """
        if forward is None:
            raise ValueError("Invalid value for `forward`, must not be `None`")

        self._forward = forward

    @property
    def _from(self):
        """Gets the _from of this AddActionForwardRequestConfig.


        :return: The _from of this AddActionForwardRequestConfig.
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this AddActionForwardRequestConfig.


        :param _from: The _from of this AddActionForwardRequestConfig.
        :type _from: str
        """
        if _from is None:
            raise ValueError("Invalid value for `_from`, must not be `None`")

        self.__from = _from

    @property
    def key(self):
        """Gets the key of this AddActionForwardRequestConfig.


        :return: The key of this AddActionForwardRequestConfig.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this AddActionForwardRequestConfig.


        :param key: The key of this AddActionForwardRequestConfig.
        :type key: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")

        self._key = key

    @property
    def type(self):
        """Gets the type of this AddActionForwardRequestConfig.


        :return: The type of this AddActionForwardRequestConfig.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AddActionForwardRequestConfig.


        :param type: The type of this AddActionForwardRequestConfig.
        :type type: str
        """
        allowed_values = ["forward"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type
