# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.elections_list import ElectionsList
from openapi_server.models.offset_info import OffsetInfo
from openapi_server import util


class ElectionsListPage(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, pagination: OffsetInfo=None, results: List[ElectionsList]=None):
        """ElectionsListPage - a model defined in OpenAPI

        :param pagination: The pagination of this ElectionsListPage.
        :param results: The results of this ElectionsListPage.
        """
        self.openapi_types = {
            'pagination': OffsetInfo,
            'results': List[ElectionsList]
        }

        self.attribute_map = {
            'pagination': 'pagination',
            'results': 'results'
        }

        self._pagination = pagination
        self._results = results

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ElectionsListPage':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ElectionsListPage of this ElectionsListPage.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def pagination(self):
        """Gets the pagination of this ElectionsListPage.


        :return: The pagination of this ElectionsListPage.
        :rtype: OffsetInfo
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this ElectionsListPage.


        :param pagination: The pagination of this ElectionsListPage.
        :type pagination: OffsetInfo
        """

        self._pagination = pagination

    @property
    def results(self):
        """Gets the results of this ElectionsListPage.


        :return: The results of this ElectionsListPage.
        :rtype: List[ElectionsList]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this ElectionsListPage.


        :param results: The results of this ElectionsListPage.
        :type results: List[ElectionsList]
        """

        self._results = results
