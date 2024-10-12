# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class InputNumberRange(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, end: float=None, start: float=None):
        """InputNumberRange - a model defined in OpenAPI

        :param end: The end of this InputNumberRange.
        :param start: The start of this InputNumberRange.
        """
        self.openapi_types = {
            'end': float,
            'start': float
        }

        self.attribute_map = {
            'end': 'end',
            'start': 'start'
        }

        self._end = end
        self._start = start

    @classmethod
    def from_dict(cls, dikt: dict) -> 'InputNumberRange':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The inputNumberRange of this InputNumberRange.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def end(self):
        """Gets the end of this InputNumberRange.

        End of range

        :return: The end of this InputNumberRange.
        :rtype: float
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this InputNumberRange.

        End of range

        :param end: The end of this InputNumberRange.
        :type end: float
        """
        if end is None:
            raise ValueError("Invalid value for `end`, must not be `None`")
        if end is not None and end < 0:
            raise ValueError("Invalid value for `end`, must be a value greater than or equal to `0`")

        self._end = end

    @property
    def start(self):
        """Gets the start of this InputNumberRange.

        Start of range

        :return: The start of this InputNumberRange.
        :rtype: float
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this InputNumberRange.

        Start of range

        :param start: The start of this InputNumberRange.
        :type start: float
        """
        if start is None:
            raise ValueError("Invalid value for `start`, must not be `None`")
        if start is not None and start < 0:
            raise ValueError("Invalid value for `start`, must be a value greater than or equal to `0`")

        self._start = start
