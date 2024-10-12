# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class URL(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, content: str=None, type: str=None):
        """URL - a model defined in OpenAPI

        :param content: The content of this URL.
        :param type: The type of this URL.
        """
        self.openapi_types = {
            'content': str,
            'type': str
        }

        self.attribute_map = {
            'content': '_content',
            'type': 'type'
        }

        self._content = content
        self._type = type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'URL':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The URL of this URL.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def content(self):
        """Gets the content of this URL.


        :return: The content of this URL.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this URL.


        :param content: The content of this URL.
        :type content: str
        """

        self._content = content

    @property
    def type(self):
        """Gets the type of this URL.


        :return: The type of this URL.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this URL.


        :param type: The type of this URL.
        :type type: str
        """

        self._type = type
