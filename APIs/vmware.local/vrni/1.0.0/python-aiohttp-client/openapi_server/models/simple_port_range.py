# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class SimplePortRange(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, end: int=None, start: int=None):
        """SimplePortRange - a model defined in OpenAPI

        :param end: The end of this SimplePortRange.
        :param start: The start of this SimplePortRange.
        """
        self.openapi_types = {
            'end': int,
            'start': int
        }

        self.attribute_map = {
            'end': 'end',
            'start': 'start'
        }

        self._end = end
        self._start = start

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SimplePortRange':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The SimplePortRange of this SimplePortRange.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def end(self):
        """Gets the end of this SimplePortRange.


        :return: The end of this SimplePortRange.
        :rtype: int
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this SimplePortRange.


        :param end: The end of this SimplePortRange.
        :type end: int
        """

        self._end = end

    @property
    def start(self):
        """Gets the start of this SimplePortRange.


        :return: The start of this SimplePortRange.
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this SimplePortRange.


        :param start: The start of this SimplePortRange.
        :type start: int
        """

        self._start = start
