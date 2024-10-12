# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.audit_category import AuditCategory
from openapi_server.models.offset_info import OffsetInfo
from openapi_server import util


class AuditCategoryPage(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, pagination: OffsetInfo=None, results: List[AuditCategory]=None):
        """AuditCategoryPage - a model defined in OpenAPI

        :param pagination: The pagination of this AuditCategoryPage.
        :param results: The results of this AuditCategoryPage.
        """
        self.openapi_types = {
            'pagination': OffsetInfo,
            'results': List[AuditCategory]
        }

        self.attribute_map = {
            'pagination': 'pagination',
            'results': 'results'
        }

        self._pagination = pagination
        self._results = results

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AuditCategoryPage':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The AuditCategoryPage of this AuditCategoryPage.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def pagination(self):
        """Gets the pagination of this AuditCategoryPage.


        :return: The pagination of this AuditCategoryPage.
        :rtype: OffsetInfo
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this AuditCategoryPage.


        :param pagination: The pagination of this AuditCategoryPage.
        :type pagination: OffsetInfo
        """

        self._pagination = pagination

    @property
    def results(self):
        """Gets the results of this AuditCategoryPage.


        :return: The results of this AuditCategoryPage.
        :rtype: List[AuditCategory]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this AuditCategoryPage.


        :param results: The results of this AuditCategoryPage.
        :type results: List[AuditCategory]
        """

        self._results = results
