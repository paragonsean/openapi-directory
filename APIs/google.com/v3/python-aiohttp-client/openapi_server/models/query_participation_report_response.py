# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.participation_result import ParticipationResult
from openapi_server import util


class QueryParticipationReportResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, next_page_token: str=None, results: List[ParticipationResult]=None):
        """QueryParticipationReportResponse - a model defined in OpenAPI

        :param next_page_token: The next_page_token of this QueryParticipationReportResponse.
        :param results: The results of this QueryParticipationReportResponse.
        """
        self.openapi_types = {
            'next_page_token': str,
            'results': List[ParticipationResult]
        }

        self.attribute_map = {
            'next_page_token': 'nextPageToken',
            'results': 'results'
        }

        self._next_page_token = next_page_token
        self._results = results

    @classmethod
    def from_dict(cls, dikt: dict) -> 'QueryParticipationReportResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The QueryParticipationReportResponse of this QueryParticipationReportResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def next_page_token(self):
        """Gets the next_page_token of this QueryParticipationReportResponse.

        Pagination token used to retrieve the next page of results.

        :return: The next_page_token of this QueryParticipationReportResponse.
        :rtype: str
        """
        return self._next_page_token

    @next_page_token.setter
    def next_page_token(self, next_page_token):
        """Sets the next_page_token of this QueryParticipationReportResponse.

        Pagination token used to retrieve the next page of results.

        :param next_page_token: The next_page_token of this QueryParticipationReportResponse.
        :type next_page_token: str
        """

        self._next_page_token = next_page_token

    @property
    def results(self):
        """Gets the results of this QueryParticipationReportResponse.

        The list of results that matches the query.

        :return: The results of this QueryParticipationReportResponse.
        :rtype: List[ParticipationResult]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this QueryParticipationReportResponse.

        The list of results that matches the query.

        :param results: The results of this QueryParticipationReportResponse.
        :type results: List[ParticipationResult]
        """

        self._results = results
