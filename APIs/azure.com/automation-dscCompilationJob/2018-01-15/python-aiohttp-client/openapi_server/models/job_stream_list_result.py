# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.job_stream import JobStream
from openapi_server import util


class JobStreamListResult(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, next_link: str=None, value: List[JobStream]=None):
        """JobStreamListResult - a model defined in OpenAPI

        :param next_link: The next_link of this JobStreamListResult.
        :param value: The value of this JobStreamListResult.
        """
        self.openapi_types = {
            'next_link': str,
            'value': List[JobStream]
        }

        self.attribute_map = {
            'next_link': 'nextLink',
            'value': 'value'
        }

        self._next_link = next_link
        self._value = value

    @classmethod
    def from_dict(cls, dikt: dict) -> 'JobStreamListResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The JobStreamListResult of this JobStreamListResult.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def next_link(self):
        """Gets the next_link of this JobStreamListResult.

        Gets or sets the next link.

        :return: The next_link of this JobStreamListResult.
        :rtype: str
        """
        return self._next_link

    @next_link.setter
    def next_link(self, next_link):
        """Sets the next_link of this JobStreamListResult.

        Gets or sets the next link.

        :param next_link: The next_link of this JobStreamListResult.
        :type next_link: str
        """

        self._next_link = next_link

    @property
    def value(self):
        """Gets the value of this JobStreamListResult.

        A list of job streams.

        :return: The value of this JobStreamListResult.
        :rtype: List[JobStream]
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this JobStreamListResult.

        A list of job streams.

        :param value: The value of this JobStreamListResult.
        :type value: List[JobStream]
        """

        self._value = value
