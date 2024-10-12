# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.site_result import SiteResult
from openapi_server import util


class SiteResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, row_count: int=None, sites: List[SiteResult]=None):
        """SiteResponse - a model defined in OpenAPI

        :param row_count: The row_count of this SiteResponse.
        :param sites: The sites of this SiteResponse.
        """
        self.openapi_types = {
            'row_count': int,
            'sites': List[SiteResult]
        }

        self.attribute_map = {
            'row_count': 'row_count',
            'sites': 'sites'
        }

        self._row_count = row_count
        self._sites = sites

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SiteResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The SiteResponse of this SiteResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def row_count(self):
        """Gets the row_count of this SiteResponse.


        :return: The row_count of this SiteResponse.
        :rtype: int
        """
        return self._row_count

    @row_count.setter
    def row_count(self, row_count):
        """Sets the row_count of this SiteResponse.


        :param row_count: The row_count of this SiteResponse.
        :type row_count: int
        """

        self._row_count = row_count

    @property
    def sites(self):
        """Gets the sites of this SiteResponse.


        :return: The sites of this SiteResponse.
        :rtype: List[SiteResult]
        """
        return self._sites

    @sites.setter
    def sites(self, sites):
        """Sets the sites of this SiteResponse.


        :param sites: The sites of this SiteResponse.
        :type sites: List[SiteResult]
        """

        self._sites = sites
