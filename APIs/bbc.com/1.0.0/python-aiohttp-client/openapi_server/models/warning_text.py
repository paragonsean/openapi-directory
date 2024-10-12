# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class WarningText(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, text: str=None, length: str=None):
        """WarningText - a model defined in OpenAPI

        :param text: The text of this WarningText.
        :param length: The length of this WarningText.
        """
        self.openapi_types = {
            'text': str,
            'length': str
        }

        self.attribute_map = {
            'text': '#text',
            'length': 'length'
        }

        self._text = text
        self._length = length

    @classmethod
    def from_dict(cls, dikt: dict) -> 'WarningText':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The warning_text of this WarningText.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def text(self):
        """Gets the text of this WarningText.


        :return: The text of this WarningText.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this WarningText.


        :param text: The text of this WarningText.
        :type text: str
        """

        self._text = text

    @property
    def length(self):
        """Gets the length of this WarningText.


        :return: The length of this WarningText.
        :rtype: str
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this WarningText.


        :param length: The length of this WarningText.
        :type length: str
        """

        self._length = length
