# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class InputTrimString(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, source: str=None, type: str=None):
        """InputTrimString - a model defined in OpenAPI

        :param source: The source of this InputTrimString.
        :param type: The type of this InputTrimString.
        """
        self.openapi_types = {
            'source': str,
            'type': str
        }

        self.attribute_map = {
            'source': 'source',
            'type': 'type'
        }

        self._source = source
        self._type = type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'InputTrimString':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The inputTrimString of this InputTrimString.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def source(self):
        """Gets the source of this InputTrimString.

        String containing the text to be trimmed

        :return: The source of this InputTrimString.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this InputTrimString.

        String containing the text to be trimmed

        :param source: The source of this InputTrimString.
        :type source: str
        """
        if source is None:
            raise ValueError("Invalid value for `source`, must not be `None`")

        self._source = source

    @property
    def type(self):
        """Gets the type of this InputTrimString.

        Type of white space to remove

        :return: The type of this InputTrimString.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InputTrimString.

        Type of white space to remove

        :param type: The type of this InputTrimString.
        :type type: str
        """
        allowed_values = ["Start", "End", "Both"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type
