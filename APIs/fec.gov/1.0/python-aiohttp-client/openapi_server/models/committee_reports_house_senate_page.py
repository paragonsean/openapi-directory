# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.committee_reports_house_senate import CommitteeReportsHouseSenate
from openapi_server.models.offset_info import OffsetInfo
from openapi_server import util


class CommitteeReportsHouseSenatePage(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, pagination: OffsetInfo=None, results: List[CommitteeReportsHouseSenate]=None):
        """CommitteeReportsHouseSenatePage - a model defined in OpenAPI

        :param pagination: The pagination of this CommitteeReportsHouseSenatePage.
        :param results: The results of this CommitteeReportsHouseSenatePage.
        """
        self.openapi_types = {
            'pagination': OffsetInfo,
            'results': List[CommitteeReportsHouseSenate]
        }

        self.attribute_map = {
            'pagination': 'pagination',
            'results': 'results'
        }

        self._pagination = pagination
        self._results = results

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CommitteeReportsHouseSenatePage':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The CommitteeReportsHouseSenatePage of this CommitteeReportsHouseSenatePage.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def pagination(self):
        """Gets the pagination of this CommitteeReportsHouseSenatePage.


        :return: The pagination of this CommitteeReportsHouseSenatePage.
        :rtype: OffsetInfo
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this CommitteeReportsHouseSenatePage.


        :param pagination: The pagination of this CommitteeReportsHouseSenatePage.
        :type pagination: OffsetInfo
        """

        self._pagination = pagination

    @property
    def results(self):
        """Gets the results of this CommitteeReportsHouseSenatePage.


        :return: The results of this CommitteeReportsHouseSenatePage.
        :rtype: List[CommitteeReportsHouseSenate]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this CommitteeReportsHouseSenatePage.


        :param results: The results of this CommitteeReportsHouseSenatePage.
        :type results: List[CommitteeReportsHouseSenate]
        """

        self._results = results
