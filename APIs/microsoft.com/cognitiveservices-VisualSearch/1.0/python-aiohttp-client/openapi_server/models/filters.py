# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Filters(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, site: str=None):
        """Filters - a model defined in OpenAPI

        :param site: The site of this Filters.
        """
        self.openapi_types = {
            'site': str
        }

        self.attribute_map = {
            'site': 'site'
        }

        self._site = site

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Filters':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Filters of this Filters.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def site(self):
        """Gets the site of this Filters.

        The URL of the site to return similar images and similar products from. (e.g., \"www.bing.com\", \"bing.com\").

        :return: The site of this Filters.
        :rtype: str
        """
        return self._site

    @site.setter
    def site(self, site):
        """Sets the site of this Filters.

        The URL of the site to return similar images and similar products from. (e.g., \"www.bing.com\", \"bing.com\").

        :param site: The site of this Filters.
        :type site: str
        """

        self._site = site
