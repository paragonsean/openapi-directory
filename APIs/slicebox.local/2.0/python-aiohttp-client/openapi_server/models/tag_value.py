# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.tag_path_tag import TagPathTag
from openapi_server import util


class TagValue(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, tag_path: TagPathTag=None, value: str=None):
        """TagValue - a model defined in OpenAPI

        :param tag_path: The tag_path of this TagValue.
        :param value: The value of this TagValue.
        """
        self.openapi_types = {
            'tag_path': TagPathTag,
            'value': str
        }

        self.attribute_map = {
            'tag_path': 'tagPath',
            'value': 'value'
        }

        self._tag_path = tag_path
        self._value = value

    @classmethod
    def from_dict(cls, dikt: dict) -> 'TagValue':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The tagValue of this TagValue.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def tag_path(self):
        """Gets the tag_path of this TagValue.


        :return: The tag_path of this TagValue.
        :rtype: TagPathTag
        """
        return self._tag_path

    @tag_path.setter
    def tag_path(self, tag_path):
        """Sets the tag_path of this TagValue.


        :param tag_path: The tag_path of this TagValue.
        :type tag_path: TagPathTag
        """

        self._tag_path = tag_path

    @property
    def value(self):
        """Gets the value of this TagValue.


        :return: The value of this TagValue.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this TagValue.


        :param value: The value of this TagValue.
        :type value: str
        """

        self._value = value
