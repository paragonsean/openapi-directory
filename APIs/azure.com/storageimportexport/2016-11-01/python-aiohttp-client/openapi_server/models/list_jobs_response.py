# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.job_response import JobResponse
from openapi_server import util


class ListJobsResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, next_link: str=None, value: List[JobResponse]=None):
        """ListJobsResponse - a model defined in OpenAPI

        :param next_link: The next_link of this ListJobsResponse.
        :param value: The value of this ListJobsResponse.
        """
        self.openapi_types = {
            'next_link': str,
            'value': List[JobResponse]
        }

        self.attribute_map = {
            'next_link': 'nextLink',
            'value': 'value'
        }

        self._next_link = next_link
        self._value = value

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ListJobsResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ListJobsResponse of this ListJobsResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def next_link(self):
        """Gets the next_link of this ListJobsResponse.

        link to next batch of jobs

        :return: The next_link of this ListJobsResponse.
        :rtype: str
        """
        return self._next_link

    @next_link.setter
    def next_link(self, next_link):
        """Sets the next_link of this ListJobsResponse.

        link to next batch of jobs

        :param next_link: The next_link of this ListJobsResponse.
        :type next_link: str
        """

        self._next_link = next_link

    @property
    def value(self):
        """Gets the value of this ListJobsResponse.

        Job list

        :return: The value of this ListJobsResponse.
        :rtype: List[JobResponse]
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ListJobsResponse.

        Job list

        :param value: The value of this ListJobsResponse.
        :type value: List[JobResponse]
        """

        self._value = value
