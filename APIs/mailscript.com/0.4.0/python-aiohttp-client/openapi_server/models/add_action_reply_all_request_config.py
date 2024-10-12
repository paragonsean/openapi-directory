# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class AddActionReplyAllRequestConfig(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, _from: str=None, html: str=None, key: str=None, text: str=None, type: str=None):
        """AddActionReplyAllRequestConfig - a model defined in OpenAPI

        :param _from: The _from of this AddActionReplyAllRequestConfig.
        :param html: The html of this AddActionReplyAllRequestConfig.
        :param key: The key of this AddActionReplyAllRequestConfig.
        :param text: The text of this AddActionReplyAllRequestConfig.
        :param type: The type of this AddActionReplyAllRequestConfig.
        """
        self.openapi_types = {
            '_from': str,
            'html': str,
            'key': str,
            'text': str,
            'type': str
        }

        self.attribute_map = {
            '_from': 'from',
            'html': 'html',
            'key': 'key',
            'text': 'text',
            'type': 'type'
        }

        self.__from = _from
        self._html = html
        self._key = key
        self._text = text
        self._type = type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AddActionReplyAllRequestConfig':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The AddActionReplyAllRequest_config of this AddActionReplyAllRequestConfig.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def _from(self):
        """Gets the _from of this AddActionReplyAllRequestConfig.


        :return: The _from of this AddActionReplyAllRequestConfig.
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this AddActionReplyAllRequestConfig.


        :param _from: The _from of this AddActionReplyAllRequestConfig.
        :type _from: str
        """
        if _from is None:
            raise ValueError("Invalid value for `_from`, must not be `None`")

        self.__from = _from

    @property
    def html(self):
        """Gets the html of this AddActionReplyAllRequestConfig.


        :return: The html of this AddActionReplyAllRequestConfig.
        :rtype: str
        """
        return self._html

    @html.setter
    def html(self, html):
        """Sets the html of this AddActionReplyAllRequestConfig.


        :param html: The html of this AddActionReplyAllRequestConfig.
        :type html: str
        """

        self._html = html

    @property
    def key(self):
        """Gets the key of this AddActionReplyAllRequestConfig.


        :return: The key of this AddActionReplyAllRequestConfig.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this AddActionReplyAllRequestConfig.


        :param key: The key of this AddActionReplyAllRequestConfig.
        :type key: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")

        self._key = key

    @property
    def text(self):
        """Gets the text of this AddActionReplyAllRequestConfig.


        :return: The text of this AddActionReplyAllRequestConfig.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this AddActionReplyAllRequestConfig.


        :param text: The text of this AddActionReplyAllRequestConfig.
        :type text: str
        """

        self._text = text

    @property
    def type(self):
        """Gets the type of this AddActionReplyAllRequestConfig.


        :return: The type of this AddActionReplyAllRequestConfig.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AddActionReplyAllRequestConfig.


        :param type: The type of this AddActionReplyAllRequestConfig.
        :type type: str
        """
        allowed_values = ["replyAll"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type
