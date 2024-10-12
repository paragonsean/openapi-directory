# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.property_performance_result import PropertyPerformanceResult
from openapi_server import util


class QueryPropertyPerformanceReportResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, next_page_token: str=None, results: List[PropertyPerformanceResult]=None):
        """QueryPropertyPerformanceReportResponse - a model defined in OpenAPI

        :param next_page_token: The next_page_token of this QueryPropertyPerformanceReportResponse.
        :param results: The results of this QueryPropertyPerformanceReportResponse.
        """
        self.openapi_types = {
            'next_page_token': str,
            'results': List[PropertyPerformanceResult]
        }

        self.attribute_map = {
            'next_page_token': 'nextPageToken',
            'results': 'results'
        }

        self._next_page_token = next_page_token
        self._results = results

    @classmethod
    def from_dict(cls, dikt: dict) -> 'QueryPropertyPerformanceReportResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The QueryPropertyPerformanceReportResponse of this QueryPropertyPerformanceReportResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def next_page_token(self):
        """Gets the next_page_token of this QueryPropertyPerformanceReportResponse.

        Pagination token used to retrieve the next page of results. If this field is omitted, there are no subsequent pages.

        :return: The next_page_token of this QueryPropertyPerformanceReportResponse.
        :rtype: str
        """
        return self._next_page_token

    @next_page_token.setter
    def next_page_token(self, next_page_token):
        """Sets the next_page_token of this QueryPropertyPerformanceReportResponse.

        Pagination token used to retrieve the next page of results. If this field is omitted, there are no subsequent pages.

        :param next_page_token: The next_page_token of this QueryPropertyPerformanceReportResponse.
        :type next_page_token: str
        """

        self._next_page_token = next_page_token

    @property
    def results(self):
        """Gets the results of this QueryPropertyPerformanceReportResponse.

        The list of results that match the query.

        :return: The results of this QueryPropertyPerformanceReportResponse.
        :rtype: List[PropertyPerformanceResult]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this QueryPropertyPerformanceReportResponse.

        The list of results that match the query.

        :param results: The results of this QueryPropertyPerformanceReportResponse.
        :type results: List[PropertyPerformanceResult]
        """

        self._results = results
