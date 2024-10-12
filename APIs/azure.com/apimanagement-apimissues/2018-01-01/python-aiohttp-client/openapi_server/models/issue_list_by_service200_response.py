# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.issue_list_by_service200_response_value_inner import IssueListByService200ResponseValueInner
from openapi_server import util


class IssueListByService200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, next_link: str=None, value: List[IssueListByService200ResponseValueInner]=None):
        """IssueListByService200Response - a model defined in OpenAPI

        :param next_link: The next_link of this IssueListByService200Response.
        :param value: The value of this IssueListByService200Response.
        """
        self.openapi_types = {
            'next_link': str,
            'value': List[IssueListByService200ResponseValueInner]
        }

        self.attribute_map = {
            'next_link': 'nextLink',
            'value': 'value'
        }

        self._next_link = next_link
        self._value = value

    @classmethod
    def from_dict(cls, dikt: dict) -> 'IssueListByService200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Issue_ListByService_200_response of this IssueListByService200Response.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def next_link(self):
        """Gets the next_link of this IssueListByService200Response.

        Next page link if any.

        :return: The next_link of this IssueListByService200Response.
        :rtype: str
        """
        return self._next_link

    @next_link.setter
    def next_link(self, next_link):
        """Sets the next_link of this IssueListByService200Response.

        Next page link if any.

        :param next_link: The next_link of this IssueListByService200Response.
        :type next_link: str
        """

        self._next_link = next_link

    @property
    def value(self):
        """Gets the value of this IssueListByService200Response.

        Issue values.

        :return: The value of this IssueListByService200Response.
        :rtype: List[IssueListByService200ResponseValueInner]
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this IssueListByService200Response.

        Issue values.

        :param value: The value of this IssueListByService200Response.
        :type value: List[IssueListByService200ResponseValueInner]
        """

        self._value = value
