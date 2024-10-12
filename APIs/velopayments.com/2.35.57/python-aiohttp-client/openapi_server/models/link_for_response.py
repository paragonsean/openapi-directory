# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class LinkForResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, href: str=None, rel: str=None):
        """LinkForResponse - a model defined in OpenAPI

        :param href: The href of this LinkForResponse.
        :param rel: The rel of this LinkForResponse.
        """
        self.openapi_types = {
            'href': str,
            'rel': str
        }

        self.attribute_map = {
            'href': 'href',
            'rel': 'rel'
        }

        self._href = href
        self._rel = rel

    @classmethod
    def from_dict(cls, dikt: dict) -> 'LinkForResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The LinkForResponse of this LinkForResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def href(self):
        """Gets the href of this LinkForResponse.


        :return: The href of this LinkForResponse.
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this LinkForResponse.


        :param href: The href of this LinkForResponse.
        :type href: str
        """

        self._href = href

    @property
    def rel(self):
        """Gets the rel of this LinkForResponse.


        :return: The rel of this LinkForResponse.
        :rtype: str
        """
        return self._rel

    @rel.setter
    def rel(self, rel):
        """Sets the rel of this LinkForResponse.


        :param rel: The rel of this LinkForResponse.
        :type rel: str
        """

        self._rel = rel
