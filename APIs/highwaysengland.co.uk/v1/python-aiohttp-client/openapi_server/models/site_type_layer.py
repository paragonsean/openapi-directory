# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.sites import Sites
from openapi_server import util


class SiteTypeLayer(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, sites: List[Sites]=None):
        """SiteTypeLayer - a model defined in OpenAPI

        :param sites: The sites of this SiteTypeLayer.
        """
        self.openapi_types = {
            'sites': List[Sites]
        }

        self.attribute_map = {
            'sites': 'Sites'
        }

        self._sites = sites

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SiteTypeLayer':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The SiteTypeLayer of this SiteTypeLayer.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def sites(self):
        """Gets the sites of this SiteTypeLayer.


        :return: The sites of this SiteTypeLayer.
        :rtype: List[Sites]
        """
        return self._sites

    @sites.setter
    def sites(self, sites):
        """Sets the sites of this SiteTypeLayer.


        :param sites: The sites of this SiteTypeLayer.
        :type sites: List[Sites]
        """

        self._sites = sites
